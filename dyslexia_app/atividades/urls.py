from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'atividades', views.AtividadesVewSet)

urlpatterns = [
    path('', include(router.urls)),
]
