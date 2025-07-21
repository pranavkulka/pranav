from django.db import models
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    ceo = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    est_year = models.IntegerField()
    logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)


    def __str__(self):
        return self.name #to display the name in admin panel

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk":self.pk})

class Products(models.Model):
    product = models.CharField(max_length=100)
    color =  models.CharField(max_length=100)
    price = models.IntegerField()
    seat_cap = models.IntegerField()
    fuel_type =  models.CharField(max_length=100)
    miliege = models.IntegerField()
    company = models.ForeignKey(Company, related_name='companies', on_delete=models.CASCADE)

