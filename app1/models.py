from django.db import models

class book(models.Model):
    name=models.TextField(max_length=100)
    author=models.TextField(max_length=50)

    def __str__(self):    
        return  self.name
