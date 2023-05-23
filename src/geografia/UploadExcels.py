
import csv


def upload_csv(fitxer, model):
    """
    Aquest procés carrega les dades que troba al fitxer csv "fitxer"
    al model que li passem a "model"
    """
    model.objects.all().delete()

    with open(fitxer, newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.DictReader(csvfile, dialect=dialect)
        for row in reader:
            item = model()
            for (camp, valor) in row.items():
                setattr(item, camp, valor)
            item.save()
        csvfile.close()