from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title
