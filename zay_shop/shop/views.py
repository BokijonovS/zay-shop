from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm, ReviewForm
from .models import Category, Product, Gender, Sale, Brand
from .utils import CartAuthenticatedUser


# Create your views here.


def index(request):
    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.order_by('-quantity')[:3],
        'brands': Brand.objects.all(),
    }
    return render(request, 'shop/index.html', context)


def about(request):
    brands = Brand.objects.all()
    return render(request, 'shop/about.html', {'brands': brands})


def shop(request):
    context = {
        'products': Product.objects.order_by('-pk'),
        'categories': Category.objects.all(),
        'genders': Gender.objects.all(),
        'sales': Sale.objects.all(),
        'brands': Brand.objects.all(),
    }
    return render(request, 'shop/shop.html', context)


def products_by_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.filter(category=category),
        'genders': Gender.objects.all(),
        'sales': Sale.objects.all(),
        'brands': Brand.objects.all(),
    }
    return render(request, 'shop/shop.html', context)


def products_by_sale(request, sale_slug):
    sale = Sale.objects.get(slug=sale_slug)
    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.filter(sale=sale),
        'genders': Gender.objects.all(),
        'sales': Sale.objects.all(),
        'brands': Brand.objects.all(),
    }
    return render(request, 'shop/shop.html', context)


def products_by_gender(request, gender_slug):
    gender = Gender.objects.get(slug=gender_slug)
    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.filter(gender=gender),
        'genders': Gender.objects.all(),
        'sales': Sale.objects.all(),
        'brands': Brand.objects.all(),
    }
    return render(request, 'shop/shop.html', context)


def products_by_name(request):
    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.order_by('name'),
        'genders': Gender.objects.all(),
        'sales': Sale.objects.all(),
        'brands': Brand.objects.all(),
    }
    return render(request, 'shop/shop.html', context)


def products_by_price(request):
    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.order_by('-price'),
        'genders': Gender.objects.all(),
        'sales': Sale.objects.all(),
        'brands': Brand.objects.all(),
    }
    return render(request, 'shop/shop.html', context)


def products_by_brand(request, brand_slug):
    brands = Brand.objects.exclude(slug=None)
    brand = brands.get(slug=brand_slug)
    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.filter(brand=brand),
        'genders': Gender.objects.all(),
        'sales': Sale.objects.all(),
        'brands': Brand.objects.all(),
    }
    return render(request, 'shop/shop.html', context)


def contact(request):
    return render(request, 'shop/contact.html')


def detail(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    cart_info = CartAuthenticatedUser(request).get_cart_info()
    context = {
        'order_products': cart_info['order_products'],
        'cart_total_price': cart_info['cart_total_price'],
        'product': product,
    }
    return render(request, 'shop/detail.html', context)



def user_register(request):
    form = RegisterForm(data=request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('index')

    form = RegisterForm()
    context = {
        'form': form,
        'title': 'Register'
    }
    return render(request, 'shop/register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')

    form = LoginForm()
    return render(request, 'shop/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('index')


def cart(request):
    if request.user.is_authenticated:
        cart_info = CartAuthenticatedUser(request).get_cart_info()
        context = {
            'order_products': cart_info['order_products'],
            'cart_total_price': cart_info['cart_total_price'],
            'page_name': 'Cart',
        }
        return render(request, 'shop/cart.html', context)
    else:
        return redirect('login')


def to_cart(request, product_id, action):
    if request.user.is_authenticated:
        CartAuthenticatedUser(request, product_id, action)
        page = request.META.get('HTTP_REFERER')
        return redirect(page)
    else:
        return redirect('login')


def save_review(request, product_slug):
    form = ReviewForm(data=request.POST)
    if request.user.is_authenticated:
        if form.is_valid():
            product = Product.objects.get(slug=product_slug)
            review = form.save(commit=False)
            review.product = product
            review.author = request.user
            review.save()
        return redirect('detail', slug=product_slug)
    else:
        return redirect('login')
