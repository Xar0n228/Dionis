
from .models import TowarOrderModel
    # импортируем модель





#

def getting_order_info(request):
    # получает информацию корзины
    session_key = request.session.session_key
    if not session_key:
        request.session["session_key"] = 123
            # если мы присваиваем ключу сессии хоть какое-то значение, то cycle_key() будет работать исправно
        request.session.cycle_key()

    towars_in_order = TowarOrderModel.objects.filter(session_key=session_key, is_active=True)
    towars_total_nmb = towars_in_order.count()
    # СВОЁ# СВОЁ# СВОЁ# СВОЁ# СВОЁ# СВОЁ
    # for_total_price = towars_in_order.

    return locals()
        # возвращает все переменные, которые есть в функции