# Generated by Django 3.2.9 on 2021-11-24 01:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_grade_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='recommendedYear',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)]),
        ),
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]