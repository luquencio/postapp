from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 20)
    home_phone = models.CharField(max_length = 20)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    autor = models.ForeignKey(UserProfile, null=True)
    title = models.CharField(max_length = 200)
    descr = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)
    photo1 = models.ImageField(upload_to="media/postsimages", blank=True, null=True)
    photo2 = models.ImageField(upload_to="media/postsimages", blank=True, null=True)
    photo3 = models.ImageField(upload_to="media/postsimages", blank=True, null=True)
    photo4 = models.ImageField(upload_to="media/postsimages", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
