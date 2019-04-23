from .models import *
from django import forms


from django import forms
from .models import *

#
# class SubscriberForm(forms.ModelForm):
#
#     class Meta:
#         model = Subscriber
#         exclude = [""]

# class Tovar_Form(forms.ModelForm): # форма заполнения полей объекта. Как в админке, только на страницу
#
#
#     class Meta:
#         model = Addtovar_new
#         fields = [""]    # поля, которые хочешь включить
#         exclude = [""]   # поля, которые хочешь отключить, можно и в админке


# в хтмл файле ставь csr-токен возле > формы