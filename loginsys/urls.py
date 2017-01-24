from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'loesk_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login', 'loginsys.views.login'),
    url(r'^logout', 'loginsys.views.logout'),

]
