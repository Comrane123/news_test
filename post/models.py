from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()

    number_of_votes = models.IntegerField(default=0)

    created_by = models.ForeignKey(
        User, related_name="stories", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return "%s" % self.title


class Vote(models.Model):
    post = models.ForeignKey(Post, related_name="votes", on_delete=models.CASCADE)

    created_by = models.ForeignKey(User, related_name="votes", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.post.number_of_votes = self.post.number_of_votes + 1
        self.post.save()

        super(Vote, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)

    body = models.TextField()

    created_by = models.ForeignKey(
        User, related_name="comments", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
