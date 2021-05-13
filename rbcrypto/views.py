from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Ticker
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    users = User.objects.all()
    return JsonResponse({'message': list(users)})

@csrf_exempt
def signupwithemail(request):
  data = json.loads(request.body)
  email = data['email']
  username = data['username']

  userHasAcc = User.objects.filter(email=email)

  if userHasAcc:
    return JsonResponse({"message": "Already a member"})

  user = User(email=email, username=username, watchlist=[])
  user.save()

  return JsonResponse({"message": "OK"})

@csrf_exempt
def signupwithgoogle(request):
  data = json.loads(request.body)
  email = data['email']
  username = data['username']

  userHasAcc = User.objects.filter(email=email)

  if userHasAcc:
    return JsonResponse({"message": "Already a member"})

  user = User(email=email, username=username, watchlist=[])
  user.save()
  return JsonResponse({"message": "OK"})

@csrf_exempt
def addtowatchlist(request):
  data = json.loads(request.body)
  symbol = data['symbol']
  email = data['email']
  user = User.objects.get(email=email)

  if {'symbol': symbol} in user.watchlist:
    return JsonResponse({"message": 'already in watchlist'})
    
  user.watchlist.append({'symbol': symbol})
  user.save()
  return JsonResponse({'message': "OK"})

@csrf_exempt
def getwatchlistinfo(request):
  data = json.loads(request.body)
  email = data['email']
  user = User.objects.get(email=email)

  return JsonResponse({"tickers": user.watchlist})
  

@csrf_exempt
def removetickerfromwatchlist(request):
  data = json.loads(request.body)
  email = data['email']
  tickerSymbol = data['tickerSymbol']

  user = User.objects.get(email=email)
  if {"symbol":tickerSymbol} in user.watchlist:
    user.watchlist.remove({"symbol":tickerSymbol})

  user.save()
  return JsonResponse({"message":"OK"})
