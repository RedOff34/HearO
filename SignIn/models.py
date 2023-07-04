from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserManager(BaseUserManager):
    def create_user(self, user_id, password, name, email, phone_num, emergency, address, gender, birth, medical_info,**extra_fields):
        if not user_id:
            raise ValueError('The user_id field must be set')
        
        
        user = self.model(
            user_id=user_id,
            name=name,
            email=self.normalize_email(email),
            phone_num=phone_num,
            emergency=emergency,
            address=address,
            gender=gender,
            birth=birth,
            medical_info = medical_info
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password, name, email, phone_num, emergency, address, gender, birth, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        user = self.create_user(user_id, password, name, email, phone_num, emergency, address, gender, birth, **extra_fields)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    user_id = models.CharField(max_length=20, unique=True, primary_key=True)
    name = models.CharField(max_length=5)
    email = models.EmailField(max_length=30, unique=True)
    phone_num = models.CharField(max_length=11)
    emergency = models.CharField(max_length=11)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    birth = models.DateField()
    medical_info = models.CharField(max_length=500,null=True, blank=True, default='')
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
     

    objects = UserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['name', 'email', 'phone_num', 'emergency', 'address', 'gender', 'birth']


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    
@receiver(post_save, sender=User)
def create_user_setting(sender, instance, created, **kwargs):
    if created:
        from Main.models import Setting  # 'Setting' 모델을 직접 가져옵니다.
        Setting.objects.create(user=instance, sensitivity=100, count=10)
