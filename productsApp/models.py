from django.db import models

# Create your models here.


class Products(models.Model):
    id = models.AutoField(primary_key=True),
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=250)
    price = models.FloatField(default=0.00)
    units = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta():
        db_table = 'products'
