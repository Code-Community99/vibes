from django.db import models
from signup.models import signup
# Create your models here.

class Followers(models.Model):
    id = models.AutoField(primary_key = True)
    user_follower = models.ForeignKey(signup , related_name = "followercounter" ,  on_delete = models.CASCADE)
    user_following = models.ForeignKey(signup , related_name = "followingcounter" , on_delete = models.CASCADE)

    class Meta:
        db_table = "Followers"
