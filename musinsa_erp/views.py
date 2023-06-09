from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from inventory.forms import InventoryForm
from inventory.models import Inventory
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model  # 사용자가 데이터베이스 안에 있는지 검사하는 함수
# Create your views here.


def home(request):
    user = request.user.is_authenticated
    if user:
        product_form = ProductForm()
        return redirect('/erp', {'product_form': product_form})
    else:
        return redirect('/sign-in')


# 상품등록
def erp(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            user = request.user
            all_product = Product.objects.filter(author_id=user).order_by()
            product_form = ProductForm()
            return render(request, 'musinsa_erp/home.html', {'product': all_product, 'product_form':product_form})
    elif request.method == "POST":
        user = request.user
        my_product = Product()
        my_product.author = user
        form = request.POST
        my_product.category = form['category']
        my_product.code = form['code']
        my_product.name = form['name']
        my_product.price = form['price']
        my_product.size = form['size']
        my_product.description = form['size']
        check_name = Product.objects.filter(name=my_product.name, author=user)
        check_size = Product.objects.filter(size=my_product.size, author=user)

        if my_product.code in Product.objects.filter(author_id=user):
            print('이미 존재하는 상품입니다.')
            return redirect('/erp')
        else:  # 상품 등록과 동시에 재고관리 Db에도 저장
            my_product.save()
            my_inventory = Inventory()
            my_inventory.author = user
            my_inventory.increased_inventory = 0
            my_inventory.decreased_inventory = 0
            my_product = Product.objects.get(id=my_product.id)
            my_inventory.product = my_product
            my_inventory.save()
            return redirect('/erp')


@login_required
def show_list(request, id):
    my_inventory = Inventory.objects.filter(author_id=id).order_by('product__category', 'product__name'
                                                                     , 'product__code')  # 해당유저
    return render(request, 'musinsa_erp/product list.html', {'inventory': my_inventory})


@login_required
def delete_erp(request, id):
    my_product = Product.objects.get(id=id)
    my_product.delete()
    return redirect('/erp')


@login_required
def inventory(request, id):
    if request.method == 'GET':
        user = request.user
        my_inventory = Inventory.objects.filter(author_id=user).order_by('product__category', 'product__name'
                                                                         , 'product__code')  # 해당유저
        inventory_form = InventoryForm()
        return render(request, 'musinsa_erp/inventory.html', {'inventory': my_inventory, 'inventory_form': inventory_form})
    elif request.method == 'POST':
        code = request.POST.get('code', '')
        if code == '':
            return redirect('inventory', id)
        else:
            product_id = Product.objects.get(code=code)
            my_inventory = Inventory.objects.get(product_id=product_id.id)
            my_inventory.increased_inventory += int(request.POST.get('increased_inventory', ''))
            my_inventory.save()
            return redirect('inventory', id)


@login_required
def delete_inventory(request, id):
    code = request.POST.get('code', '')
    if code == "":
        return redirect('inventory', id)
    else:
        product_id = Product.objects.get(code=code)
        my_inventory = Inventory.objects.get(product_id=product_id.id)
        if my_inventory.increased_inventory < int(request.POST.get('increased_inventory', '')):
            print('재고가 부족합니다.')
            return redirect('inventory', id)
        else:
            my_inventory.increased_inventory -= int(request.POST.get('increased_inventory', ''))
            my_inventory.decreased_inventory += int(request.POST.get('increased_inventory', ''))
            my_inventory.save()
            return redirect('inventory', id)
