from django.shortcuts import render

from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, Http404

from django.views import View
from django.views.generic.base import TemplateView
# from PAGE.forms import Data_Form
from PAGE.models import A_D
from TOWARS.models import Towar
# from .models import *
from .forms import CheckoutContactForm
from django.contrib.auth.models import User
# Create your views here.


from ORDER.models import TowarOrderModel, Order
#
# from ORDER.context_processor import getting_order_info

#
#
def add_to_order(request):
    dict_for_return = dict()
    session_key = request.session.session_key
    if not session_key:
        request.session["session_key"] = 123
        request.session.cycle_key()  # вручную создаёт ключ сессии
    for_data = request.POST
    t_i = for_data.get("towar_id")
    number = int(for_data.get("number"))
    print(number)
    is_delete = for_data.get("is_delete")
###############################################################ТИПО СНАЧАЛА СОЗДАЁМ
    print('FDFDSF')
    print(t_i)
    tow = Towar.objects.get(id__exact=t_i)
    tow.save()
###############################################################ТИПО СНАЧАЛА СОЗДАЁМ
    viewTowarOrder, created = TowarOrderModel.objects.get_or_create(session_key=session_key, is_active=True, towar=tow, count=number)
    if not created:
        print("NOT CRE")
        viewTowarOrder.count += int(number)
        viewTowarOrder.save(force_update=True)
#??????????????????????????????????????????????????????????????????????????????????
    viewTowarOrder.refresh_from_db()
# ??????????????????????????????????????????????????????????????????????????????????
    print(viewTowarOrder.towar.zena)
    allTowarOrder = TowarOrderModel.objects.filter(session_key=session_key, is_active=True)
    totalOrderPrice = 0
    totalOrderCount = allTowarOrder.count()
    for tow_ord in allTowarOrder:
        totalOrderPrice += tow_ord.all_price
    dict_for_return["total_number"] = totalOrderCount
    dict_for_return["towars"] = list()
    for tows in allTowarOrder:
        var_dict = dict()
        var_dict["id"] = tows.id
        var_dict["name"] = tows.towar.name
        var_dict["single_price"] = tows.one_price
        var_dict["amount"] = tows.count
        dict_for_return["towars"].append(var_dict)



    return JsonResponse(dict_for_return)

    #     # viewTowarOrder.refresh_from_db()
    # viewTowarOrder.save(force_update=True)
    # print(viewTowarOrder.towar_id)
    # ##################################
    # # через add, через внутренний метод/мэнеджер
    # ##################################
    #
    # allTowOrd = TowarInOrder.objects.filter(session_key=session_key, is_active=True)
    # allTowOrdAmount = allTowOrd.count()
    # totalPrice = 0
    # for tows in allTowOrd:
    #     totalPrice += tows.for_one_price
    #     # много способов посчитать общую цену
    # dict_for_return["total_number"] = allTowOrdAmount
    # dict_for_return["towars"] = list()
    # for tows in allTowOrd:
    #     var_dict = dict()
    #     var_dict["id"] = tows.id
    #     var_dict["name"] = tows.towar.name
    #     var_dict["single_price"] = tows.for_one_price
    #     var_dict["amount"] = tows.count
    #     dict_for_return["towars"].append(var_dict)


