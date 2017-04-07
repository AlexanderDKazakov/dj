# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from call.models import Call, Otdel, Comment
from django.contrib import auth

from datetimewidget.widgets import DateTimeWidget
from datetimewidget.widgets import DateWidget# DateTimeWidget, TimeWidget


class NewCallForm(forms.ModelForm):
    class Meta:
        model = Call

        fields = ['call_title',
                  'call_entite',
                  'call_aim',
                  'call_aim_detail',
                  'call_otvet',
                  'call_document',
                  'call_kontact',
                  "call_date_start",
                  'call_user_man',
                  'call_act',
                  'call_user_man_filial',
                  'call_user_man_otdel',
                  ]
    # Uni-form

    helper = FormHelper()
    # helper.label_class = 'label label-warning'  # this css class attribute will be added to all of the labels in your form. For instance, the "Username: " label will have 'col-md-3'
    helper.field_class = 'form-group'  # this css class attribute will be added to all of the input fields in your form. For isntance, the input text box for "Username" will have 'col-md-9'
    helper.form_method = 'post'
    helper.layout = Layout(
        Field('call_entite', required=True),
        Field('call_title', placeholder='ФИО Абонента/Название организации', required=True),
        Field('call_aim'),
        Field('call_aim_detail', placeholder='Опишите кратко детали', required=True),
        Field('call_otvet', initial=False),
        Field('call_kontact', placeholder='Контакты для связи: +7 (XXX) XXX XX XX', ),
        # Field('call_kontact', placeholder='Контакты для связи: +7 (XXX) XXX XX XX', ),
        Field('call_document'),
        Field('call_act'),
        Field('call_date_start',      readonly=True, style='display: none;'),
        Field('call_user_man',        readonly=True, style='display: none;'),
        Field('call_user_man_filial', readonly=True, style='display: none;'),
        Field('call_user_man_otdel',  readonly=True, style='display: none;'),
        FormActions(
            Submit('submit', 'Cохранить', css_class='btn btn-success btn-lg'),
            Button('cancel', 'Назад', css_class='btn btn-default btn-lg', onclick='history.go(-1);')
        )
    )
    def __init__(self, *args, **kwargs):
        super(NewCallForm, self).__init__(*args, **kwargs)

        # self.fields['call_entite'].required = True
        # self.fields['call_title'].required = True
        self.fields['call_kontact'].label = ''
        self.fields['call_date_start'].label = ''
        self.fields['call_user_man'].label = ''
        self.fields['call_user_man_filial'].label = ''
        self.fields['call_user_man_otdel'].label = ''
        self.fields['call_otvet'].label = 'Необходимо подготовить ответ'


        # self.fields['call_kontact'].style = 'display : none;'


class EditCallForm(forms.ModelForm):
    class Meta:
        model = Call
        fields = [
            'call_title',
            # 'call_entite',
            'call_aim',
            'call_aim_detail',
            'call_otvet',
            'call_document',
            'call_kontact',
            'call_date_start',
            'call_date_end',
            'call_user_man',
            'call_act',
            'call_user_man_filial',
            'call_user_man_otdel',
            ]

        widgets = {
        # Use localization and bootstrap 3
        'call_date_end': DateTimeWidget(attrs={'id': "id_call_date_end"}, usel10n=True)
        }

    # Uni-form

    helper = FormHelper()
    # helper.label_class = 'label label-warning'  # this css class attribute will be added to all of the labels in your form. For instance, the "Username: " label will have 'col-md-3'
    helper.field_class = 'form-group'  # this css class attribute will be added to all of the input fields in your form. For isntance, the input text box for "Username" will have 'col-md-9'
    helper.form_method = 'post'
    helper.html5_required = True
    # html5_required = False
    helper.layout = Layout(
        # Field('call_entite', readonly=True),
        Field('call_title', placeholder='ФИО Абонента/Название организации', readonly=True),
        Field('call_aim'),
        Field('call_aim_detail', readonly=True),
        Field('call_date_end'),
        Field('call_otvet'),
        Field('call_kontact', placeholder='Контакты для связи: +7 (XXX) XXX XX XX'),
        Field('call_document'),
        Field('call_act'),
        Field('call_date_start', readonly=True, style='display: none;'),
        Field('call_user_man', readonly=True, style='display: none;'),
        Field('call_user_man_filial', readonly=True, style='display: none;'),
        Field('call_user_man_otdel', readonly=True, style='display: none;'),
        FormActions(
            Submit('submit', 'Cохранить изменения', css_class='btn btn-success btn-lg'),
            Button('cancel', 'Назад', css_class='btn btn-default btn-lg', onclick='history.go(-1);')
        )
    )
    def __init__(self, *args, **kwargs):
        super(EditCallForm, self).__init__(*args, **kwargs)

        self.fields['call_kontact'].label = ''
        self.fields['call_date_start'].label = ''
        self.fields['call_user_man'].label = ''
        self.fields['call_user_man_filial'].label = ''
        self.fields['call_user_man_otdel'].label = ''
        self.fields['call_otvet'].label = 'Необходимо подготовить ответ'


class CommentCallForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'comment_text',
            ]

    # Uni-form
    helper = FormHelper()
    # helper.label_class = 'label label-warning'  # this css class attribute will be added to all of the labels in your form. For instance, the "Username: " label will have 'col-md-3'
    helper.field_class = 'form-group'  # this css class attribute will be added to all of the input fields in your form. For isntance, the input text box for "Username" will have 'col-md-9'
    helper.form_method = 'post'
    helper.layout = Layout(
        Field('comment_text', placeholder='Введите комментарии'),
        # Field('comment_user', readonly=True, style='display: none;'),

        FormActions(
            Submit('submit', 'Добавить комментарий', css_class='btn btn-info btn-md'),
        )
    )
    def __init__(self, *args, **kwargs):
        super(CommentCallForm, self).__init__(*args, **kwargs)

        # self.fields['comment_text'].label = ''


class DatePickerForm(forms.Form):
    date_from = forms.DateField(widget=DateWidget(usel10n=True))
    date_to = forms.DateField(widget=DateWidget(usel10n=True))


    helper = FormHelper()
    helper.field_class = 'col-sm-6'
    # helper.label_class = 'label label-warning'  # this css class attribute will be added to all of the labels in your form. For instance, the "Username: " label will have 'col-md-3'
    helper.field_class = 'form-group'  # this css class attribute will be added to all of the input fields in your form. For isntance, the input text box for "Username" will have 'col-md-9'
    helper.form_method = 'post'
    helper.form_action = 'export_excel_out/'
    helper.add_input(Submit('submit', 'Подготовить отчёт', css_class='btn btn-success btn-lg '))

    def __init__(self, *args, **kwargs):
        super(DatePickerForm, self).__init__(*args, **kwargs)
        self.fields['date_from'].label = 'С'
        self.fields['date_to'].label = 'ПО'


class RedirectCallForm(forms.ModelForm):
    class Meta:
        model = Call
        fields = ['call_title',
                  'call_entite',
                  'call_aim',
                  'call_aim_detail',
                  'call_otvet',
                  # 'call_document',
                  'call_kontact',
                  "call_date_start",
                  'call_user_man',
                  'call_act',
                  'call_user_man_filial',
                  'call_user_man_otdel',
                  ]
        # model = Otdel
        # fields = ['otdel_name']

    # date_from = forms.DateField(widget=DateWidget(usel10n=True))
    # date_to = forms.DateField(widget=DateWidget(usel10n=True))

    helper = FormHelper()
    # helper.label_class = 'label label-warning'  # this css class attribute will be added to all of the labels in your form. For instance, the "Username: " label will have 'col-md-3'
    helper.field_class = 'form-group'  # this css class attribute will be added to all of the input fields in your form. For isntance, the input text box for "Username" will have 'col-md-9'
    helper.form_method = 'post'

    helper.layout = Layout(
        Field('call_entite', required=True),
        Field('call_title', placeholder='ФИО Абонента/Название организации', required=True),
        Field('call_aim'),
        Field('call_aim_detail', placeholder='Опишите кратко детали', required=True),
        Field('call_user_man_filial'),
        Field('call_user_man_otdel'),
        Field('call_act'),
        Field('call_otvet', id='id_call_otvet_redirect'),
        Field('call_kontact', id='id_call_kontact_redirect', placeholder='Контакты для связи: +7 (XXX) XXX XX XX'),
        # INVISIABLE FIELDS
        Field('call_date_start', readonly=True, style='display: none;'),
        Field('call_user_man', readonly=True, style='display: none;'),
        FormActions(
            Submit('submit', 'Переадресовать звонок', css_class='btn btn-success btn-lg'),
            # Button('cancel', 'Назад', css_class='btn btn-default btn-lg', onclick='history.go(-1);')
        )
    )

    def __init__(self, *args, **kwargs):
        super(RedirectCallForm, self).__init__(*args, **kwargs)

        # self.fields['call_user_man_filial'].label = 'Укажите филиал'
        # self.fields['call_user_man_otdel'].label = 'Укажите отдел'
        self.fields['call_kontact'].label = ''
        self.fields['call_date_start'].label = ''
        self.fields['call_user_man'].label = ''
        self.fields['call_user_man_filial'].label = ''
        self.fields['call_user_man_otdel'].label = ''
        self.fields['call_otvet'].label = 'Необходимо подготовить ответ'
        self.fields['call_user_man_filial'].label = 'Укажите филиал'
        self.fields['call_user_man_otdel'].label = 'Укажите отдел'