# Generated by Django 3.0.8 on 2020-08-05 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pervez', '0004_remove_subject_clas'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='notesfile',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
