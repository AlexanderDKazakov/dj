from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
### SIGNALS
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

class Aim_call(models.Model):
    class Meta:
        db_table = "aim_call"
    ac_name      = models.CharField(max_length=200, verbose_name='Цель звонка', blank=True, null=True)

    def __str__(self):
        # return 'aim_call: {}'.format(self.ac_name)
        return self.ac_name


class legalEntity(models.Model):
    class Meta:
        db_table = "abonent"
    le_type      = models.CharField(max_length=200, verbose_name='Тип лица (Физический/Юридический)', blank=True, null=True)

    def __str__(self):
        return self.le_type


class Res(models.Model):
    class Meta:
        db_table = "res"
    res_name      = models.CharField(max_length=200, verbose_name='РЭС', blank=True, null=True)

    def __str__(self):
        return self.res_name


class Otdel(models.Model):
    class Meta:
        db_table = "otdel"
    otdel_name        = models.CharField(max_length=200, verbose_name='Отдел', blank=True, null=True)

    def __str__(self):
        return self.otdel_name


class reason_otdel(models.Model):
    class Meta:
        db_table = "reason_otdel"
    otdel_id = models.ForeignKey(Otdel, on_delete=models.CASCADE)
    rc_name = models.CharField(max_length=200, verbose_name='Причина обращения:', blank=True, null=True)

    def __str__(self):
        return self.rc_name

class Table_Num(models.Model):
    class Meta:
        db_table = "table_num"

    table_name = models.CharField(max_length=350, verbose_name='Название стобца:', blank=True, null=True)
    table_reason = models.ForeignKey(reason_otdel, on_delete=models.CASCADE)
    table_num = models.CharField(max_length=100, verbose_name='Номер столбца:', blank=True, null=True)

    def __str__(self):
        return self.table_name

class Filial(models.Model):
    class Meta:
        db_table = "filial"
    filial_name      = models.CharField(max_length=200, verbose_name='Филиал', blank=True, null=True)

    def __str__(self):
        return self.filial_name


class ActOperator(models.Model):
    class Meta:
        db_table = "actoperator"
    actoperator_name = models.CharField(max_length=200, verbose_name='Действия оператора', blank=True, null=True)

    def __str__(self):
        return self.actoperator_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_otchestvo = models.CharField(verbose_name='Отчество', max_length=20)
    user_filial = models.ForeignKey(Filial, null=True, blank=True, verbose_name='Филиал')
    user_res = models.ForeignKey(Res, null=True, blank=True, verbose_name='РЭС')
    user_otdel = models.ForeignKey(Otdel, null=True, blank=True, verbose_name='Отдел')
    user_numphone = models.CharField(verbose_name='Номер телефона', max_length=20)
    # user_name = models.CharField(verbose_name='Имя', max_length=20)

# TODO GET INFO ABOUT USER AND SEND IT TO ADMIN PANEL
#     def getfirsname(self):
#         full_name = User.get_short_name()
#         return full_name

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Call(models.Model):
    class Meta:
        db_table = "call"
        ordering = ['-call_date_start']
    call_title      = models.CharField(max_length=200, verbose_name='Заявитель:')
    call_entite     = models.ForeignKey(legalEntity, verbose_name='Лицо:', default=id(1), blank=True)
    call_document   = models.FileField(verbose_name='Приложить документ:',upload_to='documents/%Y/%m/%d/', blank=True, null=True)
    call_otvet      = models.BooleanField(default=False, verbose_name='Необходимо подготовить ответ:')
    call_aim        = models.ForeignKey(reason_otdel, verbose_name='Причина обращения:', default=id(1), blank=True, null=True)
    call_aim_detail = models.CharField(max_length=300, verbose_name='Детали звонка:', blank=True, null=True)
    call_act        = models.ForeignKey(ActOperator, verbose_name='Действие оператора:', default=id(1))
    call_kontact    = models.CharField(max_length=150, verbose_name='Контакты для связи:', blank=True, null=True)
    call_date_start = models.DateTimeField(default=timezone.now, verbose_name='Время открытия звонка:')
    call_date_end   = models.DateTimeField(verbose_name='Время закрытия звонка:', blank=True, null=True)
    #### INSERTING DATA FROM FORM(INITIAL)
    call_user_man        = models.CharField(max_length=50, verbose_name='Логин оператора:', blank=True, null=True)
    # call_user_man_filial = models.CharField(max_length=100, verbose_name='Филиал оператора:', blank=True, null=True)
    call_user_man_filial = models.ForeignKey(Filial, verbose_name='Филиал оператора:', blank=True, null=True)
    # call_user_man_otdel  = models.CharField(max_length=100, verbose_name='Отдел оператора', blank=True, null=True)
    call_user_man_otdel  = models.ForeignKey(Otdel, verbose_name='Отдел оператора', blank=True, null=True)

    def calliswhat(self):
        now = timezone.now()
        if (now - self.call_date_start) > datetime.timedelta(6, 100, 100):
            return True

    def __str__(self):
        return self.call_title


class Comment(models.Model):
    class Meta:
        db_table = "comments"

    comment_text = models.TextField(verbose_name="Текст комментария:")
    comment_date = models.DateTimeField(default=timezone.now, verbose_name='Время комментария:')
    comment_user = models.ForeignKey(User, blank=True, null=True)
    # NEED TO THINK AGAIN
    # comment_user_man = models.CharField(max_length=200, verbose_name="Логин", blank=True, null=True)
    comment_call = models.ForeignKey(Call)

    def __str__(self):
        return self.comment_text
