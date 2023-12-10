from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from core.models import TimestampedModel


class UserManager(BaseUserManager):
    def create_user(self, email, gender, password=None):
        if email == None:
            raise TypeError("이메일 필수값입니다.")
        if password is None:
            raise TypeError("비밀번호는 필수값입니다.")

        user = self.model(email=self.normalize_email(email), gender=gender)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, gender, password):
        user = self.create_user(email, gender, password)

        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin, TimestampedModel):
    email = models.EmailField(max_length=100, db_index=True, unique=True)
    objects = UserManager()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    GENDER = [
        ("Male", "남자"),
        ("Female", "여자"),
    ]
    gender = models.CharField(max_length=6, choices=GENDER)
    REQUIRED_FIELDS = ["password", "gender"]

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.profile.nickname:
            return self.profile.nickname
        return None


class Profile(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile")
    nickname = models.CharField(max_length=30)
    introduce = models.CharField(max_length=200)
