from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Page(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='mypage')
    pname = models.CharField('Page Name',max_length=255)
    pcat = models.CharField('Page Categorie',max_length=255)
    ppublished = models.DateField('Page Published')



class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField('Post Title',max_length=255)
    ptcat = models.CharField('Page categories',max_length=255)
    ptpublished = models.DateField('Page Published',)
    
    
class Song(models.Model):
    user = models.ManyToManyField(User)
    stitle = models.CharField('Song Title',max_length=255)
    sduration = models.IntegerField('Song Duration',)
    
    def written_by(self):
        return ",".join([str(p) for p in self.user.all()])