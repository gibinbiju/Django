# Generated by Django 2.1 on 2019-11-08 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batchname', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed', models.CharField(max_length=500)),
                ('bname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Batch')),
                ('cname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Course')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='feedback',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.User'),
        ),
        migrations.AddField(
            model_name='batch',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Course'),
        ),
    ]
