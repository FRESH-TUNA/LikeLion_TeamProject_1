from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    def __str__(self):
        return self.title
    def summary(self):
        return self.content[:100]
