from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Scince(models.Model):
    slug_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Theme(models.Model):
    scince = models.ForeignKey(Scince, on_delete=models.CASCADE)
    theme = models.CharField(max_length=255)
    video = models.CharField(max_length=255, blank=True, null=True)
    body = RichTextUploadingField()

    def __str__(self):
        return '{} - {}'.format(self.scince, self.theme)


class Quizes(models.Model):
    question = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    ball = models.IntegerField()
    timer = models.IntegerField(default=20, null=True, blank=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.question, self.ball, self.timer)


class PractisTheme(models.Model):
    scince = models.ForeignKey(Scince, on_delete=models.CASCADE)
    practis_name = models.CharField(max_length=255)
    practis_slug = models.SlugField(max_length=255)

    def __str__(self):
        return '{} - {}'.format(self.scince, self.practis_name)


class Practis(models.Model):
    practis_name = models.ForeignKey(PractisTheme, on_delete=models.CASCADE)
    question_title = models.CharField(max_length=255, blank=True, null=True)
    question = models.TextField()
    solusion = models.TextField(blank=True, null=True)
    checking = models.TextField()
    hint = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.pk, self.practis_name)


class Glossary(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='posts_img/')
    body = RichTextUploadingField()
    post_views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ResourceCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Resource(models.Model):
    resource = models.ForeignKey(ResourceCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True, null=True)
    img = models.ImageField(upload_to='resource_img/', blank=True, null=True)
    file = models.FileField(upload_to='resource_file/', blank=True, null=True)

    def __str__(self):
        return self.name
