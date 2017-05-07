from django.db import models
from django.urls import reverse

from django.utils import timezone


# Create your models here.
class post(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.CharField(max_length=360)
    created_at = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(null=True, blank=True)
    likes = models.IntegerField(default=0)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text

    # comment model
    # class comment(models.Model):
    # author = models.ForeignKey('auth.User')
    # text = models.CharField(max_length=360)
    # created_at = models.DateTimeField(default=timezone.now)
    # pub_date = models.DateTimeField(null=True, blank=True)

    # def publish(self):
    #   self.pub_date = timezone.now()
    #  self.save()

    # def __str__(self):
    #   return self.text


# feedback model

# Image model
class Images(models.Model):
    uploader = models.ForeignKey('auth.User')
    text = models.CharField(max_length=360)
    uploaded_at = models.DateTimeField(default=timezone.now)

    file_path = models.ImageField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.text


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.document.name


