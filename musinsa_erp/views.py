from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/erp')
    else:
        return redirect('/sign-in')


def erp(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            all_product = Product.objects.all().order_by()
            return render(request, 'musinsa_erp/home.html', {'product': all_product})
    elif request.method == "POST":
        user = request.user
        my_product = Product()
        my_product.author = user
        my_product.category = request.POST.get('category', '')
        my_product.code = request.POST.get('code', '')
        my_product.name = request.POST.get('name', '')
        my_product.price = request.POST.get('price', '')
        my_product.size = request.POST.get('size', '')
        my_product.description = request.POST.get('description', '')
        my_product.save()
        return redirect('/erp')


@login_required
def delete_erp(request, id):
    my_product = Product.objects.get(id=id)
    my_product.delete()
    return redirect('/erp')


def inventory(request, id):
    my_product = Product.objects.get(id=id)
    return render(request, 'musinsa_erp/inventory.html', {'product': my_product})