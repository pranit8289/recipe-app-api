from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)


class Usermanager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """ creates and saves a new user """
        if not email:
            raise ValueError("Users must have an email address")
        obj = self.model(email=self.normalize_email(email), **extra_fields)
        obj.set_password(password)
        obj.save(using=self._db)
        return obj

    def create_superuser(self, email, password):
        """ creates new superuser """
        obj = self.create_user(email, password)
        obj.is_staff = True
        obj.is_superuser = True
        obj.save(using=self._db)
        return obj


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user model which supports using email rather than username """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = Usermanager()

    USERNAME_FIELD = 'email'
