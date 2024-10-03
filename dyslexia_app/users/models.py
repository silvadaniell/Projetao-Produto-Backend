from django.db import models
from django.core.exceptions import ValidationError

def validate_age(value):
    if value < 5:
        raise ValidationError('A idade deve ser 5 ou maior que 5.')
    
    
class Users(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(validators=[validate_age])

    def __str__(self):
        return self.username


