from django.db import models


class Script(models.Model):
    name = models.CharField(max_length=100)
    source = models.TextField()

    notes       = models.TextField(blank=True)
    created     = models.DateTimeField(auto_now_add=True)
    modified    = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-modified',]