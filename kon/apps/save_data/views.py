from django.shortcuts import render
from django.http import HttpResponse
from docxtpl import DocxTemplate
import os

from .models import *


def index(request):
    return render (request, 'save_data/index.html')

def send_data(request):
    a = Base_Information(sub_AS = request.POST['k_sub'], type_avia = request.POST['k_vid'], operator = request.POST['k_op'], execut_full_name = request.POST['k_fio'], execut_post = request.POST['k_pos'], exten_num = request.POST['k_vn_NOM'], edit_repotr = request.POST['k_redakt'], prepar_date = request.POST['k_date'], status_report = request.POST['k_stat'], contact = request.POST['k_mail_phone'], zone = request.POST['k_zone'], type_equipment = request.POST['k_vid_AT'], specialty = request.POST['k_sp'])
    a.save()
    sub_AS = request.POST['k_sub']
    type_avia = request.POST['k_vid']
    operator = request.POST['k_op']
    execut_full_name = request.POST['k_fio']
    execut_post = request.POST['k_pos']
    exten_num = request.POST['k_vn_NOM']
    edit_repotr = request.POST['k_redakt']
    prepar_date = request.POST['k_date']
    status_report = request.POST['k_stat']
    contact = request.POST['k_mail_phone']
    zone = request.POST['k_zone']
    type_equipment = request.POST['k_vid_AT']
    specialty = request.POST['k_sp']

    # создание документа об отчете
    path = (os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    file_name = '{}-{}.docx'.format(operator, execut_full_name)
    f = open(os.path.join(path, 'templates', 'report_template.docx'), 'rb')
    doc = DocxTemplate(f)
    context = {
        'sub_AS': sub_AS,
        'type_avia': type_avia,
        'operator': operator,
        'execut_full_name': execut_full_name,
        'execut_post': execut_post,
        'exten_num': exten_num,
        'edit_repotr': edit_repotr,
        'prepar_date': prepar_date,
        'status_report': status_report,
        'contact': contact,
        'zone': zone,
        'type_equipment': type_equipment,
        'specialty': specialty
    }
    doc.render(context)
    doc.save("media/{}".format(file_name))
    f.close()
    # завершение создания документа отчета

    return HttpResponse('<h1>Дякуємо за користання системою моніторінга та обробки даних експлуатації ЛА.<h1/>'
                        '<h3>Внесені Вами дані будуть оброблені та внесені до бази даних.<h3/>'
                        '<h3>Сподіваємось на подальше співробітництво.<h3/>')
