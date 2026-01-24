from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)

    excerpt = models.TextField(blank=True)
    content = RichTextUploadingField()

    image = models.ImageField(upload_to="blog/", blank=True, null=True)

    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        # Slug auto si vide
        if not self.slug:
            base = slugify(self.title)[:200] or "article"
            slug = base
            i = 2
            while Article.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                suffix = f"-{i}"
                slug = (base[: (220 - len(suffix))] + suffix)
                i += 1
            self.slug = slug

        # Date de publication si on publie
        if self.is_published and self.published_at is None:
            self.published_at = timezone.now()

        super().save(*args, **kwargs)
