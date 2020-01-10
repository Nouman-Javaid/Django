from django.db import models
# To override and customize Django default user model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password, is_active=True, is_staff=False, is_admin=False):
        """Create and save new user with given detail"""
        if not email:
            return ValueError("Input Email")
        if not password:
            return ValueError("Input Password")
        if not name:
            return ValueError("Input Name")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)  # Change user password
        user.is_active = is_active
        user.is_staff = is_staff
        user.is_admin = is_admin
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, name, password):
        """Create and save new superuser with given details"""
        user = self.create_user(email, name, password, is_staff=True)
        return user

    def create_superuser(self, email, name, password):
        """Create and save new superuser with given details"""
        user = self.create_user(email, name, password, is_staff=True, is_admin=True)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database Model for Users in System"""
    email = models.EmailField(max_length=255, unique=True)
    fullname = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname']

    def get_full_name(self):
        """Retrieve user full name"""
        return self.name

    def get_short_name(self):
        """Retrieve user short name"""
        return self.name

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



