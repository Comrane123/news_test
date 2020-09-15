from rest_framework import serializers

from post.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "url",
            "created_by",
            "created_at",
            "number_of_votes",
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "post",
            "body",
            "created_by",
            "created_at",
        ]
