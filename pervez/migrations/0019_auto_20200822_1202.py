# Generated by Django 3.1 on 2020-08-22 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pervez', '0018_auto_20200822_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lectures',
            name='sub',
            field=models.ForeignKey(max_length=200, null=True, on_delete=django.db.models.deletion.CASCADE, to='pervez.subject'),
        ),
    ]
