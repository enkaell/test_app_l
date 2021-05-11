from django.db import models
from allauth.account.signals import user_signed_up
from django.dispatch import receiver


class User(models.Model):
    id_user = models.AutoField(primary_key = True)
    username = models.CharField(max_length= 40)
    userpic =  models.ImageField(blank = True)

class Post(models.Model):
    id_post = models.AutoField(primary_key = True)
    place_name = models.CharField(max_length= 60)
    review = models.CharField(max_length= 4000, blank=  True)
    coordinates = models.CharField(max_length= 40, blank= True)

    def get_absolute_url(self):
        return f'/lk/{self.id_post}'



class Post_user(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE)

@receiver(user_signed_up)
def user_signed_up_(request, Post, sociallogin=None, **kwargs):
    if sociallogin:

        if sociallogin.account.provider == 'vk':

            Post.place_name = sociallogin.account.extra_data["screen_name"]
        Post.save()
