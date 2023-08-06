# Generated by Django 4.1.1 on 2022-11-10 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_code', models.CharField(max_length=50, null=True)),
                ('c_name', models.CharField(max_length=50, null=True)),
                ('c_semester', models.CharField(max_length=30, null=True)),
                ('c_creadit', models.CharField(max_length=30, null=True)),
                ('c_Teacher', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50, null=True)),
                ('student_mailid', models.EmailField(max_length=254, null=True)),
                ('student_PRN', models.CharField(max_length=50, null=True)),
                ('student_branch', models.CharField(max_length=30, null=True)),
                ('student_year', models.CharField(max_length=30, null=True)),
                ('student_semester', models.CharField(max_length=30, null=True)),
                ('student_phno', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=50, null=True)),
                ('t_mail', models.EmailField(max_length=254, null=True)),
                ('t_phno', models.CharField(max_length=30, null=True)),
                ('t_Gender', models.CharField(max_length=50, null=True)),
                ('t_Occupation', models.CharField(max_length=50, null=True)),
                ('t_branch', models.CharField(max_length=50, null=True)),
                ('t_post', models.CharField(max_length=50, null=True)),
                ('t_DOB', models.DateField(max_length=50, null=True)),
                ('tid_name', models.CharField(max_length=50, null=True)),
                ('tid_no', models.CharField(max_length=50, null=True)),
                ('t_issue_date', models.DateField(max_length=50, null=True)),
            ],
        ),
    ]