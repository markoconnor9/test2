# Generated by Django 4.2.4 on 2023-10-03 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avilabilty', '0004_alter_employee_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='availability',
            field=models.ManyToManyField(to='avilabilty.shift'),
        ),
    ]