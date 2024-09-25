from rest_framework import serializers
from .models import Users

class UsersCadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'age']
