from django.db import models

class Participant(models.Model):
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=100)

class Certificate(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    participant = models.ForeignKey('Participant', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
