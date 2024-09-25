from rest_framework import viewsets
from .models import Users
from .serializers import UsersCadastroSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersCadastroSerializer
