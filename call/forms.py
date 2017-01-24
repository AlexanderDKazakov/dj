# -*- coding: utf-8 -*-
from django import forms
# from .models import Call
from django import forms
from django.conf import settings
from django import utils
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget
from call.models import Call, User
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
# class MessageForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(MessageForm, self).__init__(*args, **kwargs)
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
#             'call_face',
#             'call_title',
#             'call_aim',
#             'call_otvet',
#             'call_date',
#             # 'call_user',
#             'call_user_man',
#         )
########################################
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class MessageForm(forms.Form):
    class Meta:
        models = Call
    call_face = forms.ChoiceField(
        choices=(
            ('option_one', 'Физическое лицо'),
            ('option_two', 'Юридическое лицо')
        ),
        widget=forms.RadioSelect,
        initial='option_one',
        label='Абонент'
    )
    call_title = forms.CharField(label='')

    call_aim = forms.ChoiceField(
        choices=(
            ('Оказание услуг по передаче электрической энергии', 'Оказание услуг по передаче электрической энергии'),
            ('Осуществление технологического присоединения', 'Осуществление технологического присоединения'),
            ('Коммерческий учет электрической энергии', 'Коммерческий учет электрической энергии'),
            ('Качество обслуживания потребителей', 'Качество обслуживания потребителей'),
            ('Техническое обслуживание электросетевых объектов', 'Техническое обслуживание электросетевых объектов')
        ),
        widget=forms.RadioSelect,
        initial='Качество обслуживания потребителей',
        label='Причина звонка'
    )
    call_otvet = forms.BooleanField(
        label='Необходимо сформировать ответ',
        initial=False,
        required=False,
    )
    call_date = forms.DateTimeField(
        label='',
        initial=utils.timezone.now
    )
    call_user_man = forms.CharField(
        label='',
    )
    # Uni-form
    helper = FormHelper()
    # helper.form_class = 'form-vertical'
    helper.form_class = 'form'
    helper.label_class = 'label label-warning'  # this css class attribute will be added to all of the labels in your form. For instance, the "Username: " label will have 'col-md-3'
    helper.field_class = 'form-group'  # this css class attribute will be added to all of the input fields in your form. For isntance, the input text box for "Username" will have 'col-md-9'
    helper.form_method = 'post'
    helper.layout = Layout(
        Field('call_face'),
        Field('call_title', placeholder="ФИО Абонента/Название организации"),
        Field('call_aim'),
        Field('call_otvet',),
        Field('call_date', readonly=True),
        Field('call_user_man', readonly=True),
        FormActions(
            Submit('submit', u'Submit', css_class='btn btn-primary'),
            Button('cancel', 'Назад', onclick='history.go(-1);')
        )
    )

class SearchFilterForm(forms.Form):
    location = forms.ChoiceField(widget=forms.Select(), choices='',required=False)
    type = forms.ChoiceField(widget=forms.Select(), choices='',required=False)
    fromdate = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'dd/mm/yyyy','class':'datefield','readonly':'readonly'}))
    todate = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'dd/mm/yyyy','class':'datefield','readonly':'readonly'}))
    search_keyword = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Keyword Search','class':'keyword-search'}))