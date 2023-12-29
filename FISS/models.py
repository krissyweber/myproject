from django.db import models

class MyModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class FinanceResource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.title