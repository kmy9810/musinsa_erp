# tweet/models.py
from django.db import models
from musinsa_user.models import UserModel


class Product(models.Model):
    class Meta:
        db_table = "product"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)  # 다른 모델에서 찾조
    categorys = (
        ('h', '후드티'),
        ('j', '청바지'),
    )
    category = models.CharField(choices=categorys, max_length=1)
    code = models.CharField(max_length=20, null=False)
    name = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=256, default='')
    price = models.IntegerField(null=False)
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    size = models.CharField(choices=sizes, max_length=1)


def __str__(self):
    return self.code


