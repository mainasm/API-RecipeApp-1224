from .models import Recipe, Review

# Create serializers
from rest_framework import serializers
from .models import Recipe, Favorite, Review, Tag, Comment


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'recipe', 'reviewer', 'rating', 'comment', 'created_at']

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'user', 'recipe', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'recipe', 'author', 'content', 'created_at']

class RecipeSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    read_only_fields = ['created_by', 'created_at', 'updated_at']
    
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'ingredients', 'instructions', 'tags', 'reviews', 'comments', 'created_at', 'updated_at', 'created_by']