from django.db import models
from .utils import FILES, FILES_CN, GRADESIN, GRADESIN_CN
import time
import os
from users.models import Teacher


class TeachFiles(models.Model):
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, verbose_name='老师，负责上传', related_name='course')
    # 考虑到上课教师可能不唯一，存在多个教师授课的情况
    teachers = models.CharField(max_length=100, verbose_name='授课教师')
    year = models.IntegerField(verbose_name='学年')
    term = models.IntegerField(verbose_name='学期')
    course_name = models.CharField(max_length=100, verbose_name='课程名称')
    course_id = models.CharField(max_length=100, verbose_name='选课课号')
    ready2audit = models.BooleanField(default=False, verbose_name='是否提交审核')
    # 教学大纲
    teaching_syllabus = models.FileField(
        verbose_name='教学大纲', upload_to='uploads/TeachFiles/teaching_syllabus', blank=True)
    # 教学计划
    teaching_plan = models.FileField(
        verbose_name='教学计划', upload_to='uploads/TeachFiles/teaching_plan', blank=True)
    # 学生成绩登记册
    student_score = models.FileField(
        verbose_name='学生成绩登记册', upload_to='uploads/TeachFiles/student_socre', blank=True)
    # 教学小结表
    teaching_sum_up = models.FileField(
        verbose_name='教学小结表', upload_to='uploads/TeachFiles/teaching_sum_up', blank=True)
    # 正考试卷样卷
    exam_paper = models.FileField(
        verbose_name='正考试卷样卷', upload_to='uploads/TeachFiles/exam_paper', blank=True)
    # 正考试卷答案及评分标准
    exam_paper_answer = models.FileField(
        verbose_name='正考试卷答案及评分标准', upload_to='uploads/TeachFiles/exam_paper_answer', blank=True)
    # 试卷分析
    exam_paper_analyze = models.FileField(
        verbose_name='试卷分析', upload_to='uploads/TeachFiles/exam_paper_analyze', blank=True)
    # 正考部分
    exam_part = models.FileField(
        verbose_name='正考部分', upload_to='uploads/TeachFiles/exam_part', blank=True)
    # 补考试卷样卷
    exam_make_up = models.FileField(
        verbose_name='补考试卷样卷', upload_to='uploads/TeachFiles/exam_make_up', blank=True)
    # 补考试卷答案及评分标准
    exam_make_up_answer = models.FileField(
        verbose_name='补考试卷答案及评分标准', upload_to='uploads/TeachFiles/exam_make_up_answer', blank=True)
    # 补考部分
    exam_make_up_part = models.FileField(
        verbose_name='补考部分', upload_to='uploads/TeachFiles/exam_make_up_part', blank=True)
    # 审核意见
    auditing_opinion = models.TextField(verbose_name='审核意见', blank=True)

    class Meta:
        verbose_name = '教学档案'
        verbose_name_plural = '教学档案'
        permissions = (
            ("audit", "Can audit teaching files"),
        )

    def __str__(self):
        return u'%s' % self.course_name

    def file_info_list(self):
        return {
            'year': self.year,
            'term': self.term,
            'course_name': self.course_name,
            'course_id': self.course_id,
            'auditing_opinion': self.auditing_opinion
        }

    def file_detail(self):
        detail = {}
        for f, fc in zip(FILES, FILES_CN):
            item = getattr(self, f)
            if item:
                detail[f] = {'url': item.url, 'filename': fc,
                             'mtime': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(item.path)))}
            else:
                detail[f] = {'url': 'null', 'filename': fc + ' [未上传]'}
        return detail


class GraDesFiles(models.Model):
    # 基本信息,需要填写的表单
    teacher = models.ForeignKey(
        Teacher, verbose_name='老师', on_delete=models.CASCADE, related_name='gradesfiles')
    student_id = models.CharField(max_length=100, blank=True)
    graduation_thesis = models.CharField(
        max_length=100, verbose_name='毕设题目', null=True)
    # 毕设资料清单,需要上传的文件
    task = models.FileField(
        verbose_name='任务书', upload_to='uploads/GraDesFiles/task', blank=True)
    translation = models.FileField(
        verbose_name='外文翻译(附原文)', upload_to='uploads/GraDesFiles/translation', blank=True)
    summary = models.FileField(
        verbose_name='文献综述', upload_to='uploads/GraDesFiles/summary', blank=True)
    begin_report = models.FileField(
        verbose_name='开题报告', upload_to='uploads/GraDesFiles/begin_report', blank=True)
    paper = models.FileField(verbose_name='毕业设计(论文)',
                             upload_to='uploads/GraDesFiles/paper', blank=True)
    check_table = models.FileField(
        verbose_name='考核表', upload_to='uploads/GraDesFiles/check_table', blank=True)
    task_record = models.FileField(
        verbose_name='指导记录', upload_to='uploads/GraDesFiles/task_record', blank=True)
    addition = models.FileField(
        verbose_name='附件(设计图纸，软件等)', upload_to='uploads/GraDesFiles/addition', blank=True)
    project_training = models.FileField(
        verbose_name='实习手册', upload_to='uploads/GraDesFiles/project_training', blank=True)

    # 审核意见
    auditing_opinion = models.TextField(verbose_name='审核意见', blank=True)

    class Meta:
        verbose_name = '毕业设计档案'
        verbose_name_plural = '毕业设计档案'
        permissions = (
            ("audit", "Can audit graduation design"),
        )

    def __str__(self):
        return u'%s' % self.name

    def file_info_list(self):
        return {
            'graduation_thesis': self.graduation_thesis,
            'student_name': self.student.name,
            'student_id': self.student.user.username
        }

    def file_detail(self):
        detail = {}
        for f, fc in zip(GRADESIN, GRADESIN_CN):
            item = getattr(self, f)
            if item:
                detail[f] = {
                    'url': item.url,
                    'filename': fc,
                    'mtime': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(item.path)))
                }
            else:
                detail[f] = {'url': 'null', 'filename': fc + ' [未上传]'}
