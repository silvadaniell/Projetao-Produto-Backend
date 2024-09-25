from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'age']
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {
                'validators': [
                    UniqueValidator(queryset=User.objects.all())
                ],
            },
            'email': {
                'validators': [
                    UniqueValidator(queryset=User.objects.all())
                ],
            }
        }
    def validate_age(self, value):
        if value is not None and value <= 4:
            raise serializers.ValidationError("A idade deve ser maior ou igual a 5 anos")
        return value
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            age=validated_data.get('age', None)
        )
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.age = validated_data.get('age', instance.age)
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
