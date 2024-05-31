from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
  """
  Custom User Manager that will help in creating users using the fields
  I provided
  """
  
  def create_user(self, email, password, **extra_fields):
    """
    Create and save user using the provided email and password
    """
    if not email:
      raise ValueError("Email must be set")
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save()
    return user
  
  def create_superuser(self, email, password, **extra_fields):
    """
    Create and save a super user
    """
    extra_fields.setdefault("is_staff", True)
    extra_fields.setdefault("is_superuser", True)
    extra_fields.setdefault("is_active", True)

    if extra_fields.get("is_staff") is not True:
      raise ValueError("Superuser must have is_staff=True")
    if extra_fields.get("is_superuser") is not True:
      raise ValueError("Superuser must have is_superuser=True")
    if extra_fields.get("is_active") is not True:
      raise ValueError("Superuser must have is_active=True")
    
    return self.create_user(email, password, **extra_fields)