from django.db import models


# Create your models here.

class Main(models.Model):
    img = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    # 原表中的id
    trackid = models.IntegerField(default=True)

    class Meta:
        abstract = True


class MainWheel(Main):
    '''
    axf_wheel(img,name,trackid)
    '''

    class Meta:
        db_table = 'axf_wheel'


class MainNav(Main):
    '''
   axf_wheel(img,name,trackid)
   '''

    class Meta:
        db_table = 'axf_nav'


class MainMustBuy(Main):
    '''
   axf_wheel(img,name,trackid)
   '''

    class Meta:
        db_table = 'axf_mustbuy'
