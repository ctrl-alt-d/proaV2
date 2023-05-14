from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Perfil(models.Model):

    nom = models.CharField(
        "Nom de la persona de contacte",
        max_length=60,
        blank=True)

    cognoms = models.CharField(
        "Cognom de la persona de contacte",
        max_length=120,
        blank=True)

    organitzacio = models.CharField(
        "Organització",
        max_length=120,
        blank=True)

    telefon = models.CharField(
        "Telèfon de contacte",
        max_length=60,
        blank=True,
        help_text="Telèfon de contacte ( telf. Professional)")

    usuari = models.OneToOneField(
        User,
        editable=False,
        on_delete=models.CASCADE)

    def __str__(self):
        return u"{0}, {1} {4} ( {2} ) [{3}]".format(
            self.cognoms,
            self.nom,
            self.organitzacio,
            self.usuari.email,
            "*" if self.usuari.is_superuser else "")

    @ property
    def es_superuser(self):
        return self.usuari.is_superuser

    class Meta:
        ordering = ['cognoms', 'nom', ]


@ receiver(post_save, sender=User)
def _(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuari=instance, )
