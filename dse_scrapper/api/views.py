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
    return JsonResponse(dseData, safe=False)

def circuitBreaker(request):
    dseData = getCircuitBreakerRecords()
    # print(dseData)
    return JsonResponse(dseData, safe=False)

def topGainer(request):
    dseData = getTopGainerRecords()
    # print(dseData)
    return JsonResponse(dseData, safe=False)

def topLoser(request):
    dseData = getTopLooserRecords()
    # print(dseData)
    return JsonResponse(dseData, safe=False)

def listedCompanies(request):
    dseData = getListedCompanies()
    # print(dseData)
    return JsonResponse(dseData, safe=False)
