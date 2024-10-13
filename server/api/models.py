from django.db import models

# Create your models here.
class BookModel(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=100, db_index=True)
    author = models.CharField(max_length=100)
