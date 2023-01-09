from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from apps.core.models import Category, Customer, FoodCard, Order
from common.view import TitleMixin

# Create your views here.


class BaseView(TitleMixin, TemplateView):
    template_name = 'test.html'
    title = 'Store'


class ProductListView(TitleMixin, ListView):
    model = FoodCard
    template_name = 'index.html'
    title = 'Store'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data()
        categories = cache.get('category')
        if not categories:
            context['category'] = Category.objects.all()
            cache.set('category', context['category'], 30)
        else:
            context['category'] = categories
        return context


def product(request, id):
    foodcard = FoodCard.objects.get(id=id)
    one_type_categories = FoodCard.objects.all().filter(category=foodcard.category)
    return render(request, 'product.html', {'foodcard': foodcard, 'one_type_categories': one_type_categories})


def addCart(request, pk):
    cart_session = request.session.get('cart_session', [])
    cart_session.append(pk)
    request.session['cart_session'] = cart_session
    return redirect('base')

# def base(request):
#     categories = Category.objects.all()
#     foodCards = FoodCard.objects.all()
#     context = {'foodCards':foodCards, 'categories':categories}
#     return render(request, 'index.html', context=context)


# def cart(request):
#     cart_session = request.session.get('cart_session', [])
#     count_of_product = len(cart_session)
#     product_Cart = FoodCard.objects.filter(id__in=cart_session)

#     all_products_sum = 0
#     for i in product_Cart:
#         i.count = cart_session.count(i.id)
#         count_of_product += i.count
#         i.sum = cart_session.count(i.id) * i.price
#     return render(request, "cart.html", {'product_Cart':product_Cart, 'all_products_sum':all_products_sum, 'count_of_product':count_of_product})


@login_required
def cart(request):
    cart_session = request.session.get('cart_session', [])
    count_of_product = len(cart_session)
    products_cart = FoodCard.objects.filter(id__in=cart_session)

    all_products_sum = 0
    for i in products_cart:
        i.count = cart_session.count(i.id)
        i.sum = i.count * i.price
        all_products_sum += i.sum

    return render(request, 'cart.html', {'products': products_cart,
                                         'count_of_product': count_of_product,
                                         'all_products_sum': all_products_sum})


@login_required
def removeCart(request, id):
    cart_session = request.session.get('cart_session', [])
    carts = []
    for pk in cart_session:
        if pk != id:
            carts.append(pk)
    request.session['cart_session'] = carts
    return redirect('cart')


def aboutUs(request):
    return render(request, 'about.html')


def search(request):
    if request.method == 'POST':
        searched_product = request.POST.get('search').title()
        # product = FoodCard.objects.get(name = searched_product)
        product = FoodCard.objects.filter(name__contains=searched_product)
        return render(request, 'search.html', {'searched_product': searched_product, 'product': product})


# def signUp(request):
#     if request.method == 'POST':
#         user = UserCreationForm(request.POST  )
#         if user.is_valid():
#             user.save()
#             return redirect('base')
#     else:
#         user = UserCreationForm()

#     return render(request, 'auth.html', {'user':user})


# def signin(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request , username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('base')
#     else:
#         form = AuthenticationForm()

#     return render(request, 'auth.html', {'user':form})

# def signout(request):
#     logout(request)
#     return redirect('base')


def order(request):
    if request.method == 'POST':
        cart_session = request.session.get('cart_session', [])
        if len(cart_session) == 0:
            messages.error(request, 'Ваша корзина пустая', extra_tags='danger')
            return redirect('cart')
        else:
            customer = Customer()
            customer.name = request.POST.get('c_name')
            customer.last_name = request.POST.get('c_lastname')
            customer.number = request.POST.get('c_number')
            customer.addres = request.POST.get('c_addres')
            customer.message = request.POST.get('c_message')
            customer.save()
            for i in range(len(cart_session)):
                order = Order()
                order.product = FoodCard.objects.get(id=cart_session[i])
                order.customer = customer
                order.price = order.product.price
                order.phone = customer.number
                order.addres = customer.addres
                order.save()

            request.session['cart_session'] = []
            messages.error(request, 'Заказ успешно отправлено!', extra_tags='success')
            return redirect('cart')
