from django.db import models
from django.conf import settings
import uuid

class Threads(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    members=models.ManyToManyField(settings.AUTH_USER_MODEL)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
            ordering=["created_at"]
            db_table='Threads'

class Messages(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    sender=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)
    thread=models.ForeignKey(Threads,on_delete=models.CASCADE)
    content=models.CharField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=["created_at"]
        db_table='Messages'
