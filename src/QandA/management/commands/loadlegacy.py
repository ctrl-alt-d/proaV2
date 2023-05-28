from django.core.management.base import BaseCommand, CommandError
from legacydataloader import run
import traceback


class Command(BaseCommand):
    help = 'Cerrega dades anteriors'

    def handle(self, *args, **options):
        try:
            run()
        except Exception as e:
            traceback.print_exc()
            raise CommandError(f"Error creant dades de demo: {e}")

        self.stdout.write(self.style.SUCCESS("Dades creades"))
