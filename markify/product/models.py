from django.db import models
from team.models import Team
from userprofile.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    team = models.ForeignKey(Team, related_name='products', on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    

    
