from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, email, data_de_nascimento,data_de_diagnostico, altura, peso, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            data_de_nascimento=data_de_nascimento,
            data_de_diagnostico = data_de_diagnostico,
            altura = altura,
            peso = peso,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, data_de_nascimento,data_de_diagnostico, altura, peso, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            data_de_nascimento=data_de_nascimento,
            data_de_diagnostico = data_de_diagnostico,
            altura = altura,
            peso = peso,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractUser):
  
    email                        = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    data_de_nascimento           = models.DateField()
    data_de_diagnostico          = models.DateField()
    altura                       = models.FloatField()
    peso                         = models.FloatField(default=0)
    is_active                    = models.BooleanField(default=True)
    is_admin                     = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD               = 'email'
    REQUIRED_FIELDS              = ['data_de_nascimento','altura','data_de_diagnostico','peso']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
# Create your models here.
