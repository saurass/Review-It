# Generated by Django 2.1.4 on 2019-01-06 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_org_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('service', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
