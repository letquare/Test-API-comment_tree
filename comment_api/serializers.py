from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class FilterCommentListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentChildSerializer(serializers.ModelSerializer):

    child = RecursiveSerializer(many=True)

    class Meta:

        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ('id', 'parent', 'post_id', 'level', 'author', 'comment', 'child')

    def create(self, validated_data):
        tracks_data = validated_data.pop('child')
        child = Comment.objects.create(**validated_data)
        for track_data in tracks_data:
            Comment.objects.create(child=child, **track_data)
        return child


class CommentSerializer(serializers.ModelSerializer):

    child = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'parent', 'post_id', 'level', 'author', 'comment', 'child')
