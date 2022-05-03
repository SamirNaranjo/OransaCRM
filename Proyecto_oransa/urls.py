

from django.contrib import admin
from django.urls import include, path
from core.HomePage.views import IndexView
from core.Login.views import LoginFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('', IndexView.as_view(), name='index'),
    path('login/', include('core.Login.urls')),
]
