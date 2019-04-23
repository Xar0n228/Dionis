from django.contrib import admin
from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static


# from PAGE import views
from ORDER import views
from PAGE.models import *
from PAGE.views import front_page

app_name = 'orders_name'

urlpatterns = [
    # path('admin/', admin.site.urls),
    # re_path(r'^category/(?P<category_id>\w+)$', views.categor,  name='cat'),
    # path('', include('PAGE.urls')),
    re_path(r'^add_to_order/$', views.add_to_order, name='add_to_order'),
    re_path(r'^orders/$', views.checkout, name='basket_checkout')
]\
                + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
                + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
