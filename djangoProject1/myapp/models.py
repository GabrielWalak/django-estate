from django.db import models

class Nieruchomosci(models.Model):
    ID_nieruchomosci = models.AutoField(primary_key=True)
    ID_adresu = models.IntegerField()
    Powierzchnia = models.DecimalField(max_digits=10, decimal_places=2)
    Liczba_pokoi = models.IntegerField()
    Cena = models.DecimalField(max_digits=10, decimal_places=2)
    Status = models.CharField(max_length=50)
    Typ_nieruchomosci = models.CharField(max_length=50)
    Opis = models.TextField()
