from django.db import models

# Create your models here.


class Pregunta(models.Model):
    """
    Pregunta tipus. Exemple: "Hi ha porta giratòria?"
    """
    text = models.CharField(max_length=200)
    respostes = models.ManyToManyField("Resposta", through="RespostaPregunta")


class Resposta(models.Model):
    """
    Resposta tipus. Exemple: "Sí"
    """
    text = models.CharField(max_length=200)


class RespostaPregunta(models.Model):
    """
    Quines possibles respostes té una pregunta i en quin ordre apareixen
    """
    pregunta = models.ForeignKey(Pregunta, on_delete=models.RESTRICT)
    resposta = models.ForeignKey(Resposta, on_delete=models.RESTRICT)
    ordre = models.IntegerField()
