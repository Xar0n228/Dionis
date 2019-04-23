from django.contrib import admin
from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static


from TOWARS import views
from TOWARS.models import *

app_name = 'towars_name_page'
# admin.autodiscover()


urlpatterns = [
    # path('admin/', admin.site.urls), ##############################

    # path('', include('PAGE.urls')),  ##############################
    re_path(r'^towar_(?P<towar_id>\w+)/$', views.show_towar, name='page_for_tovar')

    # re_path(r'^(?P<category_key>\w+)_menu/$', views.category_url,  name='categ'),
]\
                + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
                + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
