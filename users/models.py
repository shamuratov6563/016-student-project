from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core import validators
from django.utils.deconstruct import deconstructible
from django.contrib.auth.hashers import make_password





class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone_number, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not phone_number:
            raise ValueError("Telefon raqam kiritilishi shart")
        email = self.normalize_email(email)
        user = self.model(phone_number=phone_number, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, email, password, **extra_fields)

    def create_superuser(self, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone_number, email, password, **extra_fields)


@deconstructible
class UnicodePhoneValidator(validators.RegexValidator):
    regex = r"\+998[0-9]{9}"
    message = "Kiritilgan telefon raqami noto'g'ri"
    flags = 0



class User(AbstractUser):
    phone_validator = UnicodePhoneValidator()

    username = None
    phone_number = models.CharField(
        unique=True, 
        max_length=13,
        validators=[phone_validator])
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = "phone_number"
    


    
