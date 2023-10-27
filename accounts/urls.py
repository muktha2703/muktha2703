from accounts import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
   path("",views.sign_up,name="register"),
   path("signin/",views.sign_in,name="signin"),
   path("dashboard/",views.dashboard,name="dashboard"),
   path('logout/',views.userlogout,name='logout'),
   # path("index/",views.accounts,name='index')
]