from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import requests
from bs4 import BeautifulSoup
import requests

# Create your models here.
def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)

class Graphic(models.Model):
    name = models.CharField(max_length=500,default="", editable=True)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')
class Article(models.Model):
    title = models.CharField(max_length=500)
    head_image = models.ForeignKey(Graphic, on_delete=models.CASCADE, related_name="head_image")
    text = models.TextField(max_length=100000)
    images = models.ManyToManyField(Graphic,verbose_name="list of images", related_name="images")

class WebScraper(models.Model):

    def __init__(self, page, element):
        self.page = page
        self.element = element

    def get_page(self):
        page = requests.get(self.page)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup