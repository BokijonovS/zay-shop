from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/categories/')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    color = models.CharField(max_length=50)
    specification = models.TextField()
    image = models.ImageField(upload_to='images/products/')
    quantity = models.IntegerField()
    slug = models.SlugField(unique=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    size = models.ForeignKey('Size', on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, null=True)
    gender = models.ForeignKey('Gender', on_delete=models.SET_NULL, null=True, blank=True)
    sale = models.ForeignKey('Sale', on_delete=models.SET_NULL, null=True, blank=True)


class Size(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Sale(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/brands/', null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to='images/products/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    photo = models.ImageField(upload_to='users/', null=True, blank=True)
    phone = models.CharField(max_length=13, verbose_name='Phone number', null=True, blank=True)
    mobile = models.CharField(max_length=13, verbose_name='Mobile', null=True, blank=True)
    email = models.EmailField(max_length=50, verbose_name='Email')
    site = models.URLField(max_length=50, null=True, blank=True)
    job = models.CharField(max_length=50, null=True, blank=True)
    job2 = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)

    class Meta:
        verbose_name = 'Custom user'
        verbose_name_plural = 'Custom users'
        ordering = ['-pk']


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    added = models.DateTimeField(auto_now_add=True, null=True)


    @property
    def get_cart_total_price(self):
        order_products = self.orderproduct_set.all()
        total_price = sum([product.get_total_price for product in order_products])
        return total_price


    @property
    def get_cart_total_quantity(self):
        order_products = self.orderproduct_set.all()
        total_quantity = len(order_products)
        return total_quantity


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    @property
    def get_total_price(self):
        total_price = self.quantity * self.product.price
        return total_price


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=150, null=True)
    email = models.EmailField(max_length=50, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    rating = models.IntegerField(default=0)



