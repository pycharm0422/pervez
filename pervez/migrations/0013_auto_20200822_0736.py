# Generated by Django 3.1 on 2020-08-22 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pervez', '0012_subtopic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lectures',
            name='sub',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pervez.subject'),
        ),
    ]