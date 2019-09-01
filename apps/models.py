from django.db import models

# Create your models here.
class list(models.Model):
    english = models.CharField(max_length=200)
    bangla  = models.CharField(max_length=200)
    count  = models.CharField(max_length=10)
   
    

    def __str__(self):
        return self.count  + ' - ' + str(self.english)
