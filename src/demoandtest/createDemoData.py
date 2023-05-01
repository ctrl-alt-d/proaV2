from formularis.models import Pregunta, Resposta, RespostaPregunta


def run():
    """
    Crea dades de demo
    """
    RespostaPregunta.objects.all().delete()
    Pregunta.objects.all().delete()
    Resposta.objects.all().delete()
    pregunta1 = Pregunta.objects.create(text="Hi ha porta giratòria?")
    pregunta2 = Pregunta.objects.create(text="Hi ha rampa d'accés?")
    resposta1 = Resposta.objects.create(text="Sí")
    resposta2 = Resposta.objects.create(text="No")
    resposta3 = Resposta.objects.create(text="No cal rampa, no hi ha escales")

    RespostaPregunta.objects.create(
        pregunta=pregunta1, resposta=resposta1, ordre=1)
    RespostaPregunta.objects.create(
        pregunta=pregunta1, resposta=resposta2, ordre=2)

    RespostaPregunta.objects.create(
        pregunta=pregunta2, resposta=resposta1, ordre=1)
    RespostaPregunta.objects.create(
        pregunta=pregunta2, resposta=resposta2, ordre=2)
    RespostaPregunta.objects.create(
        pregunta=pregunta2, resposta=resposta3, ordre=3)