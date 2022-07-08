from django.db import models
from django.utils.text import slugify
from .utils import generate_new_slug 
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True,null=False,blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories' # For customizing the APP name in Admin panel 
        verbose_name = 'Category' # For customizing name in admin panel inside any APP **Select <name> to change in top header **  

class Post(models.Model):
    # CAT_CHOICES = (
    #     ('general','General'),('technology','Technology'),('science','Science'),('sports','Sports'),
    #     ('entertainment','Entertainment'),('health','Health'),('business','Business'), ('politics','Politics'),
    #     ('world','World'),('education','Education'),('lifestyle','Lifestyle'),('travel','Travel'),
    #     ('fashion','Fashion'),('food','Food'),('fitness','Fitness'),('style','Style'),('travel','Travel'),('lifestyle','Lifestyle'),
    # )

    # blank is for Admin Panel whereas Null is for database
    title = models.CharField(verbose_name="post title",max_length=200,null=False,blank=False)
    slug = models.SlugField(verbose_name="post slug",unique=True,null=False,blank=False,editable=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=False,blank=False) 
    # category = models.CharField(verbose_name="post category",max_length=30,choices=CAT_CHOICES,default="general")
    content = models.TextField(verbose_name='post content',null=False,blank=False)
    summary = models.CharField(max_length=400,null=False,blank=False)
    thumbnail = models.ImageField(upload_to='posts/',null=True,blank=True)
    views = models.IntegerField(verbose_name='views',default=0)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(verbose_name='created at',auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} -> {self.created_at}"

    def save(self,*args, **kwargs):
        self.slug = generate_new_slug(self.__class__,self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('individual_post',kwargs={'slug':self.slug})

       
        