#     if is_delete == 'true':
#         print("IF")
#         # TowarInOrder.order_new.veryimp.filter(id=towar_id)
#         TowarInOrder.objects.filter(id=towar_id).update(is_active=False)
#             # форсит обновление. То есть заменяет данные is_active на False
#     else:
#         print("ELSE")
#         new_towar, created = TowarInOrder.objects.get_or_create(session_key=session_key, towar_id=towar_id, is_active=True, defaults={"count": number})
#             # возвращает (новый товар, который создаётся ; флаг, был ли он создан, или же нет)
#             # get_or_create ищет по полям запись. И если этой записи не будет, то она будет использовать поля defaults, чтобы создать новую запись
#         print("ELSE 2")
#         if not created:
#             print("FUCK THEM ALL")
#             new_towar.count += int(number)
#             new_towar.save(force_update=True)
#                 # форсим сохранение
# # код на оба случая
#     towars_in_order = TowarInOrder.objects.filter(session_key=session_key, is_active=True)
#     towars_total_nmb = towars_in_order.count()
#         # QUERRY-SET, который можно обойти в for
#         # towars_total_nmb = towars_in_order.count()
#     for_total_price = 0
#     for t_p in towars_in_order:
#         for_total_price += t_p.for_one_price
#     dict_for_return["towars_total_nmb"] = towars_total_nmb
#
#     dict_for_return["towars"] = list()
#
#     for item in towars_in_order:
#         # делаем словарь, в который заносим данные по нашим товарам
#         towar_dict = dict()
#         towar_dict["id"] = item.id
#         towar_dict["name"] = item.order_new.name
#         towar_dict["for_one_price"] = item.for_one_price
#         towar_dict["number"] = item.count
#         # создаём словарь и добавляем его к "list", чтобы потом передать в JS-файл и обрабатывать
#         dict_for_return["towars"].append(towar_dict)


        #  такой тип ответа одаёт в нужном формате те данные, которые нам нужны.


def checkout(request):
    session_key = request.session.session_key
        # берём из request
    towars_in_order = TowarOrderModel.objects.filter(session_key=session_key, is_active=True)
    for item in towars_in_order:
        print(item.order)


    # form = CheckoutContactForm(request.POST or None)                              !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # заготовленная форма для расширения возможностей передачи инфы с формы
        # на самом шаблоне HTML имя поля будет писаться как "form"
    # if request.POST:
    #     print(request.POST)
    #         #
    #     if form.is_valid():
    #         # проверяем, проходит ли эта форма валидацию. То есть правильный ли в ней ввод
    #         print("yes")
    #         data = request.POST
    #             # переменная инфы из формы в режиме post
    #         name = data.get("name", "3423453")
    #             # если писать так, как выше, то в случае, если поля не будет, то будет возвращать второе значение.
    #             # По умолчанию None
    #         phone = data["phone"]
    #             # если писать вот так, как выше, то в случае, если этого поля не будет, то появится ошибка
    #         user, created = User.objects.get_or_create(username=phone, defaults={"first_name": name})
    #             # считываем с формы Usera
    #
    #         order = Order.objects.create(user=user, customer_name=name, customer_phone=phone, status_myStatus="not")
    #         # ХОТЯ ВООБЩЕ, мы бы могли просто считывать все данные с модели через request из модели TowarInOrder
    #         # или же на странице корзини добавлять AJAX, чтобы сохранять количество.
    #         for name, value in data.items():
    #             # items() - функция для обхода словаря
    #             if name.startswith(" towars_in_order_"):
    #                 # проверяет, начинается ли название элемента с "_._"
    #                 # поскольку у всех атрибутов одинаковое начало
    #                 towar_in_order_id = name.split("towars_in_order_")[1]
    #                     # разбиваем текст itema
    #                 towar_in_order = TowarOrderModel.objects.get(id=towar_in_order_id)
    #                 print(type(value))
    #                 # ВАЖНО!!!!!!!!!!!!!! Здесь как раз видно, зачем разделили продукты в корзине и в заказе
    #                 towar_in_order.nmb = value
    #                 towar_in_order.main_order = order
    #                 towar_in_order.save(force_update=True)
    #
    #                 TowarOrderModel.objects.create(order_new=towar_in_order.order_new, count=towar_in_order.count,
    #                                               for_one_price=towar_in_order.for_one_price,
    #                                               for_all_price=towar_in_order.for_all_price,
    #                                               main_order=order)
    #
    #         return HttpResponseRedirect(request.META['HTTP_REFERER'])
    #     else:
    #         print("no")
    admin_data = A_D.objects.get(version=1)
    admin_data.cont_menu = False
    admin_data.main_path = 'basket.html'
    context = {'admin_data': admin_data}
    return render(request, 'base.html', locals())













