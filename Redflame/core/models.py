from django.db import models
from django.contrib.auth.models import User

class Userdetails(models.Model):
    STATE_CHOICES = [
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CT', 'Chhattisgarh'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OR', 'Odisha'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TG', 'Telangana'),
        ('TR', 'Tripura'),
        ('UP', 'Uttar Pradesh'),
        ('UK', 'Uttarakhand'),
        ('WB', 'West Bengal'),
        ('AN', 'Andaman and Nicobar Islands'),
        ('CH', 'Chandigarh'),
        ('DN', 'Dadra and Nagar Haveli and Daman and Diu'),
        ('DL', 'Delhi'),
        ('JK', 'Jammu and Kashmir'),
        ('LA', 'Ladakh'),
        ('LD', 'Lakshadweep'),
        ('PY', 'Puducherry'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=2,choices=STATE_CHOICES)
    pincode=models.IntegerField(
        default=0,
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.id)

class upperwear(models.Model):

    CATEGORY_CHOICES = [
        ('SHIRTS','shirts'),
        ('T_SHIRTS','t-shirts'),
        ('SWEATSHIRTS','sweatshirts')
    ]

    name=models.CharField(max_length=100)
    category = models.CharField(max_length=30,choices=CATEGORY_CHOICES)
    short_d = models.CharField(max_length=400)
    desc = models.TextField()
    original_price=models.IntegerField()
    discounted_price=models.IntegerField()
    upperwear_img = models.ImageField(upload_to='upperwear_img')

    def __str__(self):
        return str(self.name)