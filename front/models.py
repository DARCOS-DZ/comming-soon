from django.db import models

# Create your models here.

class Message(models.Model):
    """
    This model represents a service provided by the company.
    """
    fname = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.fname}-{self.email}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
