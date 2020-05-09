from django.db import models
from signup.models import signup
# Create your models here.


class MsgContent(models.Model):
    msgId = models.AutoField(primary_key = True)
    message = models.CharField(max_length = 500)
    postTime = models.DateTimeField(auto_now_add = True)
    suid = models.ForeignKey(signup , related_name = "senderuid", on_delete = models.CASCADE)
    ruid = models.ForeignKey(signup , on_delete = models.CASCADE)
    readStatus=models.BooleanField(default = False)


    class Meta:
        db_table = "messaging"
