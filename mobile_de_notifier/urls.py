from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login as django_login_view
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^login/$', django_login_view, {'template_name': 'login.html'}),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
