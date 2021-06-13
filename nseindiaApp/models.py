from django.db import models

# Create your models here.
class NSECalls(models.Model):
    openInterest = models.IntegerField(blank=True, null=True)
    changeinOpenInterest = models.IntegerField(blank=True, null=True)
    totalTradedVolume = models.IntegerField(blank=True, null=True)
    impliedVolatility = models.FloatField(max_length=10, blank=True, null=True)
    lastPrice = models.FloatField(max_length=20, blank=True, null=True)
    change = models.FloatField(max_length=20, blank=True, null=True)
    bidQty = models.IntegerField(blank=True, null=True)
    bidprice = models.FloatField(max_length=20, blank=True, null=True)
    askPrice = models.FloatField(max_length=20, blank=True, null=True)
    askQty = models.IntegerField(blank=True, null=True)
    strikePrice = models.FloatField(max_length=20, blank=True, null=True)
    expiryDate = models.CharField(max_length=20,blank=True,null=True)

class NSEPuts(models.Model):
    strikePrice = models.FloatField(max_length=20, blank=True, null=True)
    bidQty = models.IntegerField(blank=True, null=True)
    bidprice = models.FloatField(max_length=20, blank=True, null=True)
    askPrice = models.FloatField(max_length=20, blank=True, null=True)
    askQty = models.IntegerField(blank=True, null=True)
    change = models.FloatField(max_length=20, blank=True, null=True)
    lastPrice = models.FloatField(max_length=20, blank=True, null=True)
    impliedVolatility = models.FloatField(max_length=10, blank=True, null=True)
    totalTradedVolume = models.IntegerField(blank=True, null=True)
    changeinOpenInterest = models.IntegerField(blank=True, null=True)
    openInterest = models.IntegerField(blank=True, null=True)
    expiryDate = models.CharField(max_length=20,blank=True,null=True)
    
