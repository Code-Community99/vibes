from django.db import models
from signup.models import signup
# Create your models here.



class Groups(models.Model):
    id = models.AutoField(primary_key = True)
    group_admin = models.ForeignKey(signup ,on_delete = models.CASCADE)
    group_name = models.CharField(max_length = 30)
    group_icon = models.ImageField()
    group_location = models.CharField(max_length = 30)
    group_description = models.CharField(max_length = 255)
    group_create = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = "Groups"

class Members(models.Model):
    group_id = models.ManyToManyField(Groups)
    group_member = models.ForeignKey(signup , on_delete = models.CASCADE)


    class Meta:
        db_table = "Group_members"
