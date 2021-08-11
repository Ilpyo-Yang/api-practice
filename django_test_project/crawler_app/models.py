from django.db import models

# Create your models here.
class Deal(models.Model):
    img_url = models.CharField(max_length=300)
    title = models.CharField(max_length=200)
    # prohibit duplited link
    link = models.CharField(max_length=200, primary_key=True)
    reply_count = models.IntegerField()
    up_count = models.IntegerField()
