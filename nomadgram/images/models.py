from django.db import models

class TimeStampedModel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # 이건 abstract 클래스임을 알림
  # Meta 클래스: 필드가 아닌 모든 것, 필드가 아닌 정보를
  class Meta:
    abstract = True

class Image(TimeStampedModel):
  file = models.ImageField()
  location = models.CharField(max_length=140)
  caption = models.TextField()

class Comment(TimeStampedModel):
  message = models.TextField()
