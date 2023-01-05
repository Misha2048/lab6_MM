# Generated by Django 4.1.5 on 2023-01-05 20:32

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_student_get_grants_alter_student_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='value',
            field=models.PositiveIntegerField(default=26),
        ),
        migrations.AlterField(
            model_name='student',
            name='get_grants',
            field=models.ForeignKey(default=main.models.StudentGetGrants.get_default_getgrants, on_delete=django.db.models.deletion.CASCADE, to='main.studentgetgrants'),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.ForeignKey(default=main.models.StudentStatus.get_default_status, on_delete=django.db.models.deletion.CASCADE, to='main.studentstatus'),
        ),
    ]
