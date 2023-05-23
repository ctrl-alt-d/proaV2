from django.core.management.base import BaseCommand, CommandError
from demos import UploadExcels
from django.conf import settings
import os
from django.apps import apps


class Command(BaseCommand):
    help = 'Carrega dades a partir de CSVs. Esborra totes les dades anteriors.'

    def handle(self, *args, **options):

        path_dels_excels = os.path.join(
            settings.BASE_DIR,
            "demos/ExcelsUpload")
        fitxers = os.listdir(path_dels_excels)
        app__nom_model = [
            nom.replace(".csv", "").split("__")
            for nom in fitxers
            if nom.endswith(".csv")
        ]

        for app, nom_model in app__nom_model:
            try:
                model = apps.get_model(app_label=app, model_name=nom_model)
                nom_fitxer = f"{app}__{nom_model}.csv"
                fitxer = os.path.join(path_dels_excels, nom_fitxer)

                UploadExcels.upload_csv(
                    fitxer,
                    model)
                self.stdout.write(self.style.SUCCESS(
                    f"{nom_model} de l'app {app} carregat correctament"))
            except LookupError:
                msg = f"{nom_model} de l'app {app} no trobat"
                raise CommandError(msg)
            except Exception as e:
                msg = f"Error carregant {nom_model} de l'app {app}: {e}"
                raise CommandError(msg)