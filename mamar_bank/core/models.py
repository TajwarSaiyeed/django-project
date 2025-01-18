from django.db import models

class Bankrupt(models.Model):
    is_bankrupt = models.BooleanField(default=False)

    def __str__(self):
        return f"Bankrupt: {self.is_bankrupt}"