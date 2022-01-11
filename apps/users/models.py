from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (
    AbstractBaseUser, 
    BaseUserManager,
    PermissionsMixin,
)

class UserManager(BaseUserManager):
    
    def _create_user(self, name, email, password, **extra_fields):
        user = self.model(
            name         = name,
            email        = self.normalize_email(email),
            **extra_fields
        )
        user.password = make_password(password)
        user.save(using = self.db)

        return user

    def create_user(self, name, email, password, **extra_fields):

        if not name:
            raise ValueError('must have user name')
        if not email:
            raise ValueError('must have user email')
        if not password:
            raise ValueError('must have user password')

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(name, email, password, **extra_fields)

    def create_superuser(self, password, name=None, email=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(name, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    name      = models.CharField(max_length=50)
    email     = models.EmailField(unique=True)
    password  = models.CharField(max_length=300)
    is_staff  = models.BooleanField(default=False)

    objects = UserManager()

    REQUIRED_FIELDS = ['name', 'password'] 
    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'users'