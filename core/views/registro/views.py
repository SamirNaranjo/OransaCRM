from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm

class Registro(View):

    def get(self, request):
        form=UserCreationForm()
        return render(request, "create_user.html", {'form':form})
        
    def post(self, request):
        pass