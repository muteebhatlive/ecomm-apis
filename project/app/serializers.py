from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description'] 

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id', 'category', 'name', 'description']

    def create(self, validated_data):
        category_id = validated_data.pop('category_id')  # Remove category_id from validated_data
        subcategory = Subcategory.objects.create(category_id=category_id, **validated_data)
        return subcategory
