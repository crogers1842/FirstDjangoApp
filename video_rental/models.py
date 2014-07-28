from django.db import models

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=50)
    year_released = models.IntegerField()
    rating = models.CharField(max_length=5)

    def __unicode__(self):
        return self.title