# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from call.models import Call, User
from django.contrib import auth
from django.shortcuts import get_object_or_404
### For form
from .forms import MessageForm
# from .forms import CallForm
######## EXPORTING
from django.http import HttpResponse
import datetime
# data.csv
import csv
# data.pdf
### SEARCHING TO CSV/PDF
# from .forms import SearchFilterForm
# Create your views here.


def list_call(request):
    args = {}
    args['title_page'] = 'ЛОЭСК | Главная'
    args['username'] = auth.get_user(request).username
    args['id'] = auth.get_user(request).id
    if args['id'] == None:
        return redirect('loginsys.views.login')
    elif args['username'] == 'admin' or request.user.groups.values_list('name', flat=True).first() == 'Руководитель':
        user_id = args['id']
        user = User.objects.get(pk=user_id)
        args['user_filial'] = user.profile.user_filial
        args['user_otdel'] = user.profile.user_otdel
        args['user_res'] = user.profile.user_res
        args['user_group'] = request.user.groups.values_list('name', flat=True).first()
        args['call_for_filial'] = Call.objects.filter(call_user_man_filial=args['user_filial'])
        args['top_message'] = 'Список всех звонков:'
        args['list_call'] = Call.objects.all().order_by('-call_date')
        return render(request, 'list_call.html', {'args': args})
    else:
        user_id = args['id']
        user = User.objects.get(pk=user_id)
        args['user_filial'] = user.profile.user_filial
        args['user_otdel'] = user.profile.user_otdel
        args['user_res'] = user.profile.user_res
        args['user_group'] = request.user.groups.values_list('name', flat=True).first()
        args['top_message'] = 'Список звонков по которым необходимо сформировать ответ:'
        args['call_for_filial'] = Call.objects.filter(call_user_man_filial=args['user_filial']).filter(call_otvet=True).order_by('-call_date')
        return render(request, 'list_call.html', {'args': args})


def call_edit(request, call_id=1):
    args = {}
    args['title_page'] = 'ЛОЭСК | Редактирование звонка'
    args['id'] = auth.get_user(request).id
    user_id = args['id']
    user = User.objects.get(pk=user_id)
    args['call_edit'] = Call.objects.get(id=call_id)
    args['username'] = auth.get_user(request)
    args['user_filial'] = user.profile.user_filial
    args['user_otdel'] = user.profile.user_otdel
    args['user_res'] = user.profile.user_res
    args['user_group'] = request.user.groups.values_list('name', flat=True).first()
    args['title_button'] = 'Сохранить изменения'
    # HEADING
    call = get_object_or_404(Call, pk=call_id)
    if request.method == "POST":
        form = MessageForm(request.POST, request.FILES, instance=call)
        if form.is_valid():
            call = form.save(commit=False)
            call.save()
            return redirect('/')
    else:
        form = MessageForm(instance=call)
    return render(request, 'call_edit.html', {'form': form, 'args': args})


def new_call(request):
    args = {}
    args['title_page'] = 'ЛОЭСК | Новый звонок'
    args['id'] = auth.get_user(request).id
    user_id = args['id']
    user = User.objects.get(pk=user_id)
    args['list_call'] = Call.objects.all()
    args['username'] = auth.get_user(request).username
    args['user_filial'] = user.profile.user_filial
    args['user_otdel'] = user.profile.user_otdel
    args['user_res'] = user.profile.user_res
    args['user_group'] = request.user.groups.values_list('name', flat=True).first()
    args['title_button'] = 'Добавить звонок'
    ### HEADING
    if request.method == "POST":
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            call = form.save(commit=False)
            call.save()
            return redirect('/')
    else:
        form = MessageForm(initial={'call_user_man': args['username'],
                                    'call_user_man_filial': args['user_filial'],
                                    'call_user_man_otdel': args['user_otdel'],
                                    })
    return render(request, 'new_call.html', {'form': form, 'args': args})


