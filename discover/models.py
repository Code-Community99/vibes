from django.db import models
from signup.models import signup
# Create your models here.

class Followers(models.Model):
    id = models.AutoField(primary_key = True)
    follower = models.ForeignKey(signup ,  on_delete = models.CASCADE)
    following = models.ForeignKey(signup , related_name = "following" , on_delete = models.CASCADE)
    is_following = models.BooleanField(default = False)

    class Meta:
        db_table = "Followers"
