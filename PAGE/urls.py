from django.contrib import admin
from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static


from PAGE import views
from PAGE.models import *
from PAGE.views import front_page

app_name = 'page_name'

urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path(r'^home/$', views.front_page, name='page_front'),
    re_path(r'^(?P<for_page_type>\w+)_menu/$', views.page_for_menu, name='page_for_menu'),
    # re_path(r'^register/$', views.register, name='register'),
    # re_path(r'^pizza_menu/$', views.pizza_page,  name='page_pizza'),
    # re_path(r'^sushi_menu/$', views.sushi_page,  name='page_sushi'),
    # re_path(r'^burger_menu/$', views.burger_page,  name='page_burger'),
    # re_path(r'^drink_menu/$', views.drink_page,  name='page_drink'),
    # re_path(r'^alcohol_menu/$', views.alcohol_page,  name='page_alcohol'),
    # re_path(r'^category/(?P<category_id>\w+)$', views.categor,  name='cat'),
]\
                + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
                + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
