# Generated by Django 5.0.7 on 2024-09-24 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBApp', '0004_alter_teacher_mobile_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Sid',
            field=models.IntegerField(null=True),
        ),
    ]
