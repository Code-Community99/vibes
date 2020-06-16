from django.db import models
from signup.models import signup
# Create your models here.



class Groups(models.Model):
    id = models.AutoField(primary_key = True , serialize = True)
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

class Group_content(models.Model):
    postuid = models.AutoField(primary_key = True , serialize = True)
    poster = models. ForeignKey(signup , related_name = "group_content_bridge" , on_delete = models.CASCADE)
    group_post_own = models.ForeignKey(Groups , related_name = "post_group_own" , on_delete = models.CASCADE)
    post_content = models.CharField(max_length = 1024)
    post_time = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = "group_content"
