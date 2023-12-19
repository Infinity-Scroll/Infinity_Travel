from django.db import models
from accounts.models import User

class Tag(models.Model):
    tag = models.CharField(max_length=50,
                            # unique=True
                            )

    def __str__(self):
        return self.tag

class Companion(models.Model):
    STATUS_CHOICES = [
        ('A', '모집중'),
        ('Z', '모집완료'),
    ]

    AREA_CHOICES = [
        # 대륙 옵션 추가
        # 국가 옵션 추가
        # 도시 옵션 추가
    ]

    title = models.CharField(max_length=20)
    content = models.CharField(max_length=500)
    views = models.IntegerField(default=0, null=False)
    area = models.CharField(max_length=20, choices=AREA_CHOICES, null=True)
    schedule_start = models.DateField()
    schedule_end = models.DateField()
    image = models.ImageField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A', blank=True)
    tags = models.ManyToManyField(Tag)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    max_member = models.IntegerField(default=2, null=False)
    current_member = models.IntegerField(default=1, null=False)

    def __str__(self):
        return self.title
    
    def increase_views(self):
        self.views += 1
        self.save()


class Comment(models.Model):
    comment_text = models.TextField()
    parent_comment = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    companion_post = models.ForeignKey(Companion, related_name='comments', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.companion_post}: {self.comment_text[:50]}"