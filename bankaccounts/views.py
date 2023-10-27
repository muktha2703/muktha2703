from django.shortcuts import render
from bankaccounts.forms import KYC_form
from bankaccounts.models import Account
from bankaccounts.models import KYC
from transactions.models import Transaction,Creditcard
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from transactions.forms import Credit_card_form

# Create your views here.
def kyc_reg(request):
    user =request.user
    account=Account.objects.get(user=user)
    try:
        kyc=KYC.objects.get(user=user)
    except:
        kyc=None

    if request.method == "POST":
        form = KYC_form(request.POST,request.FILES,instance=kyc)
        if form.is_valid():
             new_form=form.save(commit=False)
             new_form.user=user
             new_form.account=account
             new_form.save()
             messages.success(request,'KYC form submitted successfully, In review now.')
             return redirect('accounts:dashboard')    
    else:
        form = KYC_form(instance=kyc)
    context={
        'account':account,
        'form':form,
        'kyc':kyc
    }
    return render(request,"account/kyc_form.html",context)
    # form=KYC_form()
    # return render(request,'kyc_form.html',{'form':form})
 

@login_required(login_url='singin')
def account(request):
    kyc=KYC.objects.get(user=request.user)
    account=Account.objects.get(user=request.user)
    
    context={
        'kyc':kyc,
        'account':account
    }
    return render(request,'account/account.html',context)

def dashboard(request):
    user=request.user
    account=Account.objects.get(user=request.user)
    kyc=KYC.objects.get(user=request.user)
    transaction=Transaction.objects.all()
    creditcard_detail=Creditcard.objects.all()
    if request.method=='POST':
        form=Credit_card_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=Credit_card_form        

    context={
        'user':user,
        'account':account,
        'kyc':kyc,
        'transaction':transaction,
        'form':form,
        'creditcard_detail':creditcard_detail
    }  

    return render(request,'account/dashboard.html',context)
