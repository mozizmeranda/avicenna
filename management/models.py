from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
from datetime import date
from django.contrib.auth.models import AbstractUser, PermissionsMixin


# Create your models here.


class User(AbstractUser, PermissionsMixin):
    class TypeChoices(models.TextChoices):
        doctor = "doctor"
        patient = "patient"
        admin = "admin"

    avatar = models.ImageField(verbose_name="Avatar", upload_to="images/avatars/")
    number = models.CharField(verbose_name="Number", max_length=20, unique=True)

    birth_date = models.DateField(verbose_name="Birth date", default=date(2000, 1, 1), blank=True)

    first_name = models.CharField(verbose_name="Surname", max_length=50)
    last_name = models.CharField(verbose_name="Name", max_length=50)
    patronymic = models.CharField(verbose_name="Отчество", max_length=50, null=True, default=None)

    email = None
    password = models.CharField(verbose_name="password", max_length=50)

    created_at = models.DateTimeField(verbose_name="Created Time", auto_now_add=True)

    user_type = models.CharField(verbose_name="Type of User", choices=TypeChoices.choices, default=TypeChoices.patient,
                                 max_length=20)
    USERNAME_FIELD = "number"
    REQUIRED_FIELDS = []

    groups = None
    user_permissions = None
    is_active = None
    date_joined = None
    is_staff = None
    is_superuser = None
    last_login = None

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Doctor(models.Model):
    user = models.ForeignKey(to=User, verbose_name="User", on_delete=models.CASCADE, related_name="user_doctor",
                             max_length=255)
    bachelor_document = models.ImageField(verbose_name="Bachelory documents", upload_to="images/educations/")
    master_document = models.ImageField(verbose_name="Master documents", null=True, blank=True,
                                        upload_to="images/educations/")
    experience = models.IntegerField(verbose_name="experience")

    description = models.TextField(verbose_name="Description", blank=True)

    schedule = models.CharField(verbose_name="Schedule time", max_length=20)

    rating = models.DecimalField(verbose_name="Rating of doctor", max_digits=3, decimal_places=2)

    is_verified = models.BooleanField(verbose_name="Is real doc?", default=False)

    def __str__(self):
        return f"{self.user.number}"

    class Meta:
        verbose_name = "doctor"
        verbose_name_plural = "doctors"


class Patient(User):

    class Meta:
        verbose_name = "patient"
        verbose_name_plural = "patients"


# class MedCard(User):
#     title = models.CharField(verbose_name="Title", max_length=100)
#     description = models.TextField(verbose_name="Description")
#
#     file_1 = models.FileField(verbose_name="Random File 1", upload_to="images/files/")
#     file_2 = models.FileField(verbose_name="Random File 2", upload_to="images/files/", null=True, default=True)
#     file_3 = models.FileField(verbose_name="Random File 3", upload_to="images/files/", null=True, default=True)
#
#     class Meta:
#         verbose_name = "MedCard"
#         verbose_name_plural = "MedCards"
