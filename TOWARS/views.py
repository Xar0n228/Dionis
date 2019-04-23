from django.shortcuts import render
# from .forms import *
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from django.views import View
from django.views.generic.base import TemplateView
# from PAGE.forms import Data_Form
from PAGE.models import A_D
from TOWARS.models import *



def show_towar(request, towar_id):   # product
    towar_view = Towar.objects.get(id=towar_id)
    admin_data = A_D.objects.get(version=1)
    admin_data.cont_menu = False
    admin_data.main_path = 'towar.html'
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print(request.session.session_key)
    context = {'towar_view': towar_view, 'admin_data': admin_data}

    return render(request, 'base.html', context)

# def category_url(request, cate_k):
#     try:
#
#
#     except all:
#         raise Http404("Упс")
#
#     # form = NameForm(request.POST) - привязать данные к форме
#     # print(request.session.session_key)
#     # print(product.category_key)
#     return render(request, 'HTML_MAIN_PAGE/pizza_menu_p.html', product)
#




    # form = Category_new(request.POST or None)
    # if request.method == 'POST' and form.is_active:  #  в хтмл method="post"
    #     # categ = form.clean_fields()
    #     # print(categ["category_key"])
    #     print(form.status)
    #    # x = form.cleaned_data #  создаёт словарь атрибутов, которые мы получили из формы
    #    # x["____"] # обращение к атрибуту
    # try:
    #     adm_data = A_D.objects.get(version=1)
    #     adm_data.cont_menu = False
    #     adm_data.main_path = 'HTML_MAIN_PAGE/pizza_menu_p.html'
    #     context = {'admin_data': adm_data}
    # except all:
    #     raise Http404("Упс")
    # return render(request, 'base.html', context)

