from django.db import models

# Create your models here.
class   Users(models.Model):
    # we have a uuid auto generated we dont have to write it
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
    
class   Comments(models.Model):
    author_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Blog_posts(models.Model):
    posted_at = models.DateField(auto_now=False, auto_now_add=False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    post_text = models.CharField(max_length=3000)    

    def __str__(self):
        return self.name
