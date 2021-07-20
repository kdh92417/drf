from django.db import models


class Quote(models.Model):
    quote_author = models.CharField(max_length=60)
    quote_body = models.TextField()
    context = models.CharField(max_length=60)
    source = models.URLField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'quotes'
