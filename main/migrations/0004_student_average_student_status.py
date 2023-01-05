# Generated by Django 4.1.5 on 2023-01-05 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_student_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='average',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]