from django.db import models


# Create your models here.

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50, null=False)
    lastname = models.CharField(max_length=50, null=False)
    avatar = models.ImageField(upload_to='./images/users')

    def __str__(self):
        return self.firstname + " " + self.lastname


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    thumb = models.ImageField(upload_to='./images/posts')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
