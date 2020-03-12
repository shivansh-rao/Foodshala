from django.db import models
from django.db.models import Manager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rest = models.CharField(max_length=20,default='m',editable=True)

    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

    

class fooditem(models.Model):
    
    food=models.CharField(max_length=100)
    image=models.ImageField(upload_to='pics')
    item=models.CharField(max_length=100)
    restaurent= models.CharField(max_length=100)
    price=models.IntegerField()


class order(models.Model):
    cust=models.IntegerField()
    food=models.IntegerField()
    
    

