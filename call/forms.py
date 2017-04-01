# -*- coding: utf-8 -*-
from django import forms
# from django.conf import settings
# from django import utils
# from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
# from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
# from django.forms.extras.widgets import SelectDateWidget

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from call.models import Call
from django.contrib import auth

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
# from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
#
#
# AIM_CALL = (
#     ('Оказание услуг по передаче электрической энергии', 'Оказание услуг по передаче электрической энергии'),
#     ('Осуществление технологического присоединения', 'Осуществление технологического присоединения'),
#     ('Коммерческий учет электрической энергии', 'Коммерческий учет электрической энергии'),
#     ('Качество обслуживания потребителей', 'Качество обслуживания потребителей'),
#     ('Техническое обслуживание электросетевых объектов', 'Техническое обслуживание электросетевых объектов')
# )
#
#
# # ABONENT = (
# #     ('Физическое лицо', 'Физическое лицо'),
# #     ('Юридическое лицо', 'Юридическое лицо')
# # )
#
# ABONENT = (('f', 'Физическое лицо'), ('u', 'Юридическое лицо'))
#
# class NewCallForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(NewCallForm, self).__init__(*args, **kwargs)
#         instance = getattr(self, 'instance', None)
#         if not (instance and instance.pk):
#             self.fields['call_user_man'].widget.attrs['readonly'] = True
#
#     def clean_call_user_man(self):
#         instance = getattr(self, 'instance', None)
#         if instance and instance.pk:
#             return instance.call_user_man
#         else:
#             return self.cleaned_data['call_user_man']
#
#
#     class Meta:
#         model = Call
#         fields = (
#             'call_entite',
#             'call_title',
#             'call_aim',
#             'call_otvet',
#             'call_date_start',
#             # 'call_user',
#             'call_user_man',
#         )
########################################

# def useriswho(self):
#     select_items_aim = None
#     if Profile.user_otdel == "Диспетчерская":
#         select_items_aim =
#     elif Profile.user_otdel == "ЦПЭС":
#         select_items_aim = Call.models.ForeignKey(reason_call_operator_CPES, verbose_name='Цель звонка:',
#                                              default=id(1), blank=True, null=True)
#     elif Profile.user_otdel == "ПТО":
#         select_items_aim = models.ForeignKey(reason_call_operator_PTO, verbose_name='Цель звонка:',
#                                              default=id(1), blank=True, null=True)
#     elif Profile.user_otdel == "Канцелярия ЦА":
#         select_items_aim = models.ForeignKey(reason_call_operator_CA, verbose_name='Цель звонка:',
#                                              default=id(1), blank=True, null=True)
#     elif Profile.user_otdel == "Секретариат":
#         select_items_aim = models.ForeignKey(reason_call_operator_secretar, verbose_name='Цель звонка:',
#                                              default=id(1), blank=True, null=True)
#     return select_items_aim
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
        Field('call_kontact', placeholder='Контакты для связи: +7 (XXX) XXX XX XX'),
        Field('call_document'),
        Field('call_act'),
        Field('call_date_start', readonly=True, style='display: none;'),
        Field('call_user_man', readonly=True, style='display: none;'),
        Field('call_user_man_filial', readonly=True, style='display: none;'),
        Field('call_user_man_otdel', readonly=True, style='display: none;'),
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

# class QueryRequest(forms.Form):
#     text_input = forms.CharField()

    # textarea = forms.CharField(
    #     widget = forms.Textarea(),
    # )

    # radio_buttons = forms.ChoiceField(
    #     choices = (
    #         ('option_one', "Option one is this and that be sure to include why it's great"),
    #         ('option_two', "Option two can is something else and selecting it will deselect option one")
    #     ),
    #     widget = forms.RadioSelect,
    #     initial = 'option_two',
    # )

    # checkboxes = forms.MultipleChoiceField(
    #     choices = (
    #         ('option_one', "Option one is this and that be sure to include why it's great"),
    #         ('option_two', 'Option two can also be checked and included in form results'),
    #         ('option_three', 'Option three can yes, you guessed it also be checked and included in form results')
    #     ),
    #     initial = 'option_one',
    #     widget = forms.CheckboxSelectMultiple,
    #     help_text = "<strong>Note:</strong> Labels surround all the options for much larger click areas and a more usable form.",
    # )

    # appended_text = forms.CharField(
    #     help_text = "Here's more help text"
    # )
    #
    ## Uni-form
    # helper = FormHelper()
    # helper.form_class = 'form-horizontal'
    # helper.layout = Layout(
    #     Field('text_input', css_class='input-xlarge'),
    #     Field('textarea', rows="3", css_class='input-xlarge'),
    #     'radio_buttons',
    #     Field('checkboxes', style="background: #FAFAFA; padding: 10px;"),
    #     AppendedText('appended_text', '.00'),
    #     PrependedText('prepended_text', '<input type="checkbox" checked="checked" value="" id="" name="">', active=True),
    #     PrependedText('prepended_text_two', '@'),
    #     'multicolon_select',
    #     FormActions(
    #         Submit('save_changes', 'Save changes', css_class="btn-primary"),
    #         Submit('cancel', 'Cancel'),
    #     )
    # )
# class SearchFilterForm(forms.Form):
#     location = forms.ChoiceField(widget=forms.Select(), choices='',required=False)
#     type = forms.ChoiceField(widget=forms.Select(), choices='',required=False)
#     fromdate = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'dd/mm/yyyy','class':'datefield','readonly':'readonly'}))
#     todate = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'dd/mm/yyyy','class':'datefield','readonly':'readonly'}))
#     search_keyword = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Keyword Search','class':'keyword-search'}))


class EditCallForm(forms.ModelForm):
    class Meta:
        model = Call
        widgets = {
            # Use localization and bootstrap 3
            'call_date_end': DateTimeWidget(attrs={'id': "id_call_date_end"}, usel10n=True)
        }
        fields = [
            'call_title',
            # 'call_entite',
            # 'call_aim',
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
        # Field('call_aim', readonly=True),
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
            Submit('submit', 'Cохранить', css_class='btn btn-success btn-lg'),
            Button('cancel', 'Назад', css_class='btn btn-default btn-lg', onclick='history.go(-1);')
        )
    )
    def __init__(self, *args, **kwargs):
        super(EditCallForm, self).__init__(*args, **kwargs)

        # self.fields['call_entite'].disable
        # self.fields['call_entite'].widget = forms.CheckboxInput(attrs={'readonly': True})
        ###
        # self.fields['call_aim'] = forms.ChoiceField(widget=forms.Select(attrs={'disabled': 'disabled'}))
        # self.fields['call_aim'].label = 'Цель звонка:'
        ###
        # self.fields['call_entite'].widget.attrs['readonly'] = True
        self.fields['call_kontact'].label = ''
        self.fields['call_date_start'].label = ''
        self.fields['call_user_man'].label = ''
        self.fields['call_user_man_filial'].label = ''
        self.fields['call_user_man_otdel'].label = ''
        self.fields['call_otvet'].label = 'Необходимо подготовить ответ'


        # self.fields['call_kontact'].style = 'display : none;'


class datepicker(forms.Form):
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
        super(datepicker, self).__init__(*args, **kwargs)

        self.fields['date_from'].label = 'С'
        self.fields['date_to'].label = 'ПО'

