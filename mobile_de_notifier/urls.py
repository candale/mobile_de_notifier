from django.conf.urls import url
from django.contrib import admin
from cars import views as cars_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'login/$', cars_views.LoginView.as_view()),
]
