from django.db import models

# Provincia, ConsellComarcal, Municipi
class Provincia(models.Model):
   
    codi = models.CharField(
        verbose_name="Codi de província",
        max_length=2,
        unique=True,
        primary_key=True,
        help_text="Codi de província"
    )
    
    nom = models.CharField(
        verbose_name="Nom de la província",
        max_length=100,
        help_text="Nom de la província"
    )


    def __str__(self):
        return f"{self.codi} > {self.nom}"
    
class Comarca(models.Model):
   
    codi = models.CharField(
        verbose_name="Codi del Consell Comarcal",
        max_length=2,
        unique=True,
        primary_key=True,
        help_text="Codi del Consell Comarcal"
    )
    
    nom = models.CharField(
        verbose_name="Nom del Consell Comarcal",
        max_length=100,
        help_text="Nom del Consell Comarcal"
    )


    def __str__(self):
        return f"{self.codi} > {self.nom}"    

class Municipi(models.Model):
   
    codi = models.CharField(
        verbose_name="Codi de Municipi",
        max_length=6,
        unique=True,
        primary_key=True,
        help_text="Codi de Municipi"
    )
    
    nom = models.CharField(
        verbose_name="Nom del Municipi",
        max_length=100,
        help_text="Nom del Municipi"
    )

    codi_comarca = models.ForeignKey(
        Comarca,
        verbose_name="Consell Comarcal",
        help_text="Codi de Consell Comarcal aa que pertany el municipi",
        on_delete=models.CASCADE,
    )

    nom_comarca = models.CharField(
        verbose_name="Nom del Consell Comarcal",
        max_length=100,
        help_text="Nom del Consell Comarcal"
    )

    codi_provincia = models.ForeignKey(
        Provincia,
        verbose_name="Província",
        help_text="Codi de Província al que pertany el municipi",
        on_delete=models.CASCADE,
    )

    nom_provincia= models.CharField(
        verbose_name="Nom de la Província",
        max_length=100,
        help_text="Nom de la Província"
    )

    def __str__(self):
        return f"{self.codi} > {self.nom}"    
