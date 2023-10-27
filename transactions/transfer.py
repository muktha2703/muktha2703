from django.shortcuts import render
from bankaccounts.models import Account,KYC
from django.db.models import Q
from django.shortcuts import redirect
from django.contrib import messages
from transactions.models import Transaction
# Create your views here.
def search_user_by_acc_num(request):
    account=Account.objects.all()
    query=request.POST.get("account_number")
    print(query)
    if query:
        account=account.filter(
            Q(account_number=query)
        ).distinct()
        
    context={
        'account':account,
        'query':query
    }
    return render(request,'core/search_user.html',context)

def amount_transfer(request,account_number):
    try:
       account=Account.objects.get(account_number=account_number)
    except:
        messages.warning("Account does not exist")
    context={ 
        "account":account,
    }
    return render(request,'core/amount_transfer.html',context)

def amount_transfer_process(request,account_number):
    account=Account.objects.get(account_number=account_number)
    sender=request.user
    receiver=account.user
    sender_account=request.user.account
    receiver_account=account
    if request.method =='POST':
      amount=request.POST.get('amount-send')
      description=request.POST.get('description')
      if sender_account.account_balance > 0 and amount:
          new_transaction=Transaction.objects.create(
              description=description,
              user=request.user,
              amount=amount,
              sender_account=sender_account,
              sender=sender,
              receiver=receiver,
              receiver_account=receiver_account,
              status='pending',
              transaction_type='None',
          )
          new_transaction.save()
          transaction_id=new_transaction.transaction_id
          return  redirect('transactions:transfer_confirmation',account.account_number,transaction_id)
        #   print(transaction_id)
    return render(request,'core/amount_transfer_process.html',{'account':account})

def transfer_confermation(request,account_number,transaction_id):
    try:
      account=Account.objects.get(account_number=account_number)
      transaction=Transaction.objects.get(transaction_id=transaction_id)
    #   kyc=KYC.objects.get(account_number=account_number)
      print(account.pin_number)
      if request.method == 'POST':
        pin_num=request.POST.get('pin-number')
        if transaction.amount<=account.account_balance:
          if account.pin_number==pin_num:
            print('intial balance',account.account_balance)
            account.account_balance=account.account_balance-transaction.amount
            account.save()
            print('final amount',account.account_balance)
            transaction.status='completed'
            transaction.save()
            print(transaction.status)
            print('entered pinnumber',pin_num)
            return redirect('transactions:transfer_success',account.account_number,transaction_id)
          else:
            print('pin number is not matching')
          
        else:
           print('insuffcient balance')
      
    except:
        messages.warning('account doesnot exit')
    context={
       'account':account,
       'transaction':transaction,
      
       }
    return render(request,'core/transfer_confirmation.html',context)


def transfer_success(request,account_number,transaction_id):
    account=Account.objects.get(account_number=account_number)
    transaction=Transaction.objects.get(transaction_id=transaction_id)
    context={
       'account':account,
       'transaction':transaction,
      
       }
    return render(request,'core/transfer_success.html',context)
   
def transaction_detail(request,transaction_id):
    user=request.user
    account=Account.objects.get(user=user)
    kyc=KYC.objects.get(user=user)
    transaction=Transaction.objects.get(transaction_id=transaction_id)
    receiver=account.user
    context={
       'account':account,
       'kyc':kyc,
       'transaction':transaction,
       'receiver':receiver
       }
    return render(request,'core/transfer_detail.html',context)
def transaction_list(request):
  user=request.user
  account=Account.objects.get(user=user)
  kyc=KYC.objects.get(user=user)
  transaction=Transaction.objects.all()
  query1=request.POST.get("request_sent")
  query2=request.POST.get("completed")
  if query1:
     transaction=transaction.filter(
        Q(status=query1)
     ).distinct()
  if query2:
     transaction=transaction.filter(
        Q(status=query2)
     ).distinct()
  context={
     'account':account,
     'kyc':kyc,
     'transaction':transaction,
     'query1':query1,
     'query2':query2,
  }
  return render(request,'core/transaction_list.html',context)