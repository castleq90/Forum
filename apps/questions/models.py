from django.db import models

from apps.users.models import User

class Question(models.Model):
    title      = models.CharField(max_length=200)
    contents   = models.TextField()
    like_count = models.PositiveIntegerField(default=0)
    create_at  = models.DateTimeField(auto_now_add=True)
    update_at  = models.DateTimeField(auto_now=True)
    user       = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'questions'

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment   = models.CharField(max_length=300)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    question  = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        db_table = 'comments'

    def __str__(self):
        return self.comment

class Like(models.Model):
    create_at  = models.DateTimeField(auto_now_add=True)
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    question   = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        db_table = 'likes'