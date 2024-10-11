from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('atividades.urls')),
    path('api/', include('historias.urls')),
    path('api/', include('historico_atividade.urls')),
    path('api/', include('relatorios.urls')),

]
