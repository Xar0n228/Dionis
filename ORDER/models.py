from django.db import models
from PIL import ImageFile
from django.utils.safestring import mark_safe

from django.db import models
from TOWARS.models import Towar

from django.db.models.signals import post_save



from django.contrib.auth.models import User

# Create your models here.

# класс пользователя, которому надо регистироваться. К нему привязаны заказы.

class OrderStatus(models.Model):
    TYPES_CHOISES = (
        ('yes', 'Оплачен'),
        ('dolg', 'Долг'),
        ('not', 'Не оплачен'),
    )
    myStatus = models.CharField(max_length=30, default='Не оплачен', blank=False, choices=TYPES_CHOISES, unique=True)
    def __str__(self):
        return "%s" % self.myStatus

class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    status = models.ForeignKey(OrderStatus, blank=True, null=True, default=None, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return "%s" % self.status

    class Meta:
        verbose_name = 'Заказ:'
        verbose_name_plural = 'Заказы:'

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)

class TowarOrderModel(models.Model):
    session_key = models.CharField(max_length=128, default=None, blank=True, null=True)
    count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    one_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    all_price = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)

    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, default=None)

            ########### или же попробовать через МЕТОД/МЭНЕДЖЕР
    towar = models.ForeignKey(Towar, blank=True, null=True, default=None, on_delete=models.CASCADE,
                              related_name='towars_name', related_query_name='towars_querry')
    def __str__(self):
        return self.id

    class Meta:
        default_related_name = 'back_to_order_towar'
        verbose_name = 'Товар в заказе:'
        verbose_name_plural = 'Товары в заказе:'

    def save(self, *args, **kwargs):
        var_zena = self.towar.zena
        self.one_price = var_zena
        self.all_price = self.count * var_zena
        super(TowarOrderModel, self).save(*args, **kwargs)


########################################################################################################################
# @disable_for_loaddata
# class TowarManager(models.Manager):
#     def for_create(self, t_i):




# def towar_in_order_post_save(sender, instance, created, **kwargs):
#     order = instance.order
#     all_towars_in_order = TowarInOrder.objects.filter(main_order=order, is_active=True)
#     print('3_SAVE_3')
#     order_total_price = 0
#     for item in all_towars_in_order:
#         order_total_price += item.for_all_price
#
#     instance.order.total_price = order_total_price
#     instance.order.save(force_update=True)
#
#
# post_save.connect(towar_in_order_post_save, sender=TowarInOrder)

########################################################################################################################

## class TowarInOrder(models.Model):
#     session_key = models.CharField(max_length=128, default=None, blank=True, null=True)
#     count = models.IntegerField(default=0)
#     for_one_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     for_all_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, default=None)
#
#     is_active = models.BooleanField(default=True)
#     is_delete = models.BooleanField(default=False)
#     total_wes = models.IntegerField(default=0)
#
#     towar = models.ForeignKey(Towar, null=False, default=None, on_delete=models.CASCADE)
#     def __str__(self):
#         return "%s" % self.id
#
#     def save(self, *args, **kwargs):
#         # my_tov = self.order_new.objects.get_or_create(id=self.id)
#         # добавим сохранение инфы по цене и по количеству
#         # self.refresh_from_db()
#         print('SAVE')
#         # my_tov = self.order_new.
#         # my_tov =
#         # my_tov = self.order_new.save()
#         #
#         # print(my_tov.zena)
#
#         print(self.session_key)
#         print(self.for_one_price)
#         print(self.count)
#         self.towar = Towar.objects.filter(pk=self.towar_id)
#
#         for_one_pr = self.towar.zena
#         self.for_one_price = for_one_pr
#         self.for_all_price = self.count * for_one_pr
#         print('2_SAVE_2')
#         super(TowarInOrder, self).save(*args, **kwargs)
#
#
#     class Meta:
#         verbose_name = 'Товар в заказе:'
#         verbose_name_plural = 'Товары в заказе:'
