from django.db import models
from django.contrib.auth.models import User
import random

# Create your models here.
def get_rendom_image():
    print("FUNCTION CALLED 🔥")
    return random.choice([
        'profile_pics/defaults/avatar1.jpg',
        'profile_pics/defaults/avatar2.jpg',
        'profile_pics/defaults/avatar3.jpg',
        'profile_pics/defaults/avatar4.jpg',
        'profile_pics/defaults/avatar5.jpg',
        'profile_pics/defaults/avatar6.jpg',
        'profile_pics/defaults/avatar7.jpg',
        'profile_pics/defaults/avatar8.jpg',
        'profile_pics/defaults/avatar9.jpg',
        'profile_pics/defaults/avatar10.jpg',

    ])

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    image = models.ImageField(default=get_rendom_image,upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}Profile'
    

    

    

