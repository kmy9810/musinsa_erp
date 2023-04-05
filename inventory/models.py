from django.db import models
from musinsa_user.models import UserModel
from musinsa_erp.models import Product
# Create your models here.


class Inventory(models.Model):
    class Meta:
        db_table = "inventory"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)  # 다른 모델에서 찾조
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # 상품 외래키
    inventory_date = models.CharField(max_length=20)
    increased_inventory = models.IntegerField(null=False)