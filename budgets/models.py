from django.db import models

class Income(models.Model):
    title = models.CharField(max_length=30, blank=False, null=False)
    amount = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False)
    type = models.CharField(max_length=20, default='income')
    date = models.DateField(blank=False, null=False)
    category = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
