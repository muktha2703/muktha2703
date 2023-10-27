from django.contrib import admin
from transactions.models import Transaction,Creditcard
# Register your models here.
class CreditcardAdmin(admin.ModelAdmin):
    list_display=['name','number','year','card_type']
admin.site.register(Transaction)
admin.site.register(Creditcard,CreditcardAdmin)