from django.db import models
from PIL import ImageFile
from django.utils.safestring import mark_safe
# from ORDER.models import Order, TowarInOrder
# from ORDER.models import TowarInOrder

class Status(models.Model):
    TYPES_CHOISES = (
        ('ready', 'доступен'),
        ('not_ready', 'недоступен'),
        ('allready', 'В разработке'),
    )
    mStatus = models.CharField(max_length=30, blank=True, null=True, default='ready', choices=TYPES_CHOISES)

    def __str__(self):
        return "%s" % self.mStatus

class Category_new(models.Model):

    TYPES_CHOISES = (
        ('pizza', 'Пицца'),
        ('sushi',  'Суши'),
        ('burger', 'Бургер'),
        ('drink', 'Напиток'),
        ('alcohol', 'Алкоголь')
    )

    category_key = models.CharField(max_length=30, default='pizza', blank=True, null=True, choices=TYPES_CHOISES, unique=True)
    is_active = models.BooleanField(default=True)
    # cat_type = str(category_key)

    def __str__(self):
        return "%s" % self.category_key

    class Meta:
        verbose_name = 'Категория товара:'
        verbose_name_plural = 'Категория товаров:'


class Towar(models.Model):
    category_new = models.ForeignKey(Category_new, blank=True, null=True, default=None, on_delete=models.CASCADE)
    # TYPES_CHOISES = (
    #     ('1', 'Пицца'),
    #     ('2', 'Суши'),
    #     ('3', 'Бургер'),
    #     ('4', 'Напиток'),
    #     ('5', 'Алкоголь')
    # )
    # tovar_key = models.CharField(max_length=30, blank=True, null=True, default='1', choices=TYPES_CHOISES)
    name = models.CharField(max_length=30, blank=True, null=True, default='_')
    # created = models.BooleanField(default=True) #############################
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    zena = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.ForeignKey(Status, blank=True, null=True, default='ready', on_delete=models.CASCADE)
    # Под заказ
    # order = models.ForeignKey(Order_new, blank=True, null=True, default=1, on_delete=models.CASCADE)
    ves = models.IntegerField(default=0)
    description = models.TextField(max_length=300, blank=True, null=True, default=None)
    image = models.ImageField(blank=True, upload_to='media_true/%Y/%m/%d', help_text='150x150px', verbose_name='Ссылка картинки')

    def __str__(self):
        return "%s" % self.id
    # def save(self, *args, **kwargs):
    #     # добавим сохранение инфы по цене и по количеству
    #     print('SAVE')
    #     print(self.order_new.zena)
    #     for_one_pr = self.order_new.zena
    #     self.for_one_price = for_one_pr
    #     self.for_all_price = self.count * for_one_pr
    #     print('2_SAVE_2')
    #     super(TowarInOrder, self).save(*args, **kwargs)
    #
    # def save(self, *args, **kwargs):
    #     # Переопределение метода сохранения
    #     self._____ = self_____....
    #     all_tovars = Tovars.objects.filter(___ = ___, is_active=True)
    #
    #     for item in all_tovars:
    #       ....
    #     super(model, self).save(*args, **kwargs)



    # ВОТ КАК НАДО КАРТИНКУ ЗАГРУЖАТЬ
    def image_img(self):
        if self.image:
            return mark_safe(u'<img src="{0}" id="_litle_img">'.format(self.image.url))
        else:
            return '(Нет изображения)'

    class Meta:
        verbose_name = 'Товар:'
        verbose_name_plural = 'Товары:'
        default_related_name = 'back_to_towar'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True




# ВОТ КАК НАДО КАРТИНКУ ЗАГРУЖАТЬ