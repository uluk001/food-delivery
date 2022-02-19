from unicodedata import category, name
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from core.models import FoodCard, Category, ProductsCart
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your views here.
def base(request):
    categories = Category.objects.all() 
    foodCards = FoodCard.objects.all()
    context = {'foodCards':foodCards, 'categories':categories}
    return render(request, 'index.html', context=context)


def product(request, id):
    foodcard = FoodCard.objects.get(id=id)
    one_type_categories = FoodCard.objects.all().filter(category=foodcard.category)
    return render(request, 'product.html', {'foodcard':foodcard, 'one_type_categories':one_type_categories})


cart_products = []
res = {}
def addCart(request, pk):
    cart_session = request.session.get('cart_session', [])
    count_of_product = len(cart_session)
    cart_products.append(pk)
    # product_Cart = FoodCard.objects.filter(id__in=cart_products)
    # for i in product_Cart:
    #     p_name = i.name
    #     p_count = cart_products.count(i.id)
    #     p_price = i.price
    #     p_description = i.description
    #     total_sum = p_count * p_price
    #     context = {
    #         'p_name':p_name,
    #         'p_count':p_count,
    #         'p_description':p_description,
    #         'p_price':p_price,
    #         'total_sum':total_sum,
    #         'product_Cart':product_Cart
    #     }
    # for i in cart_products:
    #     if i in res:
    #         res[i] += 1
    #     else:
    #         res[i] = 1
    # product = FoodCard.objects.get(id = pk)
    # product_cart = ProductsCart()
    # products_cart = ProductsCart.objects.all()
    # product_cart.user = request.user
    # product_cart.product = product.name
    # product_cart.photo = product.image.url
    # product_cart.price = product.price
    # product_cart.count = res[pk]
    # product_cart.total_price = product_cart.price * product_cart.count
    # product_cart.save()
    # print(product.price)
    return HttpResponseRedirect('/')

def cart(request):
    cart_session = request.session.get('cart_session', [])
    count_of_product = len(cart_session)
    product_Cart = FoodCard.objects.filter(id__in=cart_products)
    all_products_sum = 0
    for i in product_Cart:
        total_sum = cart_products.count(i.id) * i.price
        all_products_sum += total_sum
        i.count = cart_products.count(i.id)
        count_of_product += i.count
        i.sum = cart_products.count(i.id) * i.price
    return render(request, "cart.html", {'product_Cart':product_Cart, 'all_products_sum':all_products_sum, 'count_of_product':count_of_product})

def removeCart(request ,id):
    cart_session = request.session.get('cart_session', [])
    print(cart_session)
    carts = []
    for i in cart_session:
        if id !=i:
            carts.append(i)
    request.session['cart_session'] = carts
    return redirect('cart')



def aboutUs(request):
    return render(request, 'about.html')



def search(request):
    if request.method == 'POST':
        searched_product = request.POST.get('search').title()
        # product = FoodCard.objects.get(name = searched_product)
        product = FoodCard.objects.filter(name__contains = searched_product)
        return render(request, 'search.html', {'searched_product':searched_product, 'product':product})
