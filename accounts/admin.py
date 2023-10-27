from django.contrib import admin
from accounts.models import user_profile
from transactions.models import Transaction


# Register your models here.
admin.site.register(user_profile)
admin.site.register