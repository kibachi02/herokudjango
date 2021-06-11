from django.contrib import admin
from django.urls import path
from .views import TopView, ClothingDetail, ClothingRegister, ClothingDelete, ClothingUpdate, ClothingList, signupfunc, loginfunc, logoutfunc, form, forecast


urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
    path('top/', TopView.as_view(), name='top'),
    path('ClothingDetail/<int:pk>', ClothingDetail.as_view(), name='ClothingDetail'),
    path('ClothingRegister/', ClothingRegister.as_view(), name='ClothingRegister'),
    path('ClothingDelete/<int:pk>', ClothingDelete.as_view(), name='ClothingDelete'),
    path('ClothingUpdate/<int:pk>', ClothingUpdate.as_view(), name='ClothingUpdate'),
    path('Clothinglist/', ClothingList.as_view(), name='ClothingList'),
    path('signup/', signupfunc, name='signup'),
    path('', forecast, name='weather'),
    path('form', form, name='form')
]
