from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth.models import User
from users.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
