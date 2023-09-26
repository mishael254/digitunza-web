from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields.related import ForeignKey, OneToOneField

# from django.contrib.gis.db import models as gismodels
# from django.contrib.gis.geos import Point



class User(AbstractBaseUser):
    ROLE_CHOICE = (
        ('projectManager', 'projectManager'),
        ('partner', 'partner'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=14, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)
    # required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
     
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    

