from django.shortcuts import render
import json

from django.http import HttpResponse
import braintree

# Create your views here.

def get_token(request):
    #customer_id = str(request.GET.get('customer_id'))
    client_token = braintree.ClientToken.generate({
    #   "customer_id": customer_id
    })
    response = {}
    response["client_token"] = client_token
    return HttpResponse(json.dumps(response), content_type="application/json")