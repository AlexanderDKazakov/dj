# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from call.models import Call, User, reason_otdel, Comment, Table_Num
from django.contrib import auth
from django.shortcuts import get_object_or_404
### For form
from .forms import NewCallForm, EditCallForm, DatePickerForm, RedirectCallForm, CommentCallForm
######## EXPORTING
from django.http import HttpResponse
import datetime
# data.csv
import csv


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
        args['top_message'] = 'Список всех звонков:'
        args['time_now'] = datetime.datetime.now()
        args['call_for_filial'] = Call.objects.filter(call_user_man_filial=args['user_filial'])
        form = DatePickerForm()
        return render(request, 'list_call.html', {'args': args, 'form': form})
    else:
        user_id = args['id']
        user = User.objects.get(pk=user_id)
        args['user_filial'] = user.profile.user_filial
        args['user_otdel'] = user.profile.user_otdel
        args['user_res'] = user.profile.user_res
        args['user_group'] = request.user.groups.values_list('name', flat=True).first()
        args['top_message'] = 'Список звонков, по которым необходимо сформировать ответ:'
        args['time_now'] = datetime.datetime.now()
        args['call_for_filial'] = Call.objects.filter(call_user_man_filial=args['user_filial']).filter(
            call_otvet=True).filter(call_user_man_otdel=args['user_otdel']).order_by('-call_date_start')
        return render(request, 'list_call.html', {'args': args})


# def call_edit(request, call_id=1):
#     args = {}
#     args['title_page'] = 'ЛОЭСК | Редактирование звонка'
#     # args['id'] = auth.get_user(request).id
#     # user_id = args['id']
#     user = User.objects.get(pk=auth.get_user(request).id)
#     args['call_edit'] = Call.objects.get(id=call_id)
#     args['call_comments'] = Comment.objects.filter(comment_call_id=call_id)
#     args['username'] = auth.get_user(request)
#     args['user_filial'] = user.profile.user_filial
#     args['user_otdel'] = user.profile.user_otdel
#     args['user_res'] = user.profile.user_res
#     args['user_group'] = request.user.groups.values_list('name', flat=True).first()
#     # TODO comment output
#     # args['call_'] = Call.objects.all()
#
#     # args['title_button'] = 'Сохранить изменения'
#     form_comment = CommentCallForm()
#     # HEADING
#     call = get_object_or_404(Call, pk=call_id)
#     if request.method == "POST":
#         form = EditCallForm(request.POST, request.FILES, instance=call)
#         form_comment = CommentCallForm(request.POST)
#         if form.is_valid():
#             call = form.save(commit=False)
#             call.save()
#             return redirect('/')
#         elif form_comment.is_valid():
#             call_comment = form_comment.save(commit=False)
#             call_comment.comment_call = Call.objects.get(id=call_id)
#             call_comment.comment_date = datetime.datetime.now()
#             # call_comment.comment_user_id = auth.get_user(request).id
#             call_comment.comment_user = user
#             call_comment.save()
#             return redirect('/call/get/%s/' % call_id)
#     else:
#         form = EditCallForm(instance=call)
#         # form_comment = CommentCallForm(initial={'comment_user': args['username']})
#     return render(request, 'call_edit.html', {'form': form,
#                                               'form_comment': form_comment,
#                                               'args': args})


def call_edit(request, call_id=1):
    args = {}
    args['title_page'] = 'ЛОЭСК | Редактирование звонка'
    # args['id'] = auth.get_user(request).id
    # user_id = args['id']
    user = User.objects.get(pk=auth.get_user(request).id)
    args['call_edit'] = Call.objects.get(id=call_id)
    args['call_comments'] = Comment.objects.filter(comment_call_id=call_id)
    args['username'] = auth.get_user(request)
    args['user_filial'] = user.profile.user_filial
    args['user_otdel'] = user.profile.user_otdel
    args['user_res'] = user.profile.user_res
    args['user_group'] = request.user.groups.values_list('name', flat=True).first()
    # TODO comment output
    # args['call_'] = Call.objects.all()

    # args['title_button'] = 'Сохранить изменения'
    form_comment = CommentCallForm()
    # HEADING
    call = get_object_or_404(Call, pk=call_id)
    if request.method == "POST":
        form = EditCallForm(request.POST, request.FILES, instance=call)
        form_comment = CommentCallForm(request.POST)
        if form.is_valid():
            call = form.save(commit=False)
            call.save()
            return redirect('/call/get/%s/' % call_id)
        elif form_comment.is_valid():
            call_comment = form_comment.save(commit=False)
            call_comment.comment_call = Call.objects.get(id=call_id)
            call_comment.comment_date = datetime.datetime.now()
            call_comment.comment_user = user
            # call_comment.comment_user = str(1)
            call_comment.save()
            return redirect('/call/get/%s/' % call_id)
    else:
        form = EditCallForm(instance=call)

    if args['user_otdel'] != None:
        form.fields['call_aim'].queryset = user.profile.user_otdel.reason_otdel_set
    return render(request, 'call_edit.html', {'form': form,
                                              'form_comment': form_comment,
                                              'args': args})


