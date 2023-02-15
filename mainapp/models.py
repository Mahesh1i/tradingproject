from django.db import models

class CSVFile(models.Model):
    file = models.FileField(upload_to='csv/')
    timeframe_in_minutes = models.IntegerField(default=10)
    
# addin another model class
class JsonFile(models.Model):
    name = models.CharField(max_field=30)
    file_size = models.IntegerField()
