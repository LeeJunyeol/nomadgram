from django.db import models
from nomadgram.users import models as user_models

class TimeStampedModel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # 이건 abstract 클래스임을 알림
  # Meta 클래스: 필드가 아닌 모든 것, 필드가 아닌 정보를
  class Meta:
    abstract = True

class Image(TimeStampedModel):
  """ Image Model """

  file = models.ImageField()
  location = models.CharField(max_length=140)
  caption = models.TextField()
  creator = models.ForeignKey(user_models.User, null=True)

class Comment(TimeStampedModel):
  """ Comment Model """

  message = models.TextField()
  creator = models.ForeignKey(user_models.User, null=True)
  image = models.ForeignKey(Image, null=True)

class Like(TimeStampedModel):
  """ Like Model """

  creator = models.ForeignKey(user_models.User, null=True)
  image = models.ForeignKey(Image, null=True)