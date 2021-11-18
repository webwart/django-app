from django.db import models
from django.urls import reverse

# Create your models here.

class CompanyInfo(models.Model):
    CATEGORY_CHOICES = [
        (1, 'Asia'),
        (2, 'S-Afrika'),
        (3, 'N-Afrika'),
        (4, 'C-Amerika'),
    ]

    SKILL_LEVEL_CHOICES = [
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
    ]

    company = models.CharField(max_length=128)
    ceo = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    website = models.CharField(max_length=11)
    stars_count = models.DecimalField(max_digits=2, decimal_places=1)
    region = models.IntegerField(choices = CATEGORY_CHOICES)
    skill_level_id = models.IntegerField(choices = SKILL_LEVEL_CHOICES)
    is_active = models.BooleanField(default=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-stars_count","company"]

    def __str__(self):
        return self.company + ' (' + self.author + ')'

    def get_absolute_url(self):
        return reverse('allpages-home')