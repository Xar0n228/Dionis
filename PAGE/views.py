from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, Http404


from TOWARS.models import Towar
from PAGE.models import A_D


def front_page(request):
    try:
        adm_data = A_D.objects.get(version=1)
        adm_data.cont_menu = True
        adm_data.main_path = 'landing_main.html'
        context = {'admin_data': adm_data}
    except all:
        raise Http404("Упс")
    return render(request, 'base.html', context)

#
# def register(request):
#     name = "CodingMedved"
#     current_day = "03.01.2017"
#     form = SubscriberForm(request.POST or None)
#
#     if request.method == "POST" and form.is_valid():
#         print (request.POST)
#         print (form.cleaned_data)
#         data  = form.cleaned_data
#         print (data["name"])
#
#         new_form = form.save()
#
#     return render(request, 'register.html', locals())
def page_for_menu(request, for_page_type):
    # f_p = str(for_page_type)
    f_p = for_page_type
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()  # Вручную создаёт сессию
        print(request.session.session_key)
    admin_data = A_D.objects.get(version=1)
    # product = list(Tovar.objects.filter(status__mStatus='ready', category_new__category_key=f_p, is_active=True))
    product = Towar.objects.filter(status__mStatus='ready', category_new__category_key=f_p, is_active=True)
    admin_data.cont_menu = False
    admin_data.main_path = 'base_menus.html'
    context = {'admin_data': admin_data, 'page_data': product}
    return render(request, 'base.html', context)

# def pizza_page(request):
#     try:
#         adm_data = A_D.objects.get(version=1)
#         product = Category_new.objects.filter(category_key='pizza')
#         adm_data.cont_menu = False
#         adm_data.main_path = 'HTML_MAIN_PAGE/pizza_menu_p.html'
#         context = {'admin_data': adm_data, 'page_data': product}
#     except all:
#         raise Http404("Упс")
#     return render(request, 'base.html', context)
#
# def sushi_page(request):
#     try:
#         adm_data = A_D.objects.get(version=1)
#         product = Category_new.objects.filter(category_key='sushi')
#         adm_data.cont_menu = False
#         adm_data.main_path = 'HTML_MAIN_PAGE/sushi_menu_p.html'
#         context = {'admin_data': adm_data, 'page_data': product}
#     except all:
#         raise Http404("Упс")
#     return render(request, 'base.html', context)
#
# def burger_page(request):
#     try:
#         adm_data = A_D.objects.get(version=1)
#         product = Category_new.objects.filter(category_key='burger')
#         adm_data.cont_menu = False
#         adm_data.main_path = 'HTML_MAIN_PAGE/burger_menu_p.html'
#         context = {'admin_data': adm_data, 'page_data': product}
#     except all:
#         raise Http404("Упс")
#     return render(request, 'base.html', context)
#
# def drink_page(request):
#     try:
#         adm_data = A_D.objects.get(version=1)
#         product = Category_new.objects.filter(category_key='drink')
#         adm_data.cont_menu = False
#         adm_data.main_path = 'HTML_MAIN_PAGE/drink_menu_p.html'
#         context = {'admin_data': adm_data, 'page_data': product}
#     except all:
#         raise Http404("Упс")
#     return render(request, 'base.html', context)
#
# def alcohol_page(request):
#     try:
#         adm_data = A_D.objects.get(version=1)
#         product = Category_new.objects.filter(category_key='alcohol')
#         adm_data.cont_menu = False
#         adm_data.main_path = 'HTML_MAIN_PAGE/alcohol_menu_p.html'
#         context = {'admin_data': adm_data, 'page_data': product}
#     except all:
#         raise Http404("Упс")
#     return render(request, 'base.html', context)

# def categor(request, category_id):
#
#     prod = Category.objects.get(id=category_id)
#
#     session_key = request.session.session_key
#     if not session_key:
#         request.session.cycle_key()
#     print(request.session.session_key)
#     return render(request)
# #
# def pizza_menu_(request):
#     form = Pizza_Form(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         print(request.POST)
#         print(form.cleaned_data)
#         data = form.cleaned_data
#         print(data["name"])
#
#         new_form = form.save()
#
#     return render(request, 'base.html', locals())
