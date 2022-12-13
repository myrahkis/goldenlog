from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timezone import datetime


class Categories(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name="nameCat", help_text="Название категории")
    description = models.TextField(max_length=1000, blank=False, verbose_name="description", help_text="Описание категории")

    class Meta:
        db_table = "Categories"
        verbose_name = "Category"

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(Categories, blank=False, on_delete=models.CASCADE, verbose_name="category",
                                 help_text="ID категории")
    name = models.CharField(max_length=100, blank=False, verbose_name="nameProd", help_text="Название изделия")
    description = models.TextField(max_length=1000, blank=False, verbose_name="description", help_text="Описание изделия")
    cost = models.IntegerField(blank=False, verbose_name="cost", help_text="Цена")
    ownCost = models.IntegerField(blank=False, verbose_name="ownCost", default=0, help_text="Себестоимость")
    weight = models.IntegerField(blank=False, verbose_name="weight", default=0, help_text="Вес")


    class Meta:
        db_table = "Products"
        verbose_name = "Product"

    def __str__(self):
        return self.name + " // " + str(self.category.name)


class CreativeProducts(models.Model):
    category = models.ForeignKey(Categories, blank=False, on_delete=models.CASCADE, verbose_name="category",
                                 help_text="ID категории")
    name = models.CharField(max_length=100, blank=False, verbose_name="nameProd", help_text="Название изделия")

    class Meta:
        db_table = "CreativeProducts"
        verbose_name = "CreativeProduct"

    def __str__(self):
        return self.name + " // " + str(self.category.name)


class Orders(models.Model):
    MONEY = 'MONEY'
    CARD = 'CARD'
    CHOICES_PAY = [
        (MONEY, 'Наличными'),
        (CARD, 'Картой'),
    ]

    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, help_text="ID пользователя")
    products = models.ManyToManyField(Products)
    pay = models.CharField(max_length=5, choices=CHOICES_PAY, default=CARD, help_text="Вид оплаты")
    orderDate = models.DateTimeField(blank=False, default=datetime.now, help_text="Дата заказа")

    class Meta:
        db_table = "Orders"
        verbose_name = "Order"

    def __str__(self):
        return str(self.id)


class CreativeOrders(models.Model):
    PINE = 'PINE'
    SPRUCE = 'SPRUCE'
    ASPEN = 'ASPEN'
    BIRCH = 'BIRCH'
    BEECH = 'BEECH'
    OAK = 'OAK'
    ELM = 'ELM'
    MAPLE = 'MAPLE'
    ASH = 'ASH'
    CHOICES_PROD = [
        (PINE, 'Сосна'),
        (SPRUCE, 'Ель'),
        (ASPEN, 'Осина'),
        (BIRCH, 'Береза'),
        (BEECH, 'Бук'),
        (OAK, 'Дуб'),
        (ELM, 'Вяз'),
        (MAPLE, 'Клен'),
        (ASH, 'Ясень'),
    ]

    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, help_text="ID пользователя")
    email = models.CharField(max_length=30, blank=False, verbose_name="email", help_text="Адрес электронной почты")
    typeOfWood = models.CharField(max_length=6, choices=CHOICES_PROD, default=OAK, help_text="Вид древесины")
    techTask = models.TextField(max_length=1000, blank=False, verbose_name="techTask",
                                help_text="Описание пожеланий к изделию")
    exampleImg = models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name="image", help_text="Чертеж или эскиз")
    orderDate = models.DateTimeField(blank=False, default=timezone.now(), help_text="Дата заказа")

    class Meta:
        db_table = "CreativeOrders"
        verbose_name = "CreativeOrder"

    def __str__(self):
        return str(self.id)













