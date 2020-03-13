from django.db import models
from signup.models import signup
# Create your models here.


class sell_goods(models.Model):
    GoodId = models.AutoField(primary_key = True)
    Gtitle = models.CharField(max_length = 255 )
    GDescription = models.CharField(max_length = 255)
    GLocation = models.CharField(max_length = 255 , default = "Narobi/Kenya")
    Gprice = models.FloatField(max_length = 10)
    Gphoto = models.FileField()
    Sid = models.ForeignKey(signup , related_name = "seller_id" , on_delete = models.CASCADE)

    class Meta:
        db_table = "Goods"
