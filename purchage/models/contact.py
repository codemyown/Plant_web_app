from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 50)
    number = models.IntegerField(default = 0)
    message = models.TextField()


    def __str__(self):
        return self.name
