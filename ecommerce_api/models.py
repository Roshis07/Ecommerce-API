from django.db import models

# Create your models here.
class Item(models.Model):
    item_name=models.CharField(max_length=255)
    item_price=models.IntegerField()
    item_description=models.TextField()
    item_id=models.IntegerField()
    item_availavility=models.BooleanField(default=True)
    item_discount=models.IntegerField()
    item_final_price=models.IntegerField()
    
    
    def _init__(self):
        self.item_name()
        
    