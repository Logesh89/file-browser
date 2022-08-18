# Generated by Django 3.1.3 on 2022-08-17 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfileapp', '0002_remove_file_upload_file_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('ids', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('path', models.FilePathField(default='C:/Users/developer/Downloads/', path='C:/Users/developer/Downloads/')),
            ],
        ),
    ]