from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Категория')

    def __str__(self):
        return self.title

# Create your models here.


class FoodCard(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название еды')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    image = models.ImageField(upload_to='core', verbose_name='Изображение')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductsCart(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='cart', blank=True, null=True)
    count = models.IntegerField()
    price = models.IntegerField()
    total_price = models.IntegerField()

    class Meta:
        verbose_name_plural = "Product's cart"
        verbose_name = "Product's carts"


class Customer(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    number = models.CharField(max_length=1000)
    addres = models.CharField(max_length=500)
    message = models.TextField()


class Order(models.Model):
    product = models.ForeignKey(FoodCard, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    phone = models.IntegerField()
    addres = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(auto_now_add=True)