def new_call(request):
    args = {}
    args['title_page'] = 'ЛОЭСК | Новый звонок'
    # args['id'] = auth.get_user(request).id
    # user_id = args['id']
    user = User.objects.get(pk=auth.get_user(request).id)
    args['list_call'] = Call.objects.all()
    args['username'] = auth.get_user(request).username
    args['user_filial'] = user.profile.user_filial
    args['user_otdel'] = user.profile.user_otdel
    args['user_res'] = user.profile.user_res
    args['user_group'] = request.user.groups.values_list('name', flat=True).first()
    args['title_button'] = 'Добавить звонок'
    form_redirect = RedirectCallForm()
    ### HEADING
    if request.method == "POST":
        form = NewCallForm(request.POST, request.FILES)
        form_redirect = RedirectCallForm(request.POST, request.FILES)
        if form.is_valid():
            call = form.save(commit=False)
            call.save()
            return redirect('/')
        elif form_redirect.is_valid():
            call =form_redirect.save(commit=False)
            call.save()
            return redirect('/')
        else:
            return render(request, 'new_call.html', {'args': args})
    else:
        form = NewCallForm(initial={'call_user_man': args['username'],
                                    'call_user_man_filial': args['user_filial'],
                                    'call_user_man_otdel': args['user_otdel'],
                                    })
        form_redirect = RedirectCallForm(initial={'call_user_man': args['username'],
                                    'call_user_man_filial': args['user_filial'],
                                    'call_user_man_otdel': args['user_otdel'],
                                    })
    if args['user_otdel'] != None:
        form.fields['call_aim'].queryset = user.profile.user_otdel.reason_otdel_set
    return render(request, 'new_call.html', {'form': form, 'args': args, 'form_redirect': form_redirect})


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
    # ws.write(15,1, period_from)
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
            str(obj.call_date_start)[:10],
            str(obj.call_date_start)[11:19],
            '',
            '1',
        ]
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
        ws.write(row_num, 9+list_aim_call.index(str(obj.call_aim)), '1')
        ws.write(row_num, 26, '1') # call answer get at the time

    wb.save(response)
    return response


def aim_to_num(aim_call):
    Table_Num_arg = Table_Num.objects.all()
    table_num_int = (int(Table_Num_arg.filter(table_reason_id=aim_call.id)[0].table_num) - 1)
    return table_num_int


