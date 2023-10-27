from transactions.models import Creditcard
from django.shortcuts import render,redirect
from bankaccounts.models import Account,KYC


def credit_card_detail(request,number,account_number):
    account=Account.objects.get(account_number=account_number)
    credit=Creditcard.objects.get(number=number)
    context={
        'account':account,
        'credit':credit
    }
    return render(request,'account/creditcard_details.html',context)

def credit_card_bill(request,card_id):
    credit=Creditcard.objects.get(card_id=card_id)
    if request.method=='POST':
        amount_entered=request.POST.get('amount')
        print(amount_entered)
        if credit.user.account.account_balance<=0 or credit.user.account.account_balance<int(amount_entered):
            print("insufficient amount")
        else:
            credit.amount+=int(amount_entered)
            credit.user.account.account_balance-=int(amount_entered)
            print(credit.amount)
            credit.user.account.save()
            credit.save()
            return redirect('transactions:creditcard_details',credit.number,credit.user.account.account_number)    
    context={
        'credit':credit
    }
    return render(request,'account/credit_card_bill.html',context)
    
def withdraw_amt_from(request,card_id):
    # account=Account.objects.get(user=request.user)
    credit=Creditcard.objects.get(card_id=card_id)
    if request.method=='POST':
        amount_entered=request.POST.get('amount')
        print(amount_entered)
        if credit.user.account.account_balance<=0 or credit.user.account.account_balance<int(amount_entered):
            print("insufficient amount")
        else:
            credit.amount-=int(amount_entered)
            credit.user.account.account_balance+=int(amount_entered)
            print(credit.user.account.account_balance)
            credit.save()
            credit.user.account.save()
            return redirect('transactions:creditcard_details',credit.number,credit.user.account.account_number)    
    context={
        # 'account':account,
        'credit':credit
    }
    return render(request,'account/withdraw_amount.html',context)
    


def card_delete(request,card_id):
    credit_detail=Creditcard.objects.get(card_id=card_id)
    if request.method=='POST':
        if credit_detail.amount>0:
            credit_detail.user.account.account_balance+=credit_detail.amount
            credit_detail.user.account.save()
            credit_detail.delete()
            return redirect('bankaccounts:dash')
        elif credit_detail.amount==0:
            credit_detail.delete()
            return redirect('bankaccounts:dash')
    return render(request,'account/credit_card_delete.html')


            