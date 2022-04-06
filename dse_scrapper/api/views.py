from django.http import HttpResponse

from .scrap_data import getStockRecords, getCircuitBreakerRecords, getTopGainerRecords, getTopLooserRecords

def index(request):
    queryprms = request.GET
    filterValue = queryprms.get('filter')

    if(filterValue):
        dseData = getStockRecords(filter=filterValue)
    else:
        dseData = getStockRecords()

    # print(dseData)
    return HttpResponse(dseData)

def circuitBreaker(request):
    dseData = getCircuitBreakerRecords()
    # print(dseData)
    return HttpResponse(dseData)

def topGainer(request):
    dseData = getTopGainerRecords()
    # print(dseData)
    return HttpResponse(dseData)

def topLoser(request):
    dseData = getTopLooserRecords()
    # print(dseData)
    return HttpResponse(dseData)
