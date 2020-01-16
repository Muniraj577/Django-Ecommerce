from django.db import models


# Create your models here.
class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.email
