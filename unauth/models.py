from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

class AuthModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True, verbose_name='ID')
    original_url = models.URLField(max_length=500)
    short_url = models.CharField(max_length=32, unique=True)  # 10 not 6 because there might be a num added to it
    visits = models.PositiveIntegerField(default=0, verbose_name='Visits')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')

    # def __str__(self):
    #     return '%s: %s' % (self.original_url, self.short_url)
    
    def __str__(self):
        return f'ID: {self.id}, Alias: {self.short_url}, {self.visits} visits.'
    class Meta:
        verbose_name = "Link"
        verbose_name_plural = 'Most viewed links'

class Analytics(models.Model):
    parent = models.ForeignKey(AuthModel, on_delete=models.CASCADE, related_name="tracking", null=True, blank=True)