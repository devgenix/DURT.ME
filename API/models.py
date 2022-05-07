from django.db import models


class UrlModel(models.Model):
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