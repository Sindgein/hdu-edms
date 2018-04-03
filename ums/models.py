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

    def __str__(self):
        return u'%s' % self.username


class Teacher(models.Model):
    user = models.OneToOneField(
        User, related_name='teacher', on_delete=models.CASCADE)
    is_assitant = models.BooleanField(default=False, verbose_name='管理员助手')
    name = models.CharField(max_length=20, verbose_name='教师姓名')

    class Meta:
        verbose_name = '老师'
        verbose_name_plural = '老师'

    def __str__(self):
        return u'%s' % self.name


class Student(models.Model):
    user = models.OneToOneField(
        User, related_name='student', on_delete=models.CASCADE)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name='students', blank=True)
    is_assitant = models.BooleanField(default=False, verbose_name='管理员助手')
    name = models.CharField(max_length=20, verbose_name='学生姓名')
    # student_id = models.IntegerField(verbose_name='学号')

    _class = models.CharField(max_length=20, verbose_name='班级', blank=True)
    major = models.CharField(max_length=100, verbose_name='专业', blank=True)
    school = models.CharField(max_length=50, verbose_name='学院', blank=True)
    gra_des = models.CharField(
        max_length=100, default='未选', verbose_name='毕设题目', blank=True)
    # teacher = models.CharField(max_length=20, verbose_name='指导老师')
    # socer = models.CharField(max_length=50, verbose_name='成绩')

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = '学生'

    def __str__(self):
        return u'%s' % self.name

    def student_info(self):
        return {
            'student_id': self.user.username,
            'student_name': self.name,
            '_class': self._class,
            'major': self.major,
            'school': self.school,
            'gra_des': self.gra_des}
