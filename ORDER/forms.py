from django import forms
from .models import *


# class CheckoutContactForm(forms.Form):
#     name = forms.CharField(required=True)
#     phone = forms.CharField(required=True)


class CheckoutContactForm(forms.Form):
    # форма для использования в форме отправки инфы. Передаётся в шаблон HTML через views
    # Поля передачи пишутся здесь:
    name = forms.CharField(required=True)
    # required=True Пишем, что это поле нам нужно
    phone = forms.CharField(required=True)
    # class Meta: Т.К не относиться ни к какой модели
    #     model = Subscriber
    #     exclude = [""]
