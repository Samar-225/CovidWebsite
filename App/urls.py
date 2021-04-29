from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('base/',views.base,name='base'),
    path('base2/',views.base2,name='base'),
    path('test-centres/',views.testCentres,name='testCentres'),
    path('ambulance/',views.ambulance,name='a'),
    path('helpline/',views.helpLine,name='b'),
    path('ct-scan/',views.ctScan,name='c'),
    path('dashboard/',views.adminPanel,name='ad'),
    path('signup/',views.signup,name='si'),
    path('login/',views.signin,name='log'),
    path('profile/',views.basicprofile,name='pro'),
    path('logout/',views.user_logout,name='logout')
]
