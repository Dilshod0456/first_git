from django.db import models

# Create your models here.
class Blog(models.Model):
    sanasi = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    author = models.ForeignKey('app1.User', on_delete = models.CASCADE, null =True, blank = True)
    image = models.ImageField(upload_to="imgs/")

    def __str__(self):
        return self.title
    