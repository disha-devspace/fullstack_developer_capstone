from django.db import models


class Dealer(models.Model):
    id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    short_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Review(models.Model):
    dealer = models.ForeignKey(
        Dealer,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    name = models.CharField(max_length=100)
    review = models.TextField()
    purchase = models.BooleanField(default=False)
    purchase_date = models.DateField(null=True, blank=True)
    car_make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_year = models.IntegerField()
    sentiment = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name
