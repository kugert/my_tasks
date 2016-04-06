from django.db import models


class VkUser(models.Model):
    user_id = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.BooleanField()
    status = models.TextField()
    interests = models.TextField()
    tv = models.TextField()
    site = models.CharField(max_length=50)
    movies = models.TextField()
    books = models.TextField()
    music = models.TextField()
    about = models.TextField()
    games = models.TextField()

    def __unicode__(self):
        return self.user_id


class VkFields(models.Model):
    field_name = models.CharField(max_length=20)
