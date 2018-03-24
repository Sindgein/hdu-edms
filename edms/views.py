# -*- coding:utf-8 -*-
from django.shortcuts import render
from .models import *
from django.http import HttpResponse,FileResponse,StreamingHttpResponse,JsonResponse
# Create your views here.
def edms(request):
    return render(request,'edms/index.html')


def file_download(request):
    # do something...
    a = MyModel.objects.all()[2]
    paths = a.upload.url
    
    with open(paths,'rb') as f:
        c = f.read()
    
    response = HttpResponse(c)        
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="test.xlsx"'
    return response
    # return JsonResponse('hello',safe=False)