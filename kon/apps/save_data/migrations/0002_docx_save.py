# Generated by Django 2.2.6 on 2019-12-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('save_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docx_Save',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docx', models.FileField(blank=True, upload_to='docx')),
            ],
            options={
                'verbose_name': 'Файл док',
                'verbose_name_plural': 'Файлы док',
            },
        ),
    ]
