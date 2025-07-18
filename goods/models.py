from django.db import models
from decimal import Decimal


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название', unique=True)
    slug = models.SlugField(unique=True, max_length=200, blank=True, null=True, verbose_name='URL')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Products(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название', unique=True)
    slug = models.SlugField(unique=True, max_length=200, blank=True, null=True, verbose_name='URL')
    desc = models.TextField(default="Скоро тут будет описание ...", blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=Decimal("0.00"), max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=Decimal("0.00"), max_digits=7, decimal_places=2, verbose_name='Скидка %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories,on_delete=models.CASCADE, verbose_name='Категория')


    def __str__(self) -> str:
        return f"{self.name} - Количество {self.quantity}"    
    
    def display_id(self):
        return f"{self.id:05}"
    
    def sell_price(self):
        if self.discount:
            return round (self.price - self.price * self.discount / 100, 2)
        return self.price
    
    
    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ("id",)
