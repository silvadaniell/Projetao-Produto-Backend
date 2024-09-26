from rest_framework import serializers
from .models import Users

class UsersCadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'age']
        
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def update(self, instance, validated_data):
    # Atualiza a instância com os dados validados
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.age = validated_data.get('age', instance.age)

        # Atualiza a senha se fornecida
        password = validated_data.get('password')
        if password:
            instance.password = password 

        instance.save()
        return instance   
