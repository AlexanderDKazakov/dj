from django.contrib import admin
from call.models import Call, Profile

class CallAdmin(admin.ModelAdmin):
    list_filter = ['call_date']
# Register your models here.

admin.site.register(Call, CallAdmin)
admin.site.register(Profile)