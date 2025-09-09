from django.db import models

# Create your models here.
class UnderConstruction(models.Model):
    is_under_construction = models.BooleanField(default=False)
    uc_note = models.TextField(blank=True,null=True,help_text="Note for Under Construction mode")
    uc_duration = models.DateTimeField(blank=True,null=True,help_text="End data and time  for Under Construction mode")
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Under construction: {self.is_under_construction}"
    
    
