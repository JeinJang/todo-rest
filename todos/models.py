from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
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
