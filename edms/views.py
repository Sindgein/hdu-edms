# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, FileResponse, StreamingHttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import *
import json
# Create your views here.

@login_required
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


def get_teach_file_list(request):
    teacher = request.user.teacher
    file_set = teacher.course.all()
    file_set_info = [f.file_info_list() for f in file_set]
    return JsonResponse(file_set_info, safe=False)


def get_teach_file_detail(request, course_id):
    teacher = request.user.teacher
    teachfile = teacher.course.get(course_id=course_id)
    return JsonResponse(teachfile.file_detail(), safe=False)


def get_gradesign_file_list(request):
    teacher = request.user.teacher
    file_set = teacher.gradesfiles.all()
    file_set_info = [f.file_info_list() for f in file_set]
    return JsonResponse(file_set_info, safe=False)


def get_gradesign_file_detail(request, graduation_thesis):
    teacher = request.user.teacher
    gradesign = teacher.gradesfiles.get(graduation_thesis=graduation_thesis)
    return JsonResponse(gradesign.file_detail(), safe=False)
