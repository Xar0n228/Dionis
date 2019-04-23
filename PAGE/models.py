from django.db import models
from django.db.models import Q
from PIL import ImageFile
# Create your models here.
from django.utils.safestring import mark_safe
# from TOWARS.models import *

class A_D(models.Model):
    version = models.IntegerField(default=1)
    main_title = models.CharField(max_length=64, blank=True, null=True, default="Dionis")
    our_city = models.CharField(max_length=64, blank=True, null=True, default="Львов")
    our_street = models.CharField(max_length=64, blank=True, null=True, default="Шевченко 24")
    our_email = models.EmailField(max_length=64, blank=True, null=True, default="DionisVicinus@gmail.com")
    our_inst = models.CharField(max_length=64, blank=True, null=True, default="D_i0Ni_S")
    our_face = models.CharField(max_length=64, blank=True, null=True, default="DioVici")
    super_action = models.IntegerField(default=0)
    super_title = models.CharField(max_length=64, blank=True, null=True, default="f")
    super_title_price = models.FloatField(default=0.0)
    cont_menu = False
    main_path = 'landing_main.html'
    self_style = 'D:/PYTHON/DIONIS/SERVER/static/css/project.css'
    self_page_tip = 'landing_main'

    def __str__(self):
        return "%s" % self.version

    #####
# class Subscriber(models.Model):
#     email = models.EmailField()
#     name = models.CharField(max_length=128)
#
#     def __str__(self):
#         return "Пользователь %s %s" % (self.name, self.email,)
#
#     class Meta:
#         verbose_name = 'MySubscriber'
#         verbose_name_plural = 'A lot of Subscribers'






from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
