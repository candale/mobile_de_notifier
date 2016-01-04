from django.shortcuts import render, render_to_response
from django.views.generic.base import View
from django.template import RequestContext


class LoginView(View):

    http_methods_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        return render_to_response(
            'login.html', context_instance=RequestContext(request))
