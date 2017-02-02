from django.conf.urls import include, url

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'loesk_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^call/get/(?P<call_id>[0-9]+)/$', 'call.views.call_edit'),
    url(r'^new/$', 'call.views.new_call'),
    # url(r'^data_out/$', 'call.views.export_xls'),
    # url(r'^data_out/$', 'call.views.get_data_out'),
    # url(r'^data_out_pdf$', 'call.views.data_out_pdf'),
    url(r'^export_excel_out/$','call.views.export_excel_out'),
    url(r'^$', 'call.views.list_call'),
    url(r'^login', 'loginsys.views.login'),
]
