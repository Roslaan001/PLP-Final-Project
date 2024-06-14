
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from cart.forms import CartAddProductForm
from .models import Category, Product
from django.views.generic import ListView


class ProductListView(ListView):
    model = Product
    template_name = 'yourapp/product_list.html'
    context_object_name = 'products'

class ProductListByCategoryView(ListView):
    model = Product
    template_name = 'yourapp/product_list_by_category.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        return Product.objects.filter(category__slug=category_slug)



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    product_list_url = reverse('shop:product_list')  # Get the URL for product list view
    print(f"Generated URL for product list: {product_list_url}")
    # ...  rest of your view code

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(
        request,
        'shop/product/list.html',
        {
            'category': category,
            'categories': categories,
            'products': products,
        },
    )



def product_detail(request, id, slug):
    product = get_object_or_404(
        Product, id=id, slug=slug, available=True
    )
    cart_product_form = CartAddProductForm()
    return render(
        request,
        'shop/product/detail.html',
        {'product': product, 'cart_product_form': cart_product_form},
    )
    
    
