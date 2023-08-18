from django.db import models


# Create your models here.

TYPE_CHOICES = [

    ('Cultural', 'Cultural'),
    ('Casual', 'Casual'),
    ('Sports', 'Sports'),

]


class Outfit(models.Model):
    name = models.CharField(max_length=200, help_text="What do you want to call this outfit?")
    description = models.TextField(help_text="Describe this outfit to give your clients a better understanding.")
    category = models.CharField(max_length=50, choices=TYPE_CHOICES, default="Cultural", help_text="Choose a category.")
    image = models.ImageField(upload_to="images", help_text="Choose an image that will represent your outfit.")
    price = models.DecimalField(max_digits=9, decimal_places=2, help_text="How much is this outfit going to cost?")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
