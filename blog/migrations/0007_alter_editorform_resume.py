# Generated by Django 4.1.3 on 2022-11-21 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_editorform_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editorform',
            name='resume',
            field=models.ImageField(blank=True, null=True, upload_to='resume/'),
        ),
    ]
