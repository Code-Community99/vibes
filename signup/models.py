from django.db import models

# Create your models here.
class signup(models.Model):
    uid = models.AutoField(primary_key=True , serialize = True)
    email = models.EmailField(max_length = 60 , unique = True)
    username = models.CharField(max_length = 30 , unique = True)
    location = models.CharField(max_length = 30 , null=True)
    hobby = models.CharField(max_length = 30)
    profilepic = models.ImageField()
    password = models.CharField(max_length = 255)

    class Meta:
        db_table = "signup"
