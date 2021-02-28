from django.conf.urls import url
from . import api

urlpatterns = [

    url(r'^sms/', api.send_sms),
    url(r'^login/', api.login),

]