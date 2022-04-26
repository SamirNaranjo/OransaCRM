

from django.contrib import admin
from django.urls import include, path
from core.HomePage.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('', IndexView.as_view()),
]
