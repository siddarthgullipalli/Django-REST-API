# Generated by Django 4.1.1 on 2022-09-08 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='Med_rec_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]