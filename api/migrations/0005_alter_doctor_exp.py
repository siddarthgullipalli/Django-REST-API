# Generated by Django 4.1.1 on 2022-09-08 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_doctor_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='exp',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
