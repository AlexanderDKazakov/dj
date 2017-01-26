from django.contrib import admin
from call.models import Call, Profile, Filial, legalEntity, Aim_call, Res, Otdel, ActOperator
###
# class CallAdmin(admin.ModelAdmin):
#     list_filter = ['call_date']
# Register your models here.
# class TaskAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', etc. etc]
#
# admin.site.register(Task, TaskAdmin)

class CallAdmin(admin.ModelAdmin):

    list_filter = ['call_entite',
                   'call_date',
                   'call_user_man',
                   'call_user_man_filial',
                   'call_user_man_otdel',
                   ]
    list_display = ['id',
                    'call_title',
                    'call_otvet',
                    'call_date',
                    ]
    # list_editable = ['id']

admin.site.register(Call, CallAdmin)
admin.site.register(Profile)
admin.site.register(Filial)
admin.site.register(legalEntity)
admin.site.register(Aim_call)
admin.site.register(Res)
admin.site.register(Otdel)
admin.site.register(ActOperator)
