# Generated by Django 2.0 on 2018-04-04 05:22

from django.db import migrations, models
import django.db.models.deletion
import edms.file_storage.file_storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraDesFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graduation_thesis', models.CharField(max_length=100, null=True, verbose_name='毕设题目')),
                ('student_id', models.CharField(blank=True, max_length=100)),
                ('task', models.FileField(blank=True, storage=edms.file_storage.file_storage.FileStorage(), upload_to='unchecked/GraDesFiles/', verbose_name='任务书')),
                ('translation', models.FileField(blank=True, storage=edms.file_storage.file_storage.FileStorage(), upload_to='unchecked/GraDesFiles/', verbose_name='外文翻译(附原文)')),
                ('summary', models.FileField(blank=True, storage=edms.file_storage.file_storage.FileStorage(), upload_to='unchecked/GraDesFiles/', verbose_name='文献综述')),
                ('begin_report', models.FileField(blank=True, storage=edms.file_storage.file_storage.FileStorage(), upload_to='unchecked/GraDesFiles/', verbose_name='开题报告')),
                ('paper', models.FileField(blank=True, storage=edms.file_storage.file_storage.FileStorage(), upload_to='unchecked/GraDesFiles/', verbose_name='毕业设计(论文)')),
                ('check_table', models.FileField(blank=True, storage=edms.file_storage.file_storage.FileStorage(), upload_to='unchecked/GraDesFiles/', verbose_name='考核表')),
                ('task_record', models.FileField(blank=True, storage=edms.file_storage.file_storage.FileStorage(), upload_to='unchecked/GraDesFiles/', verbose_name='指导记录')),
                ('addition', models.FileField(blank=True, storage=edms.file_storage.file_storage.FileStorage(), upload_to='unchecked/GraDesFiles/', verbose_name='附件(设计图纸，软件等)')),
                ('project_training', models.FileField(blank=True, storage=edms.file_storage.file_storage.FileStorage(), upload_to='unchecked/GraDesFiles/', verbose_name='实习手册')),
                ('archive', models.FileField(blank=True, upload_to='checked/GraDesFiles/', verbose_name='存档')),
                ('auditing_opinion', models.TextField(blank=True, verbose_name='审核意见')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gradesfiles', to='ums.Teacher', verbose_name='老师')),
            ],
            options={
                'verbose_name': '毕业设计档案',
                'verbose_name_plural': '毕业设计档案',
                'permissions': (('audit', 'Can audit graduation design'),),
            },
        ),
        migrations.CreateModel(
            name='TeachFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teachers', models.CharField(max_length=100, verbose_name='授课教师')),
                ('year', models.IntegerField(verbose_name='学年')),
                ('term', models.IntegerField(verbose_name='学期')),
                ('course_name', models.CharField(max_length=100, verbose_name='课程名称')),
                ('course_id', models.CharField(max_length=100, verbose_name='选课课号')),
                ('ready2audit', models.BooleanField(default=False, verbose_name='是否提交审核')),
                ('teaching_syllabus', models.FileField(blank=True, storage=edms.file_storage.file_storage.FileStorage(), upload_to='unchecked/TeachFiles/', verbose_name='教学大纲')),
                ('teaching_plan', models.FileField(blank=True, storage=edms.file_storage.file_storage.FileStorage(), upload_to='unchecked/TeachFiles/', verbose_name='教学计划')),
                ('student_score', models.FileField(blank=True, storage=edms.file_storage.file_storage.FileStorage(), upload_to='unchecked/TeachFiles/', verbose_name='学生成绩登记册')),
                ('teaching_sum_up', models.FileField(blank=True, storage=edms.file_storage.file_storage.FileStorage(), upload_to='unchecked/TeachFiles/', verbose_name='教学小结表')),
                ('exam_paper', models.FileField(blank=True, storage=edms.file_storage.file_storage.FileStorage(), upload_to='unchecked/TeachFiles/', verbose_name='正考试卷样卷')),
                ('exam_paper_answer', models.FileField(blank=True, storage=edms.file_storage.file_storage.FileStorage(), upload_to='unchecked/TeachFiles/', verbose_name='正考试卷答案及评分标准')),
                ('exam_paper_analyze', models.FileField(blank=True, storage=edms.file_storage.file_storage.FileStorage(), upload_to='unchecked/TeachFiles/', verbose_name='试卷分析')),
                ('exam_part', models.FileField(blank=True, storage=edms.file_storage.file_storage.FileStorage(), upload_to='unchecked/TeachFiles/', verbose_name='正考部分')),
                ('exam_make_up', models.FileField(blank=True, storage=edms.file_storage.file_storage.FileStorage(), upload_to='unchecked/TeachFiles/', verbose_name='补考试卷样卷')),
                ('exam_make_up_answer', models.FileField(blank=True, storage=edms.file_storage.file_storage.FileStorage(), upload_to='unchecked/TeachFiles/', verbose_name='补考试卷答案及评分标准')),
                ('exam_make_up_part', models.FileField(blank=True, storage=edms.file_storage.file_storage.FileStorage(), upload_to='unchecked/TeachFiles/', verbose_name='补考部分')),
                ('archive', models.FileField(blank=True, upload_to='checked/TeachFiles/', verbose_name='存档')),
                ('auditing_opinion', models.TextField(blank=True, verbose_name='审核意见')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='ums.Teacher', verbose_name='老师，负责上传')),
            ],
            options={
                'verbose_name': '教学档案',
                'verbose_name_plural': '教学档案',
                'permissions': (('audit', 'Can audit teaching files'),),
            },
        ),
    ]
