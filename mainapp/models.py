from django.db import models

class CSVFile(models.Model):
    file = models.FileField(upload_to='csv/')
    timeframe_in_minutes = models.IntegerField(default=10)