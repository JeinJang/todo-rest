from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models

class UserManager(BaseUserManager):
  def create_user(self, nickname, user_id, password):

    user = self.model(
      nickname=nickname,
      user_id=user_id,
    )
    user.set_password(password)
    user.save(using=self._db)

    return user

class User(AbstractBaseUser):
  nickname = models.CharField(max_length=100, unique=True)
  user_id = models.CharField(max_length=100, unique=True)

  USERNAME_FIELD = 'email'

  def __str__(self):
    return self.nickname

class Tag(models.Model):
  name = models.CharField(max_length=50)

  text_color = models.CharField(
    max_length=7,
    validators=[
      RegexValidator('^#[A-Fa-f0-9]{6}$', message="Text color must be hex code.")
    ]
  )
  background_color = models.CharField(
    max_length=7,
    validators=[
      RegexValidator('^#[A-Fa-f0-9]{6}$', message="Background color must be hex code.")
    ]
  )
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class Todo(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=500)
  creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
  tag = models.ForeignKey(Tag, on_delete=models.PROTECT, related_name='tags')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  due_date = models.DateTimeField()
  closed_at = models.DateTimeField(blank=True, null=True)
  is_closed = models.BooleanField(default=False)
  deleted_at = models.DateTimeField(blank=True, null=True)

  def __str__(self):
    return self.title
