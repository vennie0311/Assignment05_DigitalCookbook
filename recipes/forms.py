from django import forms
from django.forms import inlineformset_factory
from .models import Ingredient, Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'prep_time_minutes', 'recipe_photo']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'prep_time_minutes': forms.NumberInput(attrs={'min': 0}),
        }


IngredientFormSet = inlineformset_factory(
    Recipe,
    Ingredient,
    fields=['name', 'quantity'],
    extra=1,  # Start with just 1 ingredient field
    can_delete=True,  # Allow deletion
    widgets={
        'name': forms.TextInput(attrs={'placeholder': 'Ingredient name'}),
        'quantity': forms.TextInput(attrs={'placeholder': 'Quantity, e.g. 2 cups'}),
    }
)
