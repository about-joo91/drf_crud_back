from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,email, password=None):
        if not email:
            raise ValueError('아이디가 공란이어서 곤란합니다.')
        user = self.model(
            email = email
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_superuser(self, email, password=None):
        user =self.create_user(
            email= email,
            password= password
        )
        user.is_admin = True
        user.save(using= self._db)
        return user
    
# Create your models here.
class UserModel(AbstractBaseUser):
    email = models.EmailField('email',max_length=128 , unique=True)
    password  = models.CharField('password', max_length=128)
    fullname = models.CharField('fullname', max_length=100)
    nickname = models.CharField('nickname', max_length=100)
    
    join_date = models.DateField('created_at', auto_now_add=True)
    updated_at = models.DateField('updated_at', auto_now=True)

    is_active = models.BooleanField(default=True)

    is_admin =models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class UserProfile(models.Model):
    user = models.OneToOneField('UserModel', on_delete=models.CASCADE)
    address = models.CharField('address', max_length=30)
    hobby = models.ManyToManyField('Hobby')


class Hobby(models.Model):
    hobby_name = models.CharField(max_length=30)