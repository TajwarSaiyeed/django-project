from django.db import models
from categories.models import Category
from author.models import Author

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # one post can have multiple categories and one category can have multiple posts
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
