import os
from pathlib import Path
import posixpath
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.db.models import Q
from .models import ProductImage, Product
from .forms import ProductImageUploadForm, ProductForm, VariantFormSet


def index(request):
    """Products app home page"""
    return HttpResponse("Products App - iPOS System")


def _collect_media_files():
    """Return list of media files with link status, sorted newest first."""
    media_root: Path = Path(settings.MEDIA_ROOT)
    image_exts = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'}
    files = []
    if media_root.exists():
        for root, _, filenames in os.walk(media_root):
            for fname in filenames:
                ext = os.path.splitext(fname)[1].lower()
                if ext not in image_exts:
                    continue
                abs_path = Path(root) / fname
                try:
                    mtime = abs_path.stat().st_mtime
                except Exception:
                    mtime = 0
                rel_path = abs_path.relative_to(media_root).as_posix()
                url = posixpath.join(settings.MEDIA_URL.rstrip('/'), rel_path)
                files.append({
                    'rel': rel_path,
                    'url': url,
                    'mtime': mtime,
                })
    files.sort(key=lambda x: x['mtime'], reverse=True)
    return files


def _enrich_files_with_links(files):
    """Given bare file dicts from _collect_media_files, attach DB link info."""
    link_map = {}
    qs = ProductImage.objects.select_related('product', 'variant', 'variant__product')
    for pi in qs:
        link_map.setdefault(pi.image.name, []).append(pi)

    enriched = []
    for f in files:
        links = link_map.get(f['rel'], [])
        linked_products = []
        linked_variants = []
        for pi in links:
            if pi.product_id and pi.product:
                linked_products.append({
                    'id': pi.product_id,
                    'name': pi.product.name,
                    'url': reverse('products:product_edit', args=[pi.product_id]),
                })
            if pi.variant_id and pi.variant:
                pid = pi.variant.product_id
                vname = pi.variant.name
                url = reverse('products:product_edit', args=[pid]) + f"#variant-{pi.variant_id}" if pid else '#'
                linked_variants.append({
                    'id': pi.variant_id,
                    'name': vname,
                    'url': url,
                })
        enriched.append({
            **f,
            'is_linked': bool(linked_products or linked_variants),
            'linked_products': linked_products,
            'linked_variants': linked_variants,
        })
    return enriched


def media_manager(request):
    """Page shell: grid is loaded via htmx; upload form is shown in modal."""
    return render(request, 'products/media_manager.html')


def media_grid(request):
    files = _collect_media_files()
    enriched = _enrich_files_with_links(files)
    return render(request, 'products/partials/media_grid.html', { 'files': enriched })


def upload_media(request):
    if request.method == 'POST':
        form = ProductImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # If htmx request, instruct client to redirect
            if request.headers.get('HX-Request'):
                resp = HttpResponse("", status=204)
                resp['HX-Redirect'] = reverse('products:media_manager')
                return resp
            # Fallback for non-htmx
            return redirect('products:media_manager')
    else:
        form = ProductImageUploadForm()
    return render(request, 'products/partials/upload_form.html', { 'form': form })


def delete_media(request):
    """Delete an unlinked media file by relative path under MEDIA_ROOT."""
    if request.method != 'POST':
        return HttpResponseBadRequest('Invalid method')

    rel_path = request.POST.get('path')
    if not rel_path:
        return HttpResponseBadRequest('Missing path')

    # Security: normalize and ensure inside MEDIA_ROOT
    media_root: Path = Path(settings.MEDIA_ROOT)
    abs_path = (media_root / rel_path).resolve()
    if media_root not in abs_path.parents and abs_path != media_root:
        return HttpResponseBadRequest('Invalid path')

    # Block deletion if linked in DB (has product or variant)
    if ProductImage.objects.filter(
        Q(image=rel_path) & (Q(product__isnull=False) | Q(variant__isnull=False))
    ).exists():
        return HttpResponseBadRequest('File is linked to a product/variant. Unlink first.')

    # Delete if exists
    try:
        if abs_path.exists():
            abs_path.unlink()
    except Exception:
        pass

    # Clean up orphan ProductImage rows (no product and no variant)
    ProductImage.objects.filter(
        Q(image=rel_path) & Q(product__isnull=True) & Q(variant__isnull=True)
    ).delete()

    if request.headers.get('HX-Request'):
        files = _collect_media_files()
        enriched = _enrich_files_with_links(files)
        return render(request, 'products/partials/media_grid.html', { 'files': enriched })
    return redirect('products:media_manager')


# Product pages
def product_list(request):
    products = (
        Product.objects
        .select_related('category')
        .prefetch_related('images')
        .order_by('-created_at')
    )
    return render(request, 'products/product_list.html', { 'products': products })


def product_edit(request, pk: int):
    from django.shortcuts import get_object_or_404
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    formset = VariantFormSet(request.POST or None, instance=product)

    if request.method == 'POST' and form.is_valid() and formset.is_valid():
        form.save()
        formset.save()
        return redirect('products:product_list')

    return render(request, 'products/product_form.html', {
        'product': product,
        'form': form,
        'formset': formset,
    })

