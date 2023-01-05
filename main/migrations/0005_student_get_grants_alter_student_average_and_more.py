# Generated by Django 4.1.5 on 2023-01-05 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_student_average_student_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='get_grants',
            field=models.CharField(default='No', max_length=3),
        ),
        migrations.AlterField(
            model_name='student',
            name='average',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
