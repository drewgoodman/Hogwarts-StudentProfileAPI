# Generated by Django 3.2.9 on 2021-11-29 03:04

from django.db import migrations, models
import students.models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('ATTENDING', 'Attending'), ('GRADUATED', 'Graduated'), ('EXPELLED', 'Expelled'), ('DECEASED', 'Deceased')], default='ATTENDING', max_length=12),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=students.models.upload_course_image, width_field='width_field'),
        ),
        migrations.AlterField(
            model_name='student',
            name='house',
            field=models.CharField(choices=[('GRYFFINDOR', 'Gryffindor'), ('RAVENCLAW', 'Ravenclaw'), ('HUFFLEPUFF', 'Hufflepuff'), ('SLYTHERIN', 'Slytherin')], default='GRYFFINDOR', max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=students.models.upload_student_image, width_field='width_field'),
        ),
    ]
