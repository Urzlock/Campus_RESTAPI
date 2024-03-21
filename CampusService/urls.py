from CampusService import views 
from django.urls import path, re_path, include
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from rest_framework import routers


router = routers.DefaultRouter()
router.register('carreras',views.CampusView,'campus')

urlpatterns = [
    # path('campus-REST/', CampusViews.campus_list, name='campus'),
    # path('campus-REST/<int:pk>', CampusViews.campus_detail,name='campus_detail'),
    path('api/campus/',include(router.urls))
]