# def data_out_csv(request):
#     #  IT COULD WORK LIKE SEPARATION USERS...
#     # if not request.user.is_staff:
#     #     raise PermissionDenied
#     #
#     # opts = queryset.model._meta
#     # model = queryset.model
#     # Create the HttpResponse object with the appropriate CSV header.
#     response = HttpResponse(content_type='text/csv')
#     # force download.
#     response['Content-Disposition'] = 'attachment; filename="data_out.csv"'
#     # the csv writer
#     writer = csv.writer(response)
#     writer.writerow(['Приложение N 7 к Единым стандартам качества обслуживания сетевыми организациями потребителей услуг сетевых организаций Список изменяющих документов (введено Приказом Минэнерго России от 06.04.2015 N 217)'])
#     writer.writerow([' Информация о качестве обслуживания потребителей_______________Филиал АО "ЛОЭСК"_____________________ услуг за 2015  год (наименование сетевой организации)'])
#     writer.writerow([''])
#     writer.writerow([u'4.9. Информация по обращениям потребителей.'])
#     writer.writerow([' ', ' ', ' ', ' ',
#                      'Форма обращения',
#                      ' ', ' ', ' ', ' ',
#                      'Обращения'
#                      ' ', ' ', ' ', ' ', ' ', ' ',
#                      'Обращения потребителей, содержащие жалобу',
#                      ' ', ' ', ' ', ' ', ' ', ' ',
#                      'Обращения потребителей, содержащие заявку на оказание услуг',
#                      ' ',' ', ' ',
#                      'Факт получения потребителем ответа',
#                      ' ', ' ',
#                      'Мероприятия по результатам обращения',
#                      ' ', ' '])
#     writer.writerow(
#         ['N',
#          'Идентификационный номер обращения',
#          'Дата обращения',
#          'Время обращения',
#          'Очное обращение',
#          'Заочное обращение посредством телефонной связи',
#          'Заочное обращение посредством сети Интернет',
#          'Письменное обращение посредством почтовой связи',
#          'Прочее',
#          'Оказание услуг по передаче электрической энергии',
#          'Осуществление технологического присоединения',
#          'Коммерческий учет электрической энергии',
#          'Качество обслуживания потребителей',
#          'Техническое обслуживание электросетевых объектов',
#          'Прочее',
#          'Качество услуг по передаче электрической энергии',
#          'Качество электрической энергии',
#          'Осуществление технологического присоединения',
#          'Коммерческий учет электрической энергии',
#          'Качество обслуживания потребителей',
#          'Техническое обслуживание электросетевых объектов',
#          'Прочее',
#          'По технологическому присоединению',
#          'Заключение договора на оказание услуг по передаче электроэнергии',
#          'Организация коммерческого учета электроэнергии',
#          'Прочее',
#          'Заявителем был получен исчерпывающий ответ в установленные сроки',
#          'Заявителем был получен исчерпывающий ответ с нарушением сроков',
#          'Обращение оставлено без ответа',
#          'Выполненные мероприятия по результатам обращения',
#          'Планируемые мероприятия по результатам обращения'])
#     writer.writerow(
#         ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
#          '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'])
#     calls = Call.objects.all().values_list('id','call_title', 'call_date', 'call_entite', 'call_otvet', 'call_aim')
#     for call in sorted(calls):
#         # writer.writerow(call)
#         writer.writerow(
#                 [
#                     call[0],
#                     'Инд.номер',
#                     call[2],
#                     ' ', ' ',
#                     '+',
#                     ' ', ' ', ' ',
#                     '',
#                 ]
#         )
#     return response


