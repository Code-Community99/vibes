from django.db import models
from signup.models import signup
# Create your models here.


class notif(models.Model):
    id = models.AutoField(primary_key = True)
    source = models.ForeignKey(signup , on_delete = models.CASCADE , related_name = "source")
    destination = models.ForeignKey(signup , on_delete = models.CASCADE , related_name = "destination")
    message = models.CharField(max_length = 70)
    notiftime = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = "notifications"
