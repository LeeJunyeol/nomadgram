from django.db import models
from nomadgram.users import models as user_models
from django.utils.encoding import python_2_unicode_compatible

class TimeStampedModel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # 이건 abstract 클래스임을 알림
  # Meta 클래스: 필드가 아닌 모든 것, 필드가 아닌 정보를
  class Meta:
    abstract = True

@python_2_unicode_compatible
class Image(TimeStampedModel):
  """ Image Model """

  file = models.ImageField()
  location = models.CharField(max_length=140)
  caption = models.TextField()
  creator = models.ForeignKey(user_models.User, null=True)

  def __str__(self):
    return '{} - {}'.format(self.location, self.caption)


@python_2_unicode_compatible
class Comment(TimeStampedModel):
  """ Comment Model """

  message = models.TextField()
  creator = models.ForeignKey(user_models.User, null=True)
  image = models.ForeignKey(Image, null=True, related_name='comments')

  def __str__(self):
    return self.message

class Like(TimeStampedModel):
  """ Like Model """

  creator = models.ForeignKey(user_models.User, null=True)
  image = models.ForeignKey(Image, null=True, related_name='likes')

  def __str__(self):
    return 'User: {} - Image Caption: {}'.format(self.creator.username, self.image.caption)
