from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    like = models.IntegerField(default=0)
    like_activated_author = ArrayField(models.CharField(max_length=255, default=''), default=list)

    def publish(self):
        self.published_date = timezone.now()

    def __str__(self):
        return str(self.pk)


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=2000, verbose_name='comment')
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    like = models.IntegerField(default=0)
    like_activated_author = ArrayField(models.CharField(max_length=255, default=''), default=list)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.content


