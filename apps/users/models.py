from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

GENDER_CHOICES = (
    ("male","男"),
    ("female","女")
)

class BasicModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now(),verbose_name='添加时间')
    
    class Meta:
        abstract = True

class UserProfile(AbstractUser):
    nick_name = models.CharField(verbose_name='昵称', max_length=50,default='')
    birthday = models.DateField(verbose_name='生日',null=True,blank=True)
    gender= models.CharField(verbose_name='性别',choices=GENDER_CHOICES,max_length=7)
    address = models.CharField(verbose_name='地址', max_length=50,default="")
    mobile = models.CharField(verbose_name='手机',max_length=11,unique=True)
    image = models.ImageField(upload_to='image/%Y/%m', height_field=None, width_field=None, max_length=None,default='default.png')
    
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
        
    def __str__(self):
        if self.nick_name :
            return self.nick_name
        else :
            return self.name
    