from django.db import models

# Create your models here.
class Articles(models.Model):
    article_title = models.TextField(max_length=30)
    article_url = models.TextField(max_length=30)
    article_summary = models.TextField(max_length=30)

    def _str_ (self):
        return self.article_title