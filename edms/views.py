# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, FileResponse, StreamingHttpResponse, JsonResponse
from .models import *
import json
# Create your views here.


def edms(request):
    content = {
        'user_id': request.user.username,
        'user_name': request.user.teacher.name
    }
    return render(request, 'edms/index.html', context=content)


def file_download(request):
    # do something...
    a = MyModel.objects.all()[2]
    paths = a.upload.url

    with open(paths, 'rb') as f:
        c = f.read()

    response = HttpResponse(c)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="test.xlsx"'
    return response


def get_teachfile(request):
    teacher = request.user.teacher
    file_set = teacher.course.all()
    file_set_info = [file.file_info() for file in file_set]
    return JsonResponse(file_set_info, safe=False)
