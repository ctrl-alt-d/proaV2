from django.core.management.base import BaseCommand, CommandError
from geografia.excelsgeografia2model import run
import traceback


class Command(BaseCommand):
    help = 'Carrega dades de geografia a partir dels excels. Esborra les dades anteriors.'

    def handle(self, *args, **options):

        try:
            carregats, errors = run()
        except Exception as e:
            traceback.print_exc()
            msg = f"Error executant la comanda: {e}"
            raise CommandError(msg)

        carregats_txt = "\n * ".join(carregats)
        self.stdout.write(
            self.style.SUCCESS(
                f"Carregats:\n * {carregats_txt}")
        )
        if errors:
            errors_txt = "\n * ".join(errors)
            self.stdout.write(
                self.style.ERROR(
                    f"Errors:\n * {errors_txt}")
            )
            raise CommandError("Càrrega amb errors")
