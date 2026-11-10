
from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):

    ITEM_TYPE = [
        ('Lost', 'Lost'),
        ('Found', 'Found'),
    ]

    STATUS = [
        ('Active', 'Active'),
        ('Returned', 'Returned'),
    ]

    CATEGORY = [
        ('Electronics', 'Electronics'),
        ('Books', 'Books'),
        ('Accessories', 'Accessories'),
        ('Clothing', 'Clothing'),
        ('Documents', 'Documents'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=200)

    item_type = models.CharField(
        max_length=10,
        choices=ITEM_TYPE
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY
    )

    description = models.TextField()

    location = models.CharField(max_length=200)

    image = models.ImageField(
        upload_to='items/',
        blank=True,
        null=True
    )

    contact = models.CharField(max_length=100)

    status = models.CharField(
        max_length=10,
        choices=STATUS,
        default='Active'
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
