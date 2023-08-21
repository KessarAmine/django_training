from rest_framework import serializers
from .models import Users, Comments, Blog_posts

class   Users_serializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.save()
        return instance

class   comments_serializer(serializers.ModelSerializer):
    class Meta:
        model = Comments,
        fields = '__all__'
    def update(self, instance, validated_data):
        instance.author_id = validated_data.get('author_id', instance.author_id)
        instance.content = validated_data.get('content', instance.content)

class   Blog_posts_serializer(serializers.ModelSerializer):
    class Meta:
        model = Blog_posts,
        fields = '__all__'
    def update(self, instance, validated_data):
        instance.posted_at = validated_data.get('posted_at', instance.posted_at)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.post_text = validated_data.get('post_text', instance.post_text)
        
