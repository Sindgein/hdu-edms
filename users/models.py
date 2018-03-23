from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# 管理员，通过django admin后台注册，不开放注册入口


class Admin(models.Model):
    user = models.OneToOneField(
        User, related_name='admin', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '管理员'
        verbose_name_plural = '管理员'


class Teacher(models.Model):
    user = models.OneToOneField(
        User, related_name='teacher', on_delete=models.CASCADE)
    is_assitant = models.BooleanField(default=False, verbose_name='管理员助手')
    name = models.CharField(max_length=20, verbose_name='教师姓名')

    class Meta:
        verbose_name = '老师'
        verbose_name_plural = '老师'


class Student(models.Model):
    user = models.OneToOneField(
        User, related_name='student', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    is_assitant = models.BooleanField(default=False, verbose_name='管理员助手')
    name = models.CharField(max_length=20, verbose_name='学生姓名')
    # student_id = models.IntegerField(verbose_name='学号')

    _class = models.CharField(max_length=20, verbose_name='班级', null=True)
    major = models.CharField(max_length=100, verbose_name='专业', null=True)
    school = models.CharField(max_length=50, verbose_name='学院', null=True)
    grades = models.CharField(max_length=100, verbose_name='题目', null=True)
    # teacher = models.CharField(max_length=20, verbose_name='指导老师')
    # socer = models.CharField(max_length=50, verbose_name='成绩')

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = '学生'
