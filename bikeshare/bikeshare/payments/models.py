from django.db import models

# Create your models here.

class Transaction(models.Model):
    braintree_id = models.CharField(max_length=100)
    nonce = models.CharField(max_length=500)
    amount = models.DecimalField(decimal_places=2, max_digits=10)