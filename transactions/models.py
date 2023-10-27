from django.db import models
from shortuuid.django_fields import ShortUUIDField
from bankaccounts.models import Account,User

# Create your models here.
Transaction_status=(
    ['failed','FAILED'],
    ['completed','COMPLETED'],
    ['pending','PENDING'],
    ['processing','PROCESSING'],
    ['request_sent','REQUEST_SENT'],
    ['request_processing','REQUEST_PROCESSING']
)
Transaction_type=(
    ['transfer','TRANSFER'],
    ['withdraw','WITHDRAW'],
    ['refund','REFUND'],
    ['received','RECEIVED'],
    ['request','REQUEST'],
    ['none','NONE']
)
Card_Type=(
    ['master','MASTER'],
    ['visa','VISA'],
    ['rupay','RUPAY'],
    ['platinum','PLATINUM']
)
Card_Status=(
    ['active','ACTIVE'],
    ['inactive','INACTIVE']
)
class Transaction(models.Model):
    transaction_id=ShortUUIDField(unique=True,length=15,max_length=25,prefix="TRN")
    user=models.ForeignKey(User,related_name='user',on_delete=models.CASCADE,null=True)
    amount=models.DecimalField(max_digits=12,decimal_places=2,default=0.00)
    description=models.CharField(max_length=100,null=True,blank=True)
    receiver=models.ForeignKey(User,related_name='receiver',on_delete=models.CASCADE,null=True)
    sender=models.ForeignKey(User,related_name='sender',on_delete=models.CASCADE,null=True)
    receiver_account=models.ForeignKey(Account,related_name='receiver_account',on_delete=models.CASCADE,null=True)
    sender_account=models.ForeignKey(Account,related_name='sender_account',on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=200,choices=Transaction_status,default="pending")
    transaction_type=models.CharField(max_length=200,choices=Transaction_type,default="none")
    date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now_add=False,null=True,blank=True)

    def __str__(self):
        return f"{self.user}"

class Creditcard(models.Model):
    card_id=ShortUUIDField(unique=True,length=10,max_length=20,prefix="CRED",alphabet='0123456789')
    user=models.ForeignKey(User,related_name='users',on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=200)
    number=ShortUUIDField(unique=True,length=16,alphabet='0123456789')
    month=models.CharField(max_length=200)
    year=models.IntegerField()
    cvv=ShortUUIDField(unique=True,length=3,alphabet='0123456789')
    card_type=models.CharField(max_length=200,choices=Card_Type)   
    card_status=models.CharField(max_length=200,choices=Card_Status)     
    dates=models.DateField(auto_now_add=True)
    amount=models.IntegerField()