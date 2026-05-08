from pathlib import Path
from PIL import Image, ImageDraw
import os
import sys

base = Path(__file__).resolve().parent
sys.path.insert(0, str(base))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digital_cookbook.settings')

media_dir = base / 'media' / 'recipes'
os.makedirs(media_dir, exist_ok=True)
img = Image.new('RGB', (640, 420), color=(255, 160, 90))
d = ImageDraw.Draw(img)
d.text((40, 180), 'Sample Dish', fill=(255, 255, 255))
img_path = media_dir / 'sample_dish.jpg'
img.save(img_path, 'JPEG')
print('Image saved at', img_path)

import django

django.setup()

from recipes.models import Recipe, Ingredient

recipe = Recipe.objects.create(
    title='Sunset Curry Bowl',
    description='A warm citrus curry bowl with coconut rice.',
    prep_time_minutes=90,
    recipe_photo='recipes/sample_dish.jpg',
)
Ingredient.objects.create(recipe=recipe, name='Coconut milk', quantity='1 can')
Ingredient.objects.create(recipe=recipe, name='Sweet potato', quantity='2 cups diced')
Ingredient.objects.create(recipe=recipe, name='Red curry paste', quantity='3 tbsp')
print('Created recipe', recipe)
