# Generated by Django 2.2.6 on 2019-12-02 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('save_data', '0003_auto_20191202_1616'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='docx_save',
            options={},
        ),
        migrations.RemoveField(
            model_name='docx_save',
            name='docx',
        ),
    ]