def export_xls(request):
    import xlwt
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Otchet_ot_'+str(datetime.date.today())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Отчёт от' + str(datetime.date.today()))
    # 	ws.write(0, 0, 'foobar') # row, column, value
    # TABLE HEAD
    ws.write(0, 0, u'Приложение N 7 к Единым стандартам качества обслуживания сетевыми организациями потребителей услуг сетевых организаций Список изменяющих документов (введено Приказом Минэнерго России от 06.04.2015 N 217)')
    ws.write(1, 0, u' Информация о качестве обслуживания потребителей_______________Филиал АО "ЛОЭСК"_____________________ услуг за 2015  год (наименование сетевой организации)')
    ws.write(3, 0, u'4.9. Информация по обращениям потребителей.')
    ws.write(4, 4, u'Форма обращения')
    ws.write(4, 9, u'Обращения')
    ws.write(4, 15, u'Обращения потребителей, содержащие жалобу')
    ws.write(4, 22, u'Обращения потребителей, содержащие заявку на оказание услуг')
    ws.write(4, 26, u'Факт получения потребителем ответа')
    ws.write(4, 29, u'Мероприятия по результатам обращения')
    row_list = [u'N',
                u'Идентификационный номер обращения',
                u'Дата обращения',
                u'Время обращения',
                u'Очное обращение',
                u'Заочное обращение посредством телефонной связи',
                u'Заочное обращение посредством сети Интернет',
                u'Письменное обращение посредством почтовой связи',
                u'Прочее',
                u'Оказание услуг по передаче электрической энергии',
                u'Осуществление технологического присоединения',
                u'Коммерческий учет электрической энергии',
                u'Качество обслуживания потребителей',
                u'Техническое обслуживание электросетевых объектов',
                u'Прочее',
                u'Качество услуг по передаче электрической энергии',
                u'Качество электрической энергии',
                u'Осуществление технологического присоединения',
                u'Коммерческий учет электрической энергии',
                u'Качество обслуживания потребителей',
                u'Техническое обслуживание электросетевых объектов',
                u'Прочее',
                u'По технологическому присоединению',
                u'Заключение договора на оказание услуг по передаче электроэнергии',
                u'Организация коммерческого учета электроэнергии',
                u'Прочее',
                u'Заявителем был получен исчерпывающий ответ в установленные сроки',
                u'Заявителем был получен исчерпывающий ответ с нарушением сроков',
                u'Обращение оставлено без ответа',
                u'Выполненные мероприятия по результатам обращения',
                u'Планируемые мероприятия по результатам обращения']
    # END TABLE HEAD
    # Lists for FILLING TABLE
    list_aim_call = ['Оказание услуг по передаче электрической энергии',
                     'Осуществление технологического присоединения',
                     'Коммерческий учет электрической энергии',
                     'Качество обслуживания потребителей',
                     'Техническое обслуживание электросетевых объектов',
                     'Прочее',
                     '(Жалоба) Качество услуг по передаче электрической энергии',
                     '(Жалоба) Качество электрической энергии',
                     '(Жалоба) Осуществление технологического присоединения',
                     '(Жалоба) Коммерческий учет электрической энергии',
                     '(Жалоба) Качество обслуживания потребителей',
                     '(Жалоба) Техническое обслуживание электросетевых объектов',
                     '(Жалоба) Прочее',
                     '(Заявка) По технологическому присоединению',
                     '(Заявка) Заключение договора на оказание услуг по передаче электроэнергии',
                     '(Заявка) Организация коммерческого учета электроэнергии',
                     '(Заявка) Прочее',
                     ]
    # END Lists
    # font_style = xlwt.XFStyle()
    # font_style.font.bold = True

    for index, value in enumerate(row_list):
        ws.write(5, index, str(value))
    for i in range(0, 31):
        ws.write(6, i, str(i+1))

    ####### SOME TRYING
    args = {}
    args['id'] = auth.get_user(request).id
    user_id = args['id']
    user = User.objects.get(pk=user_id)
    args['user_filial'] = user.profile.user_filial
    user_filial = args['user_filial']
    queryset = Call.objects.filter(call_user_man_filial=user_filial)

    #######
    row_num = 6
    # columns = [
    #     (u"ID", 2000),
    #     (u"ФИО Абонента", 6000),
    #     (u"Причина звонка", 8000),
    # ]
    #
    # font_style = xlwt.XFStyle()
    # font_style.font.bold = True
    #
    # for col_num in range(len(columns)):
    #     ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width
        # ws.col(col_num).width = columns[col_num][1]
    #
    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1
    count_number = 0
    for obj in queryset:
        row_num += 1
        count_number += 1
        row = [
            count_number,
            row_list[1],
            str(obj.call_date)[:10],
            str(obj.call_date)[11:19],
            '',
            '1',
        ]
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
        ws.write(row_num, 9+list_aim_call.index(str(obj.call_aim)), '1')
        ws.write(row_num, 26, '1') # call answer get at the time

    wb.save(response)
    return response
########## ITS COULD BE WORKING LIKE SEARCHING...
###
# def search(request):
#     """Search reports using filters
#     """
#     user = request.user
#     report_list = []
#     searchfilter = SearchFilterForm(user)
#     reports = Report.objects.filter(user=user)
#     if request.method == 'POST':
#        if 'search' in request.POST:
#             search_keyword = request.POST.get('search_keyword') #reports filter by keywords
#             reports = reports.filter(Q(incident_description__icontains=search_keyword)|Q(incident_number__icontains=search_keyword))
#         elif 'filter' in request.POST:
#             searchfilter = SearchFilterForm(user,request.POST)
#             loc_id = request.POST.get('location')
#             type_id = request.POST.get('type')
#             start_date = request.POST.get('fromdate')
#             end_date = request.POST.get('todate')
#             reportlist = []
#             # """"""""""" #some stuff for search come here
#             # if start_date or end_date:
#             #     if start_date and not end_date:
#             #         reports = reports.filter(created_date_time__gte=start_date)
#             #     elif not start_date and end_date:
#             #         reports = reports.filter(created_date_time__lte=end_date)
#             #     elif start_date and end_date:
#             #         reports = reports.filter(created_date_time__gt=start_date,created_date_time__lt=end_date)
#     # for report in reports:
#     #   """"""  report iteration goes here
#     #     report_list.append(items)
#     # return render(request, 'incident/search.html',
#     #                {'SearchKeywordForm':searchform,})
