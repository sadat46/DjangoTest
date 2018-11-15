from django.shortcuts import render
from .forms import ProductForm
from .models import Product
# Create your views here.

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

def product_detail_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list":queryset
     }
    return render(request, "products/product_details.html", context)

        #def product_detail_view(request):
            # context = {
             #   'object': obj
           # }
           # return render(request, "products/product_details.html", context)"""

