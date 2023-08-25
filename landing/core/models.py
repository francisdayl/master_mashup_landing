from django.db import models

# Create your models here.


class Email(models.Model):
    email = models.EmailField(unique=True, null=False)
    def __str__(self):
        return self.email
