"""ems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from equipment.views import equipment_list, equipment_detail, equipment_inc, \
    equipment_detail_download, equipment_detail_upload

urlpatterns = [
    url(r'^$', equipment_list),
    url(r'^zone/(?P<zone_id>\d+)$', equipment_list),
    url(r'^equipment/(?P<equip_id>\d+).html$', equipment_detail),
    url(r'^equipment/inc.html$', equipment_inc),
    url(r'^equipment/download$', equipment_detail_download),
    url(r'^equipment/upload$',equipment_detail_upload),
    url(r'^admin/', admin.site.urls),
]
