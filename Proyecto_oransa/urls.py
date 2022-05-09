

from django.contrib import admin
from django.urls import include, path
from core.HomePage.views import IndexView
from core.Login.views import LoginFormView, Registro
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('', IndexView.as_view(), name='index'),
    path('login/', include('core.Login.urls')),
    path('registro/', Registro.as_view(), name='registro'),
    
    # path('user/', include('User.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
