from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=125)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Comment(models.Model):

    level = models.IntegerField(default=0, blank=True, null=True)
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='post')
    author = models.CharField(max_length=50)
    comment = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='child', blank=True, null=True)

    def __str__(self):
        return f'Author: {self.author}, says: {self.comment}'
