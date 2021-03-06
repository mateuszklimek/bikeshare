from django.shortcuts import render
import json

from django.http import HttpResponse
import braintree
from bikeshare.payments.models import Transaction
from django.views.decorators.csrf import csrf_exempt

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

def test(request):
    return render(request, 'index.html', locals())

# Create your views here.

def get_token(request):
    #customer_id = str(request.GET.get('customer_id'))
    client_token = braintree.ClientToken.generate({
    #   "customer_id": customer_id
    })
    response = {}
    response["client_token"] = client_token
    return HttpResponse(json.dumps(response), content_type="application/json")

@csrf_exempt
def new_bike(request):
    nonce = request.POST.get('payment_method_nonce')
    result = braintree.Transaction.sale({
        "amount": "10.00",
        "payment_method_nonce": nonce
    })
    response = {}
    response["success"] = result.is_success
    if not result.is_success:
        response["message"] = result.message
    else:
        result2 = braintree.Transaction.submit_for_settlement(result.transaction.id)
        Transaction.objects.create(braintree_id=str(result.transaction.id), nonce=nonce, amount=result.transaction.amount)
        response["success"] = result2.is_success
        if not result2.is_success:
            response["message"] = result2.message
        else:
            send_mail("Bike rented", "Your bike has been rented",
                "Mateusz Klimek <matkk11gmail.com>", ["k.sawicka.k@gmail.com"])


    return HttpResponse(json.dumps(response), content_type="application/json")
