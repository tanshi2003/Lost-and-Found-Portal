from django.db import models
class service(models.Model):
    service_icon=models.CharField(max_length=50)
    service_title=models.CharField(max_length=50)
    service_des=models.TextField()
class Meta:
        app_label = 'authentication'
# Create your models here.
