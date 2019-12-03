from django.db import models
from django.conf import settings
from django.utils.html import format_html

class Base_Information(models.Model):
    sub_AS = models.CharField(max_length=20, verbose_name='Субъект ГА')
    type_avia = models.CharField(max_length=20, verbose_name='Вид авиации')
    operator = models.CharField(max_length=20, verbose_name='Эксплуатант')
    execut_full_name = models.CharField(max_length=70, verbose_name='ФИО исполнителя')
    execut_post = models.CharField(max_length=70, verbose_name='Должность исполнителя')

    exten_num = models.CharField(max_length=50, verbose_name='Внутренний номер')
    edit_repotr = models.CharField(max_length=50, verbose_name='Редакция отчета')
    prepar_date = models.CharField(max_length=15, verbose_name='Дата составления')
    status_report = models.CharField(max_length=20, verbose_name='Статус отчета')
    contact = models.CharField(max_length=50, verbose_name='Контактная информация')
    zone = models.CharField(max_length=10, verbose_name='Зона')
    type_equipment = models.CharField(max_length=30, verbose_name='Тип техники')
    specialty = models.CharField(max_length=20, verbose_name='Специальность')

    def file_location(self):
        return format_html('<a href="{}">{}</a>'.format(settings.MEDIA_URL + '{}-{}.docx'.format(self.operator, self.execut_full_name), 'link'))

    def __str__(self):
        return ('Информация от пользователя')

    class Meta:
        verbose_name = 'Базовая информация'
        verbose_name_plural = 'Базовые информации'

class Docx_Save(models.Model):
    pass

