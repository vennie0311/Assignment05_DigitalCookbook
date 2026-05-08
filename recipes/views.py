from django.shortcuts import get_object_or_404, redirect, render
from .forms import IngredientFormSet, RecipeForm
from .models import Recipe


def dashboard(request):
    recipes = Recipe.objects.order_by('-created_at')
    return render(request, 'recipes/dashboard.html', {'recipes': recipes})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


def manage_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        formset = IngredientFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            recipe = form.save()
            formset.instance = recipe
            formset.save()
            return redirect('dashboard')
    else:
        form = RecipeForm()
        formset = IngredientFormSet()

    return render(request, 'recipes/manage_recipe.html', {
        'form': form,
        'formset': formset,
    })
