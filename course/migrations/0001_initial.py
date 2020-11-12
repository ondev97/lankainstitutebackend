<<<<<<< HEAD
# Generated by Django 3.0 on 2020-11-06 17:29
=======
# Generated by Django 3.0 on 2020-11-11 13:50
>>>>>>> ad6d5f28082237ef1433d0393d306645a0ff0004

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(default=None, max_length=300)),
                ('course_description', models.TextField(null=True)),
                ('course_cover', models.ImageField(blank=True, null=True, upload_to='course_covers/')),
                ('author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.TeacherProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_name', models.CharField(max_length=100)),
                ('module_content', models.CharField(max_length=100)),
                ('file', models.FileField(null=True, upload_to='course_files/')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='course.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enroll_key', models.CharField(default='Text here', max_length=100, null=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enrollment', to='course.Course')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.StudentProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_key', models.CharField(max_length=100, null=True)),
                ('isValid', models.BooleanField(default=True)),
                ('isIssued', models.BooleanField(default=False)),
                ('expire_date', models.DateField(null=True, verbose_name='expire_date')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
            ],
        ),
    ]
