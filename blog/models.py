from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=timezone.now)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def pub_date_minutless(self):
        return self.pub_date.strftime('%e %b %Y')

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})
