from django.db import models

class applists(models.Model):
    appname=models.CharField(verbose_name='App name',primary_key=True,max_length=50,unique=True,null=False)
    appimg=models.ImageField(upload_to = 'app_images',null=True,blank=True)
    created_at = models.DateTimeField(verbose_name='created date',auto_now_add=True,editable=False,null=True,blank=True)
    updated_at = models.DateTimeField(verbose_name='updated date',null=True,blank=True)

    def __str__(self):
        return str(self.appname)

    def save(self, *args, **kwargs):
        super(applists, self).save()