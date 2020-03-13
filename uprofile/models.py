from django.db import models
from signup.models import signup
# Create your models here.



class events(models.Model):
    eid = models.AutoField(primary_key = True)
    usereventid = models.ForeignKey(signup , related_name = "events" , on_delete = models.CASCADE)
    event_name = models.CharField(max_length = 50)
    event_description = models.TextField(max_length = 200)
    post_time = models.TimeField(auto_now_add = True)
    event_brief_pic = models.FileField()

    class Meta:
        db_table = "events"
