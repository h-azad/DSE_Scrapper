from django.http import HttpResponse, JsonResponse

from .scrap_data import getStockRecords, getCircuitBreakerRecords, getTopGainerRecords, getTopLooserRecords, getListedCompanies

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

def listedCompanies(request):
    dseData = getListedCompanies()
    # print(dseData)
    return JsonResponse(dseData, safe=False)
