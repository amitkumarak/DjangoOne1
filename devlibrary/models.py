from django.db import models


# Create your models here.
from django.urls import reverse


class Library(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    creator = models.ForeignKey('auth.User')
    screenshot1 = models.ImageField(upload_to="devlibrary/", null=True, blank=True)
    screenshot2 = models.ImageField(upload_to="devlibrary/", null=True, blank=True)
    screenshot3 = models.ImageField(upload_to="devlibrary/", null=True, blank=True)
    githublink = models.CharField(max_length=256)
    websitelink = models.CharField(max_length=256)
    rating=models.SmallIntegerField(default=0)
    description= models.CharField(max_length=360)


    def publish(self):
        self.save()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("devsdetail", kwargs={"id": self.id})
