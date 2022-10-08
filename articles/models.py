from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    body = models.CharField(max_length=500, null=False, blank=False)
    writer = models.CharField(max_length=100, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Article:{self.id} Created:{self.created}"