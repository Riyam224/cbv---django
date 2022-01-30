from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(_("title"), max_length=50)
    content = models.TextField(_("content"))
    created_at = models.DateTimeField(_("created at"), default=timezone.now)
    image = models.ImageField(_("image"), upload_to='post-img')
    active  = models.BooleanField(_("active") , default=False)
    slug = models.SlugField(_("slug") , blank=True , null=True)

    

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title

    def save(self , *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post , self).save(*args, **kwargs)
