from django.db import models
from management.models import User

# Create your models here.


class DiseasePost(models.Model):
    poster = models.ForeignKey(to=User, verbose_name="Disease Post's poster", on_delete=models.CASCADE, max_length=255)

    title = models.CharField(verbose_name="Title of post", max_length=255)
    description = models.TextField(verbose_name="Description of post")

    intensity = models.IntegerField(verbose_name="Intensity")

    files_1 = models.FileField(verbose_name="Attachment № 1", upload_to="images/files/", null=True, default=None)
    files_2 = models.FileField(verbose_name="Attachment № 2", upload_to="images/files/", null=True, default=None)
    files_3 = models.FileField(verbose_name="Attachment № 3", upload_to="images/files/", null=True, default=None)

    objects = models.Manager()

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return f"{self.poster.first_name}-{self.title}"


class Comment(models.Model):
    commentator = models.ForeignKey(to=User, verbose_name="Commentator", on_delete=models.CASCADE,
                                    related_name="commentator")
    post = models.ForeignKey(to=DiseasePost, on_delete=models.CASCADE, verbose_name="Post's comment",
                             related_name="Comment")

    content = models.TextField(verbose_name="Content of Comment")

    likes = models.IntegerField(verbose_name="Likes of comment", null=True)
    dislikes = models.IntegerField(verbose_name="Dislikes of comment", null=True)

    objects = models.Manager()

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"{self.commentator.first_name}-{self.post}"
