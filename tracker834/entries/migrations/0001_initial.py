# Generated by Django 2.2.6 on 2019-10-04 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folderName', models.CharField(blank=True, max_length=50, null=True)),
                ('subfolder', models.CharField(blank=True, max_length=100, null=True)),
                ('subfolder2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('queryUsedFor', models.CharField(blank=True, max_length=500, null=True)),
                ('queryName', models.CharField(max_length=50)),
                ('files', models.CharField(blank=True, max_length=100, null=True)),
                ('convertYN', models.BooleanField(default=False)),
                ('conversionStartDate', models.DateField(blank=True, null=True, verbose_name='Conversion Start Date')),
                ('assignedTo', models.CharField(blank=True, max_length=20, null=True)),
                ('conversionCompletionDate', models.DateField(blank=True, null=True, verbose_name='Conversion Completion Date')),
                ('newNameInBI', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
