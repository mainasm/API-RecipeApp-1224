from django.contrib import admin
from .models import Recipe, Review, Favorite, Tag, Comment

# Register your models here.
# List of models
models = [Recipe, Review, Favorite, Tag, Comment]

# Loop through the model list
# And register each of them
for model in models:
    admin.site.register(model)