from django.urls import path


from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('shop/', shop, name='shop'),
    path('category/<slug:category_slug>/', products_by_category, name='products_by_category'),
    path('sale/<slug:sale_slug>/', products_by_sale, name='products_by_sale'),
    path('gender/<slug:gender_slug>/', products_by_gender, name='products_by_gender'),
    path('brand/<slug:brand_slug>/', products_by_brand, name='products_by_brand'),
    path('ordered-name/', products_by_name, name='products_by_name'),
    path('ordered-price/', products_by_price, name='products_by_price'),
    path('contact/', contact, name='contact'),
    path('detail/<slug:product_slug>/', detail, name='detail'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
    path('cart/', cart, name='cart'),
    path('to-cart/<int:product_id>/<str:action>', to_cart, name='to_cart'),
    path('save-review/<slug:product_slug>/', save_review, name='save_review'),
    path('payment/', create_checkout_sessions, name='payment'),
    path('success-payment/', success_payment, name='success_payment'),

]
