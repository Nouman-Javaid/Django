from django.db import models
# To override and customize Django default user model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, f_name, l_name, password=None, is_staff=False, is_super=False):
        """Create and save new user with given detail"""

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=f_name, last_name=l_name)
        user.set_password(password)
        user.is_superuser = is_super
        user.is_staff = is_staff
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        """Create and save new superuser with given details"""

        user = self.create_user(email, first_name, last_name, password, True, True)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database Model for Users in System"""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    '''
    def get_full_name(self):
        """Retrieve user full name"""
        
        return "%s %s" % (self.first_name, self.last_name)
    '''

    def get_first_name(self):
        """Retrieve user short name"""

        return self.first_name

    def get_last_name(self):
        """Retrieve user short name"""

        return self.last_name

    def __str__(self):
        """Return string representation of our user"""
        return self.email

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        """Create Token for each new user"""
        if created:
            Token.objects.create(user=instance)


''' 
class ProfileFeedItems(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return model as a string"""
        return self.status_text
'''