# TODO REDO export_excel_out!
#   new list ==> new output.
def export_excel_out(request):
    if request.method == "POST":
        # my_var = dict.get('data_from', False)
        data_from = request.POST.get('date_from')
        data_to = request.POST.get('date_to')
        # inp_otdel = request.POST.get('inp_otdel')
        # export_xls(request)
        import xlwt
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename=Otchet_ot_' + str(datetime.date.today()) + '.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Отчёт от' + str(datetime.date.today()))
        # 	ws.write(0, 0, 'foobar') # row, column, value
        # TABLE HEAD
        ws.write(0, 0,
                 u'Приложение N 7 к Единым стандартам качества обслуживания сетевыми организациями потребителей услуг сетевых организаций Список изменяющих документов (введено Приказом Минэнерго России от 06.04.2015 N 217)')
        ws.write(1, 0,
                 u' Информация о качестве обслуживания потребителей_______________Филиал АО "ЛОЭСК"_____________________ услуг за 2015  год (наименование сетевой организации)')
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
        list_aim_call = [
            # 'ДИСПЕТЧЕРСКАЯ',
            'Жалоба: Информация об аварийных отключениях, в том числе периодических отключениях',
            'Обращение: Информация о повреждениях энергообъектов',
            'Жалоба: Информация о повреждениях энергообъектов',
            'Жалоба: Вопросы об отклонении уровня напряжения',
            'Обращение: Вопросы по графику плановых отключений',
            'Жалоба: Вопросы по графику плановых отключений',
            'Обращение: Прочее',
            'Жалоба: Прочее',
            # 'ЦПЭС',
            'Обращение по вопросу осуществления технологического присоединения',
            'Жалоба на осуществление технологического присоединения',
            'Заявки по технологическому присоединению',
            'Заявки на заключение договора на оказание услуг по передаче электроэнергии',
            'Обращение: Прочее, связанное с технологическим присоединением',
            'Жалоба: Прочее, связанное с технологическим присоединением',
            'Заявка: Прочее, связанное с технологическим присоединением',
            # 'ПТО',
            'Коммерческие услуги',
            'Обращение: Прочее',
            'Жалоба: Прочее',
            # 'Канцелярия ЦА',
            'Информация о рассмотрении обращений, поступивших в Общество',
            'Жалоба на рассмотрение обращений, поступивших в Общество',
            'Обращение: Коммерческий учёт электрической энергии',
            'Жалоба: Коммерческий учёт электрической энергии',
            'Обращение: Качество обслуживания потребителей',
            'Жалоба: Качество обслуживания потребителей',
            'Обращение: Прочее',
            'Жалоба: Прочее',
            # 'Секретариат',
            'Обращение: Вопросы по графику плановых отключений',
            'Жалоба: Вопросы по графику плановых отключений',
            'Обращение: Прочее',
            'Жалоба: Прочее',
        ]
        Table_Num_dict = Table_Num.objects.all()

        # list_aim_call = ['Оказание услуг по передаче электрической энергии',
        #                  'Осуществление технологического присоединения',
        #                  'Коммерческий учет электрической энергии',
        #                  'Качество обслуживания потребителей',
        #                  'Техническое обслуживание электросетевых объектов',
        #                  'Прочее',
        #                  '(Жалоба) Качество услуг по передаче электрической энергии',
        #                  '(Жалоба) Качество электрической энергии',
        #                  '(Жалоба) Осуществление технологического присоединения',
        #                  '(Жалоба) Коммерческий учет электрической энергии',
        #                  '(Жалоба) Качество обслуживания потребителей',
        #                  '(Жалоба) Техническое обслуживание электросетевых объектов',
        #                  '(Жалоба) Прочее',
        #                  '(Заявка) По технологическому присоединению',
        #                  '(Заявка) Заключение договора на оказание услуг по передаче электроэнергии',
        #                  '(Заявка) Организация коммерческого учета электроэнергии',
        #                  '(Заявка) Прочее',
        #                  ]
        # END Lists
        # font_style = xlwt.XFStyle()
        # font_style.font.bold = True

        for index, value in enumerate(row_list):
            ws.write(5, index, str(value))
        for i in range(0, 31):
            ws.write(6, i, str(i + 1))
        # ws.write(15,1, period_from)
        # args = {}
        # args['id'] = auth.get_user(request).id
        # user_id = args['id']
        user = User.objects.get(pk=auth.get_user(request).id)
        # args['user_filial'] = user.profile.user_filial
        # user_filial = args['user_filial']
        queryset = Call.objects.filter(call_user_man_filial=user.profile.user_filial)
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
        # datetime.date(year, month, day)
        year_f = int(data_from[6:])
        day_f = int(data_from[:2])
        month_f = int(data_from[3:5])
        print(year_f,month_f,day_f)
        data_from_comparible=datetime.date(year_f, month_f, day_f)
        year_t = int(data_to[6:])
        day_t = int(data_to[:2])
        month_t = int(data_to[3:5])
        data_to_comparible=datetime.date(year_t, month_t, day_t)
        # data_to_comparible=datetime.date(data_to[6:], data_to[:2], data_to[3:5])
        for obj in queryset:
            #  DATA FOR COMPARISON DATE
            day_c = int(str(obj.call_date_start)[8:10])
            month_c = int(str(obj.call_date_start)[5:7])
            year_c = int(str(obj.call_date_start)[:4])
            data_current = datetime.date(year_c, month_c, day_c)
            # END DATA
            if (data_current <= data_to_comparible) and (data_current >= data_from_comparible):
                row_num += 1
                count_number += 1
                row = [
                    count_number,
                    row_list[1],
                    str(obj.call_date_start)[8:10]+'/'+str(obj.call_date_start)[5:7]+'/'+str(obj.call_date_start)[:4], # dd/mm/yyyy
                    str(obj.call_date_start)[11:19],
                    '',
                    '1',
                ]
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)
                # ws.write(row_num, 9 + list_aim_call.index(str(obj.call_aim)), '1')
                ws.write(row_num, aim_to_num(obj.call_aim), '1')
                ws.write(row_num, 26, '1')  # call answer get at the time

        # ws.write(30,1, data_from)
        # ws.write(31,1, int(data_from[:2])) # dd
        # ws.write(32,1, int(data_from[3:5])) # mm
        # ws.write(33, 1, int(data_from[6:]))  # yyyy
        # ws.write(30,2, data_to)
        # ws.write(30,3, inp_otdel)
        wb.save(response)
        return response