from django.db import models

class Todo(models.Model):
    oppgavetekst = models.CharField(max_length=200)
    ferdig = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.oppgavetekst}'