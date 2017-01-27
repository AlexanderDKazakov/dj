from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
### SIGNALS
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    otdel_name      = models.CharField(max_length=200, verbose_name='Отдел', blank=True, null=True)

    def __str__(self):
        return self.otdel_name


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

    def __str__(self):
        # return 'Users: {}'.format(self.user.username)
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
        ordering = ['-call_date']
    call_title      = models.CharField(max_length=200, verbose_name='ФИО абонента:')
    call_entite     = models.ForeignKey(legalEntity, verbose_name='Лицо:', default=id(1))
    call_document   = models.FileField(verbose_name='Приложить документ:', blank=True, null=True)
    call_otvet      = models.BooleanField(default=False, verbose_name='Необходимо подготовить ответ:')
    call_aim        = models.ForeignKey(Aim_call, verbose_name='Цель звонка:', default=id(1))
    call_act        = models.ForeignKey(ActOperator, verbose_name='Действие оператора:', default=id(1))
    call_kontact    = models.CharField(max_length=150, verbose_name='Контакты для связи:', blank=True, null=True)
    call_date       = models.DateTimeField(default=timezone.now, verbose_name='Время звонка:')
    #### INSERTING DATA FROM FORM(INITIAL)
    call_user_man = models.CharField(max_length=50, verbose_name='Логин оператора:', blank=True, null=True)
    call_user_man_filial = models.CharField(max_length=100, verbose_name='Филиал оператора:', blank=True, null=True)
    call_user_man_otdel = models.CharField(max_length=100, verbose_name='Отдел оператора', blank=True, null=True)

    def __str__(self):
        return self.call_title
