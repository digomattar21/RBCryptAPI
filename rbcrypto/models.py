from djongo import models

class Ticker(models.Model):
  symbol = models.CharField(max_length=10)
  class Meta:
    abstract = True


class User(models.Model):
  username= models.CharField(max_length=50)
  email = models.EmailField()
  token = models.CharField(max_length=200, null=True)
  watchlist = models.ArrayField(model_container=Ticker)
  

