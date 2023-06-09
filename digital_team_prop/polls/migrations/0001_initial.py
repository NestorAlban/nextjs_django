# Generated by Django 4.1.7 on 2023-03-14 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_name', models.CharField(max_length=200)),
                ('child_birth_date', models.DateTimeField(auto_now_add=True, verbose_name='birth date')),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='date registered')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('reviews', models.IntegerField(auto_created=True, default=0)),
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('course_description', models.CharField(max_length=150)),
                ('teacher', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='date registered')),
                ('update_date', models.DateTimeField(auto_now_add=True, verbose_name='date registered')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_name', models.CharField(max_length=100)),
                ('parent_mail', models.CharField(max_length=100)),
                ('parent_phone', models.CharField(max_length=30)),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='date registered')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='date registered')),
                ('update_date', models.DateTimeField(auto_now_add=True, verbose_name='date registered')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.child')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.course')),
            ],
        ),
        migrations.AddField(
            model_name='child',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.parent'),
        ),
    ]
