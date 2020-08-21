# Generated by Django 3.0.8 on 2020-08-05 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pervez', '0005_notes_notesfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_desc', models.CharField(max_length=200, null=True)),
                ('question', models.FileField(blank=True, null=True, upload_to='')),
                ('answer_desc', models.CharField(max_length=200, null=True)),
                ('answers', models.FileField(blank=True, null=True, upload_to='')),
                ('clss', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pervez.Cls')),
                ('sub', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pervez.Subject')),
            ],
        ),
    ]