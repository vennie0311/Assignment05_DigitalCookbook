from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    prep_time_minutes = models.PositiveIntegerField(default=0)
    recipe_photo = models.ImageField(upload_to='recipes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.quantity} {self.name}" if self.quantity else self.name
