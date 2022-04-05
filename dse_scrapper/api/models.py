from django.db import models

# Create your models here.


class StockPriceInfo(models.Model):
    dse_id = models.CharField(max_length=200)
    trading_code = models.CharField(max_length=200)
    ltp = models.CharField(max_length=200)
    highest_trade = models.CharField(max_length=200)
    lowest_trade = models.CharField(max_length=200)
    closeP = models.CharField(max_length=200)
    ycp = models.CharField(max_length=200)
    change = models.CharField(max_length=200)
    trade = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    volume = models.CharField(max_length=200)
