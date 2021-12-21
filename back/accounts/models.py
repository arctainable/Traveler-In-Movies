from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class User(AbstractUser):
    nickname = models.CharField(max_length=100, default='')
    background_image = ProcessedImageField(
        blank=True,
        upload_to='profile_background_images/%Y/%m/%d',
        # processors=[ResizeToFill()]
        format='JPEG',
        options={'quality':100}
    )
    profile_image = ProcessedImageField(
        blank=True,
        upload_to='profile_images/%Y/%m/%d/',
        processors=[ResizeToFill(200,200)],
        format='JPEG',
        options={'quality':100 }
    )
    # 유저의 리뷰 및 댓글에 따른 점수 필드
    rank_point = models.BigIntegerField(default=0)

    # 팔로워 팔로우 N:M 관계
    # followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')

    # preference
    user_preference = models.TextField(max_length=100)
