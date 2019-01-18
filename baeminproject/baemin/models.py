from django.db import models
from django.conf import settings


class Shop(models.Model):
    name = models.CharField(max_length=100)                 # 이름
    tel = models.CharField(max_length=20)                   # 전화번호
    addr = models.CharField(max_length=100)                 # 주소

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name

class Item(models.Model):
    shop = models.ForeignKey(Shop, on_delete = models.CASCADE)                 # 가게
    name = models.CharField(max_length=100)                 # 이름
    price = models.PositiveIntegerField()                # 가격

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name

class Order(models.Model):
    shop = models.ForeignKey(Shop , on_delete = models.CASCADE)                 # 가게
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete = models.CASCADE)                 # 주문한 유저
    item_set = models.ManyToManyField(Item)             # 주문한 상품 목록 (Hint: ManyToManyField)
    created_at = models.DateTimeField(auto_now_add=True)           # 생성일시

    class Meta:
        ordering = ('-id',)

    @property
    def total(self):
        return sum(item.price for item in self.item_set.all())
