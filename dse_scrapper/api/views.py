from django.http import HttpResponse

from .scrap_data import getStockRecords

def index(request):
    dseData = getStockRecords()
    # print(dseData)
    return HttpResponse(dseData)
