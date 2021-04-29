from django.db import models
from django.contrib.auth.models import User


# https://github.com/abhijeetekad / samarsinh225@gmail.com

class Hospital(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    phone = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=300,null =True)
    status = models.CharField(max_length=20,null=True)
    beds_with_oxygen = models.IntegerField()
    beds_without_oxygen = models.IntegerField(null=True)
    icu_with_ventilator = models.IntegerField(null=True)
    normal_icu = models.IntegerField()
    total_beds_with_oxygen = models.IntegerField(null=True)
    total_beds_without_oxygen = models.IntegerField(null=True)
    total_icu_with_ventilator = models.IntegerField(null=True)
    total_normal_icu = models.IntegerField(null=True)
    time_update = models.TimeField(null=True)

    def __repl__(self):
        return self.name

class UserProfile(models.Model):
   user = models.OneToOneField(User,on_delete=models.DO_NOTHING)
   phone = models.IntegerField(null=True)
   address = models.CharField(max_length=300,null=True)


   def __str__(self):
       return self.user


