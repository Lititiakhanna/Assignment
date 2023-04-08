from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255, unique=True)
    blog_comment = models.JSONField(blank=True, null=True)

class Blog(models.Model):
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="blog_account",
        null=False,
        blank=False,
    )
    blog_text = models.TextField()

class Comment(models.Model):
    comment = models.TextField()
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="comment_account",
        null=False,
        blank=False,
    )
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name="blog",
        null=False,
        blank=False,
    )

    # client_info = models.ForeignKey(
    #     ClientInfo,
    #     on_delete=models.CASCADE,
    #     related_name="requester_clientinfo",
    #     null=False,
    #     blank=False,
    # )
# Create your models here.
