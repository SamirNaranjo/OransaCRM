from multiprocessing import context
from django.conf import Settings
from django.contrib.auth import login
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.views.generic import RedirectView, View
from django.contrib.auth.models import User
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


class Registro(View):
    
    class Meta:
        model = User
        fields = ('__all__')
        
    def get(self, request):
          form=UserCreationForm()
          return render(request, "create_user.html", {'form':form})
        
    def post(self, request):
         form=UserCreationForm(request.POST)
         
         if form.is_valid():
             usuario= form.save()
             login(request, usuario)
             return redirect('index')
         else:
             pass
