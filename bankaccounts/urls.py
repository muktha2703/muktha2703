from bankaccounts import views
from django.urls import path

app_name='bankaccounts'
urlpatterns=[
    path('',views.kyc_reg),
    path("dashboard/",views.kyc_reg,name='dashboard'),
    path("account/",views.account,name="account"),
    path("dash/",views.dashboard,name='dash'),
]