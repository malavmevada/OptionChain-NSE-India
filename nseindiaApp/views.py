from django.shortcuts import render
import requests
import json
from .models import NSEPuts, NSECalls


def get_data(request):
    youroption = 'NIFTY'
    yourPrice = ''
    yourDate = ''
    final = []
    if request.GET.get('options') == 'NIFTY':
        youroption = 'NIFTY'
    elif request.GET.get('options') == 'FINNIFTY':
        youroption = 'FINNIFTY'
    elif request.GET.get('options') == 'BANKNIFTY':
        youroption = 'BANKNIFTY'
    check = False
    try:
        oldoption = youroption
        url = 'https://www.nseindia.com/api/option-chain-indices?symbol=' + youroption
        headers = {'User-Agent': 'Mozilla/5.0'}
        data = requests.get(url, headers=headers).content
        data2 = data.decode('utf-8')
        df = json.loads(data2)
        final_data = df['records']['data']
        all_nse_ce = {}
        all_nse_pe = {}
        remove_ce = NSECalls.objects.all()
        remove_ce.delete()
        remove_pe = NSEPuts.objects.all()
        remove_pe.delete()
        for i in final_data:
            if 'PE' in i:
                pe = i['PE']
                nse_pe = NSEPuts(
                    strikePrice=round(i['strikePrice'], 2),
                    expiryDate = i['expiryDate'],
                    bidQty=round(pe['bidQty'], 2),
                    bidprice=round(pe['bidprice'], 2),
                    askPrice=round(pe['askPrice'], 2),
                    askQty=round(pe['askQty'], 2),
                    change=round(pe['change'], 2),
                    lastPrice=round(pe['lastPrice'], 2),
                    impliedVolatility=round(pe['impliedVolatility'], 2),
                    totalTradedVolume=round(pe['totalTradedVolume'], 2),
                    changeinOpenInterest=round(pe['changeinOpenInterest'], 2),
                    openInterest=round(pe['openInterest'], 2)
                )
                nse_pe.save()
            else:
                nse_pe = NSEPuts(
                    strikePrice=round(i['strikePrice'], 2),
                    expiryDate = i['expiryDate'],
                    bidQty=0,
                    bidprice=0,
                    askPrice=0,
                    askQty=0,
                    change=0,
                    lastPrice=0,
                    impliedVolatility=0,
                    totalTradedVolume=0,
                    changeinOpenInterest=0,
                    openInterest=0
                )
                nse_pe.save()

            if 'CE' in i:
                ce = i['CE']
                nse_ce = NSECalls(
                    strikePrice=round(i['strikePrice'], 2),
                    expiryDate = i['expiryDate'],
                    bidQty=round(ce['bidQty'], 2),
                    bidprice=round(ce['bidprice'], 2),
                    askPrice=round(ce['askPrice'], 2),
                    askQty=round(ce['askQty'], 2),
                    change=round(ce['change'], 2),
                    lastPrice=round(ce['lastPrice'], 2),
                    impliedVolatility=round(ce['impliedVolatility'], 2),
                    totalTradedVolume=round(ce['totalTradedVolume'], 2),
                    changeinOpenInterest=round(ce['changeinOpenInterest'], 2),
                    openInterest=round(ce['openInterest'], 2)
                )
                nse_ce.save()
            else:
                nse_ce = NSECalls(
                    strikePrice=round(i['strikePrice'], 2),
                    expiryDate = i['expiryDate'],
                    bidQty=0,
                    bidprice=0,
                    askPrice=0,
                    askQty=0,
                    change=0,
                    lastPrice=0,
                    impliedVolatility=0,
                    totalTradedVolume=0,
                    changeinOpenInterest=0,
                    openInterest=0
                )
                nse_ce.save()

        if request.GET.get('price') != 'select':
            yourPrice = request.GET.get('price')
            if len(yourPrice)==0:
                all_nse_ce = NSECalls.objects.all()
                all_nse_pe = NSEPuts.objects.all()
            else:
                all_nse_ce = NSECalls.objects.filter(strikePrice=yourPrice)
                all_nse_pe = NSEPuts.objects.filter(strikePrice=yourPrice)

        elif request.GET.get('ex-date') != 'select':
            yourDate = request.GET.get('ex-date')
            if len(yourDate) == 0:
                all_nse_ce = NSECalls.objects.all()
                all_nse_pe = NSEPuts.objects.all()
            else:
                all_nse_ce = NSECalls.objects.filter(expiryDate=yourDate)
                all_nse_pe = NSEPuts.objects.filter(expiryDate=yourDate)
        else:
            all_nse_ce = NSECalls.objects.all()
            all_nse_pe = NSEPuts.objects.all()
        final = list(zip(all_nse_ce, all_nse_pe))

    except Exception as e:
        check = True

    return render(request,'core/home.html',{
    "final": final,
    "check":check,
    "oldOption":oldoption,
    "yourOption": youroption,
    "yourPrice":yourPrice,
    "yourDate":yourDate
    })
