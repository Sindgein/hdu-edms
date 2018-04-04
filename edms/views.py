# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, FileResponse, StreamingHttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .utils import FILES, GRADESIN
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


def api_get_teach_file_list(request):
    teacher = request.user.teacher
    file_set = teacher.course.all()
    file_set_info = [f.file_info_list() for f in file_set]
    return JsonResponse(file_set_info, safe=False)


def api_get_teach_file_detail(request, course_id):
    teacher = request.user.teacher
    teachfile = teacher.course.get(course_id=course_id)
    return JsonResponse(teachfile.file_detail(), safe=False)


def api_get_gradesign_file_list(request):
    teacher = request.user.teacher
    file_set = teacher.gradesfiles.all()
    file_set_info = [f.file_info_list() for f in file_set]
    return JsonResponse(file_set_info, safe=False)


def api_get_gradesign_file_detail(request, mark):
    graduation_thesis = mark.split('-')[0]
    student_id = mark.split('-')[1]
    teacher = request.user.teacher
    gradesign = teacher.gradesfiles.get(
        graduation_thesis=graduation_thesis, student_id=student_id)
    return JsonResponse(gradesign.file_detail(), safe=False)


def api_get_student_list(request):
    teacher = request.user.teacher
    students = teacher.students.all()
    students_info = [student.student_info() for student in students]
    return JsonResponse(students_info, safe=False)


@csrf_exempt
def api_create_teach_file(request):
    rsp = {'message': 'operation success', 'status_code': 200}
    try:
        data = request.POST
        files = request.FILES
        teachfile = TeachFiles(teacher=request.user.teacher)
        for i in FILES:
            try:
                teachfile.upload_file(i, files.get(i))
            except AttributeError:
                pass
        for i in data:
            if i == 'year' or i == 'term':
                setattr(teachfile, i, int(data[i]))
            else:
                setattr(teachfile, i, data[i])

        teachfile.save()
    except:
        rsp['message'] = 'operation failed'
        rsp['status_code'] = 400

    return JsonResponse(rsp, safe=False)


@csrf_exempt
def api_create_gradesign_file(request):
    rsp = {'message': 'operation success', 'status_code': 200}
    try:
        teacher = request.user.teacher
        data = request.POST
        files = request.FILES
        gfile = GraDesFiles(teacher=teacher, student_id=data['students'],
                            graduation_thesis=data['gradesign_thesis'])
        for i in GRADESIN:
            try:
                setattr(gfile, i, files.get(i))
            except AttributeError:
                pass
        gfile.save()
    except:
        rsp['message'] = 'operation failed'
        rsp['status_code'] = 400

    return JsonResponse(rsp, safe=False)


@csrf_exempt
def api_creat_student(request):
    rsp = {'message': 'operation success', 'status_code': 200}
    try:
        teacher = request.user.teacher
        data = request.POST
        user = User(username=data['student_id'])
        user.set_password(data['student_id'])
        user.save()
        student = Student(user=user, teacher=teacher,
                          name=data['student_name'], _class=data['_class'],
                          major=data['major'], school=data['school'])
        student.save()
    except:
        rsp['message'] = 'operation failed'
        rsp['status_code'] = 400

    return JsonResponse(rsp, safe=False)


@csrf_exempt
def api_upload_single(request, file_type, file_id, file_name):
    rsp = {'message': 'operation success', 'status_code': 200}
    sfile = request.FILES.get(file_name)
    if file_type == 'tf':
        try:
            tf = TeachFiles.objects.get(course_id=file_id)
            tf.upload_file(file_name, sfile)
            tf.save()
        except:
            rsp['message'] = 'operation failed'
            rsp['status_code'] = 400
    if file_type == 'gf':
        try:
            thesis = file_id.split('-')[0]
            student_id = file_id.split('-')[1]
            gf = GraDesFiles.objects.get(
                graduation_thesis=thesis, student_id=student_id)
            gf.upload_file(file_name, sfile)
            gf.save()
        except:
            rsp['message'] = 'operation failed'
            rsp['status_code'] = 400
    return JsonResponse(rsp, safe=False)
