# Generated by Django 4.2.7 on 2023-12-06 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_ادارة_افراد_student_accounting_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(unique=True),
        ),
    ]
