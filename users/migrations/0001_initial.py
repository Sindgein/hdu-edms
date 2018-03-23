# Generated by Django 2.0 on 2018-03-23 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '管理员',
                'verbose_name_plural': '管理员',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_assitant', models.BooleanField(default=False, verbose_name='管理员助手')),
                ('name', models.CharField(max_length=20, verbose_name='学生姓名')),
                ('_class', models.CharField(max_length=20, null=True, verbose_name='班级')),
                ('major', models.CharField(max_length=100, null=True, verbose_name='专业')),
                ('school', models.CharField(max_length=50, null=True, verbose_name='学院')),
                ('grades', models.CharField(max_length=100, null=True, verbose_name='题目')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_assitant', models.BooleanField(default=False, verbose_name='管理员助手')),
                ('name', models.CharField(max_length=20, verbose_name='教师姓名')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '老师',
                'verbose_name_plural': '老师',
            },
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Teacher'),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
    ]
