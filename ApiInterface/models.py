from django.db import models

class Message(models.Model):
    MessageBody = models.TextField()
    MessageFromEmail = models.CharField(max_length=100)
    MessageTo = models.CharField(max_length=100)
    IsRead = models.BooleanField()
    MessageDate = models.DateField()

    def __str__(self):
        return self.MessageBody


# Create your models here.
