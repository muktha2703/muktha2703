from django.urls import path
from transactions import transfer,payment_request,credit_card
from bankaccounts.models import Account
app_name="transactions"
urlpatterns=[
    path("",transfer.search_user_by_acc_num,name="search"),
    path("amount_transfer/<account_number>/",transfer.amount_transfer,name="amount_transfer"),
    path("amount_transfer_process/<account_number>/",transfer.amount_transfer_process,name="amount_transfer_process"),
    path('transfer_confirmation/<account_number>/<transaction_id>/',transfer.transfer_confermation,name='transfer_confirmation'),
    path('transfer_success/<account_number>/<transaction_id>/',transfer.transfer_success,name='transfer_success'),
    path('transaction_detail/<transaction_id>',transfer.transaction_detail,name="transaction_detail"),
    path('user_request_payment/',payment_request.user_request_payment_by_accnum,name='user_request_payment'),
    path('request_amount/<account_number>/',payment_request.request_amount,name='request_amount'),
    path('request_amount_confirmation/<account_number>/<transaction_id>/',payment_request.request_amount_confirmation,name='request_amount_confirmation'),
    path('request_confirmation_success/<account_number>/<transaction_id>/',payment_request.request_confirmation_success,name='confirmation_success'),
    path('transaction_list/',transfer.transaction_list,name="transaction_list"),
    path('send_confirmation/<account_number>/',payment_request.send_confirmation,name='send_confirmation'),
    path('send_completed/<account_number>/<transaction_id>/',payment_request.send_completed,name='send_completed'),
    path('send_amount_completed/<account_number>/<transaction_id>/',payment_request.send_amount_success,name='send_amount_completed'),
    path('creditcard_details/<number>/<account_number>/',credit_card.credit_card_detail,name='creditcard_details'),
    path('credit_card_bill/<card_id>/',credit_card.credit_card_bill,name='credit_bill'),
    path('withdraw_amount/<card_id>/',credit_card.withdraw_amt_from,name='withdraw_amount'),
    path('credit_card_delete/<card_id>/',credit_card.card_delete,name='credit_card_delete')
]