from django.db import models
from django.shortcuts import reverse
from tinymce import HTMLField

from django.utils.text import slugify
from time import time


class Upload(models.Model):
    UPLOAD_TYPES = (
        ('I', 'Image'),
        ('V', 'Video'),
        ('D', 'Doc'),
    )
    title = models.CharField(max_length=200, db_index=True)
    type = models.CharField(max_length=50, blank=True, choices=UPLOAD_TYPES)
    pub_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, blank=True, unique=True)
    data = models.ImageField(upload_to=type)  

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']


class Company(models.Model):
    COMPANY_TYPES = (
        ('P', 'Partner'),
        ('C', 'Customer'),
    )
    title = models.CharField(max_length=200, db_index=True)
    type = models.CharField(max_length=50, blank=True, choices=COMPANY_TYPES)
    image = models.ForeignKey(Upload, on_delete=models.CASCADE)    
    brief = HTMLField(blank=True, max_length=500, db_index=True)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.title


class Content(models.Model):
    CONTENT_TYPES = (
        ('P', 'Product'),
        ('L', 'Solution'),
        ('S', 'Service'),
        ('V', 'Vacancy'),
        ('N', 'News'),
        ('J', 'Project'),
        ('A', 'About'),
    )
    title = models.CharField(max_length=200, db_index=True)
    type = models.CharField(max_length=50, blank=True, choices=CONTENT_TYPES)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey(Upload, on_delete=models.CASCADE)    
    brief = HTMLField(blank=True, max_length=500, db_index=True)
    description = HTMLField(blank=True, max_length=2000, db_index=True)
    characteristic = HTMLField(blank=True, max_length=2000, db_index=True)
    resources = HTMLField(blank=True, max_length=2000, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']

    # def get_absolute_url(self):
    #     return reverse('dracoin:post_detail_url', kwargs={'slug': self.slug})

    # def get_update_url(self):
    #     return reverse('dracoin:post_update_url', kwargs={'slug': self.slug})

    # def get_delete_url(self):
    #     return reverse('dracoin:post_delete_url', kwargs={'slug': self.slug})

    # def get_add_comment_url(self):
    #     return reverse('dracoin:add_comment_url', kwargs={'slug': self.slug})

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = gen_slug(self.title)
    #     super().save(*args, **kwargs)

    # def __str__(self):
    #     return self.title

    # class Meta:
    #     ordering = ['-pub_date']
