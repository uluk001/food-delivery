# Generated by Django 4.0.1 on 2022-02-21 11:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('number', models.CharField(max_length=1000)),
                ('addres', models.CharField(max_length=500)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FoodCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название еды')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('image', models.ImageField(upload_to='core', verbose_name='Изображение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='cart')),
                ('count', models.IntegerField()),
                ('price', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': "Product's carts",
                'verbose_name_plural': "Product's cart",
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('addres', models.CharField(max_length=100, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.foodcard')),
            ],
        ),
    ]