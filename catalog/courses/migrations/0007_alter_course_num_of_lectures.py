# Generated by Django 3.2.1 on 2021-05-04 18:34

import courses.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_course_num_of_lectures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='num_of_lectures',
            field=models.SmallIntegerField(validators=[courses.models.validate_positive], verbose_name='Number of lectures'),
        ),
    ]
