from django.db import models

from django.contrib.auth.models import User


class List(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.pk, self.owner)


class Record(models.Model):
    record = models.TextField()
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='records')

    def __str__(self):
        return '{} - {}'.format(self.pk, self.record)
