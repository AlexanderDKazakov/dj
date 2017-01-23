from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
### SIGNALS
from django.db.models.signals import post_save
from django.dispatch import receiver

AIM_CALL = (
    ('Оказание услуг по передаче электрической энергии', 'Оказание услуг по передаче электрической энергии'),
    ('Осуществление технологического присоединения', 'Осуществление технологического присоединения'),
    ('Коммерческий учет электрической энергии', 'Коммерческий учет электрической энергии'),
    ('Качество обслуживания потребителей', 'Качество обслуживания потребителей'),
    ('Техническое обслуживание электросетевых объектов', 'Техническое обслуживание электросетевых объектов')
)

ABONENT = (
    ('Физическое лицо', 'Физическое лицо'),
    ('Юридическое лицо', 'Юридическое лицо')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_otchestvo = models.CharField(verbose_name='Отчество', max_length=20)
    user_filial = models.CharField(verbose_name='Филиал', max_length=100)
    user_res = models.CharField(verbose_name='РЭС', max_length=100)
    user_otdel = models.CharField(verbose_name='Отдел', max_length=100)
    user_numphone = models.CharField(verbose_name='Номер телефона', max_length=20)

    def __str__(self):
        return 'Users: {}'.format(self.user.username)

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
    call_title      = models.CharField(max_length=200, verbose_name='ФИО абонента')
    call_face       = models.CharField(max_length=30, verbose_name='Абонент', choices=ABONENT, default='Физическое лицо')
    call_otvet      = models.BooleanField(default=False, verbose_name='Требуется подготовить ответ?',)
    call_aim        = models.CharField(max_length=100, verbose_name='Цель звонка', choices=AIM_CALL, default='Качество обслуживания потребителей')
    call_date       = models.DateTimeField(default=timezone.now)
    # call_user       = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    call_user_man   = models.CharField(max_length=50, verbose_name='Логин оператора:', blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return 'Calls: {}'.format(self.call_title)
