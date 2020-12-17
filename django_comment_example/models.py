from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to = "user_image",null=True, blank = True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
    	return reverse('post-detail', kwargs={'pk': self.pk})

class Like(models.Model):
    user = models.ManyToManyField(User, related_name='likingUser')
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    likes = models.IntegerField(default = 0)

    #Like the Post
#
    @classmethod
    def like(cls, post, liking_user):
        obj, create = cls.objects.get_or_create(post = post)
        obj.user.add(liking_user)
        likes +=1
        #if obj.user.add == 1;


    #Dislike the Post

    @classmethod
    def dislike(cls, post, disliking_user):
        obj, create = cls.objects.get_or_create(post = post)
        obj.user.remove(disliking_user)


    def __str__(self):
        return str(self.post)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField( max_length=100)
    text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

"""
    def get_absolute_url(self):
        return reverse('comments-detail', kwargs={'pk': self.pk})
"""