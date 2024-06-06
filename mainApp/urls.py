from django.urls import path,re_path

from .views import *

app_name = 'mainApp'

urlpatterns = [
    #English
    path('', HomePageEnView.as_view(), name='homeEn'),
    re_path('emailSend/', emailSend, name='emailSend'),
    re_path('verifyCode/', verifyCode, name='verifyCode'),
    ################

]