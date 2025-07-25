from django.db import models
from tinymce.models import HTMLField

class BannerImage(models.Model):
    image = models.ImageField(upload_to="polo_imgs/")

    def __str__(self):
        return f"bannerimage {self.id}"

class Chef(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="polo_imgs/")
    about = models.TextField()

    def __str__(self):
        return self.name

class MenuCategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="polo_imgs/", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Menu Categories"

    def __str__(self):
            return self.name

class Menu(models.Model):
    meal = models.CharField(max_length=100)
    ingredient = models.TextField()
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to="polo_imgs/", blank=True, null=True)

    def __str__(self):
        return self.meal

class Event(models.Model):
    image = models.ImageField(upload_to="polo_imgs/")
    title = models.CharField(max_length=200)
    content = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return self.title

class Reservation(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    people = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    mail = models.EmailField(max_length=256)

    def __str__(self):
        return self.date

class Testimonial(models.Model):
    image = models.ImageField(upload_to="polo_imgs/")
    content = models.TextField()
    name = models.CharField(max_length=70)
    location = models.CharField(max_length=70)
    rait = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class BlogCategory(models.Model):
    name = models.CharField(max_length=70)

    class Meta:
        verbose_name_plural = "Blog Categories"

    def __str__(self):
        return self.name

class Blog(models.Model):
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name="blogs")
    image = models.ImageField(upload_to="polo_imgs/")
    title = models.CharField(max_length=70)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Blogcomment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=256)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name

class GalleryCategory(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Gallery Categories"

    def __str__(self):
        return self.name

class Gallery(models.Model):
    image = models.ImageField(upload_to="polo_imgs/")
    name = models.CharField(max_length=100)
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, related_name="images")

    class Meta:
        verbose_name_plural = "Galleries"

    def __str__(self):
        return self.name

class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=256)
    phone = models.CharField(max_length=12)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class SiteSettings(models.Model):
    bannertitle = models.CharField(max_length=1000)
    abouttitle1 = models.CharField(max_length=100)
    aboutcontent1 = models.TextField()
    aboutimage1 = models.ImageField(upload_to="polo_imgs/")
    abouttitle2 = models.CharField(max_length=100)
    aboutcontent2 = models.TextField()
    aboutimage2 = models.ImageField(upload_to="polo_imgs/")
    abouttitle3 = models.CharField(max_length=100)
    aboutcontent3 = models.TextField()
    aboutimage3 = models.ImageField(upload_to="polo_imgs/")
    aboutvideo = models.FileField(upload_to="polo_imgs/")
    reservationimage = models.ImageField(upload_to="polo_imgs/")
    reservationcontent = HTMLField()
    subscribemail = models.EmailField(max_length=256)
    location = models.TextField()
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=256)
    workinghours = models.TextField()

    class Meta:
        verbose_name_plural = 'Site Settings'

    def save(self, *args, **kwargs):
        if not self.id and SiteSettings.objects.exists():
            return None
        return super(SiteSettings,self).save(*args,**kwargs)

    def __str__ (self):
        return "Settings"