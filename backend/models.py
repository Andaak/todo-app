from django.db import models

class Todo(models.Model):
    oprettet = models.DateTimeField(auto_now_add=True)
    oppgavetekst = models.CharField(max_length=200)
    frist = models.DateTimeField(null=True, blank=True)
    ferdig = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.oppgavetekst} - {self.oprettet}'