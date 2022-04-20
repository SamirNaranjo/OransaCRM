from django.shortcuts import render

from core.models import Category



# Create your views here.
def category_list(request):
    data= {
        'title':'Listado De Categorias',
        'categories': Category.objects.all()
    }

    return render(request, 'list_category.html', data)