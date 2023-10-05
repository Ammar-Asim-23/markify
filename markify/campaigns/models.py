# from django.db import models
# from product.models import Advertisement
# from client.models import Client

# class Campaigns(models.Model):
#     title = models.CharField(max_length=100)
#     ads = models.ManyToManyField(Advertisement, related_name='campaigns')
#     clients = models.ManyToManyField(Client, related_name='campaigns')
#     start_date = models.DateTimeField(auto_now_add=True)
#     end_date = models.DateTimeField()
    
#     def __str__(self):
#         return self.title
