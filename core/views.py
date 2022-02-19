from unicodedata import category, name
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from core.models import FoodCard, Category, ProductsCart
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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


res = {}
def addCart(request, pk):
    cart_session = request.session.get('cart_session', [])
    cart_session.append(pk)
    request.session['cart_session'] = cart_session
    return redirect('base')

def cart(request):
    cart_session = request.session.get('cart_session', [])
    count_of_product = len(cart_session)
    product_Cart = FoodCard.objects.filter(id__in=cart_session)

    all_products_sum = 0
    for i in product_Cart:
        i.count = cart_session.count(i.id)
        count_of_product += i.count
        i.sum = cart_session.count(i.id) * i.price
    return render(request, "cart.html", {'product_Cart':product_Cart, 'all_products_sum':all_products_sum, 'count_of_product':count_of_product})







def removeCart(request ,id):
    cart_session = request.session.get('cart_session', [])
    carts = []
    for pk in cart_session:
        if pk !=id:
            carts.append(pk)
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

def signUp(request):
    if request.method == 'POST':
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            return redirect('base')
    else:
        user = UserCreationForm()

    return render(request, 'auth.html', {'user':user})
