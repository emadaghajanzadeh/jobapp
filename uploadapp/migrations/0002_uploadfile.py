# Generated by Django 3.2.16 on 2022-12-22 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
