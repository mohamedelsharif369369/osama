from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
from .forms import ProductForm , ProductUpdateForm

# Create your views here.

    

def products(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            return redirect('/products')
    else:
        product_form = ProductForm()
    product = Product.objects.all()
    return render(request,'products/products.html',{
        'product':product,'product_form':product_form
        })
    return render(request,'',{})

def edit_products(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        edit_form = ProductUpdateForm(request.POST,instance=obj)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('/products')
    else:
        edit_form = ProductUpdateForm(instance=obj)
    return render(request,'products/edit_products.html',{'edit_form':edit_form})



def delete_products(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        edit_form = ProductUpdateForm(request.POST,instance=obj)
        obj.delete()
        return redirect('/products')
    return render(request,'products/delete_products.html',{'object':obj})