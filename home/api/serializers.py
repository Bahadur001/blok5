from rest_framework import serializers
from home.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'content',"created_date" , "draft" ]