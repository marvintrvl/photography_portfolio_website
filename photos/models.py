from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f"Photo in category {self.category.name}"
