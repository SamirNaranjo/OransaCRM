from multiprocessing import context
from django.conf import Settings
from django.contrib.auth.views import LoginView,LogoutView
from django.shortcuts import redirect
from django.views.generic import RedirectView
from Proyecto_oransa.settings import LOGIN_REDIRECT_URL

class LoginFormView(LoginView):
    template_name='login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect (LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']= 'Iniciar Sesion'
        return context
