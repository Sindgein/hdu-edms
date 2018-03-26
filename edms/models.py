from django.db import models
from users.models import Teacher, Student
import json


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
        try:
            index = self.teaching_syllabus.path.find('uploads')
        except:
            pass
        if self.teaching_syllabus:
            detail['teaching_syllabus'] = {
                'url': self.teaching_syllabus.path[index::]}
        else:
            detail['teaching_syllabus'] = {'url': 'null'}
        if self.teaching_plan:
            detail['teaching_plan'] = {'url': self.teaching_plan.path[index::]}
        else:
            detail['teaching_plan'] = {'url': 'null'}
        if self.student_score:
            detail['student_score'] = {'url': self.student_score.path[index::]}
        else:
            detail['student_score'] = {'url': 'null'}
        if self.teaching_sum_up:
            detail['teaching_sum_up'] = {
                'url': self.teaching_sum_up.path[index::]}
        else:
            detail['teaching_sum_up'] = {'url': 'null'}
        if self.exam_paper:
            detail['exam_paper'] = {'url': self.exam_paper.path[index::]}
        else:
            detail['exam_paper'] = {'url': 'null'}
        if self.exam_paper_answer:
            detail['exam_paper_answer'] = {
                'url': self.exam_paper_answer.path[index::]}
        else:
            detail['exam_paper_answer'] = {'url': 'null'}
        if self.exam_paper_analyze:
            detail['exam_paper_analyze'] = {
                'url': self.exam_paper_analyze.path[index::]}
        else:
            detail['exam_paper_analyze'] = {'url': 'null'}
        if self.exam_part:
            detail['exam_part'] = {'url': self.exam_part.path[index::]}
        else:
            detail['exam_part'] = {'url': 'null'}
        if self.exam_make_up:
            detail['exam_make_up'] = {'url': self.exam_make_up.path[index::]}
        else:
            detail['exam_make_up'] = {'url': 'null'}
        if self.exam_make_up_answer:
            detail['exam_make_up_answer'] = {
                'url': self.exam_make_up_answer.path[index::]}
        else:
            detail['exam_make_up_answer'] = {'url': 'null'}
        if self.exam_make_up_part:
            detail['exam_make_up_part'] = {
                'url': self.exam_make_up_part.path[index::]}
        else:
            detail['exam_make_up_part'] = {'url': 'null'}
        if self.auditing_opinion:
            detail['auditing_opinion'] = {
                'url': self.auditing_opinion.path[index::]}
        else:
            detail['auditing_opinion'] = {'url': 'null'}

        return detail


class GraDesFiles(models.Model):
        # 基本信息,需要填写的表单
    student = models.ForeignKey(
        Student, verbose_name='学生', on_delete=models.CASCADE, related_name='gradesfiles')
    name = models.CharField(max_length=100, verbose_name='毕设题目', null=True)
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

# class Course(models.Model):
#     teacher = models.ForeignKey(
#         Teacher, on_delete=models.CASCADE, verbose_name='老师，负责上传', related_name='course')
#     # 考虑到上课教师可能不唯一，存在多个教师授课的情况
#     teachers = models.CharField(max_length='100', verbose_name='授课教师')
#     year = models.IntegerField(verbose_name='学年')
#     term = models.CharField(max_length=10, verbose_name='学期')
#     course_name = models.CharField(max_length=100, verbose_name='课程名称')
#     course_id = models.CharField(max_length=100, verbose_name='选课课号')

#     class Meta:
#         verbose_name = '档案信息'
#         verbose_name_plural = '档案信息'

#     @classmethod
#     def get_course_by_teacher(cls, teacher):
#         courses = [{'course_name': course.course_name,
#                     'course_id': course.course_id,
#                     'year': course.year,
#                     'term': course.term}
#                    for course in cls.objects.get(teacher=teacher)]
#         return json.dumps(courses)

# # 教案，对应于课程
