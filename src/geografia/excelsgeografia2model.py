import openpyxl
from django.conf import settings
from django.template.defaultfilters import slugify
import os
from django.apps import apps


def run():

    carregats, errors = [], []
    
    # Per cada fitxer, per aquest ordre ja que estan referenciats     
    fitxers = ['provincia','consell','municipi']

    # Per cada fitxer 
    for fitxer in fitxers:

        if settings.DEBUG:
            print(f"Fitxer: {fitxer}")

        carregats_aux, errors_aux = load_excel(fitxer)
        carregats += carregats_aux
        errors += errors_aux

    # Tornem els fitxers carregats
    return carregats, errors


def load_excel(fitxer):

    carregats, errors = [], []
    
    file_name = f"{fitxer}.xlsx"

    excel_file = os.path.join(
        settings.BASE_DIR, "geografia/ExcelsUpload/", file_name)
    existeix = os.path.exists(excel_file)

    if settings.DEBUG:
        trobat = "(fitxer trobat)" if existeix else "**No Trobat**"
        print(f"- file_name: {file_name} {trobat}")

    # Si no existeix saltem al següent
    if not existeix:
        return carregats, errors

    wb = openpyxl.load_workbook(filename=excel_file, data_only=True)

    # Cada excel te una sola pestanya    
    carregats_aux, errors_aux = carrega_pestanya(wb, file_name)
    carregats += carregats_aux
    errors += errors_aux

    # Gravem el nou excel i l'afegim a la llista
    return carregats, errors


def carrega_pestanya(wb, file_name):

    # DAVID aqui, ara hem de caregar cada fitxer la model corresponent-
    
    carregats, errors = carrega_pestanya_anual(dataset, wb, file_name)
    carregats_mensuals, errors_mensuals = carrega_pestanya_mensual(
        dataset, wb, file_name)

    return carregats + carregats_mensuals, errors + errors_mensuals

def carrega_pestanya_anual(dataset, wb, file_name):

    carregats, errors = [], []

    # Creem la capcelera amb la columna any
    capcelera = ['any']

    # Cada mètrica dataentry és una columna del fitxer.
    tots_els_dataentry = [
        metrica
        for metrica in dataset.metrica_set.all()
        if (metrica.font_de_dades == Metrica.DATAENTRY and
            metrica.actualitzacio == Metrica.ANUAL)
    ]
    for metrica in tots_els_dataentry:
        capcelera.append(metrica.label)

    if not bool(tots_els_dataentry):
        if settings.DEBUG:
            print(f"  - dataset anual: {dataset.nom} (no té data entries)")
        return carregats, errors

    # Cada dataset serà una pestanya de l'excel
    # Carregar pestanya
    sheet = dataset.get_short_model_name()
    if sheet not in wb.sheetnames:
        msg = f"No trobada la pestanya: {sheet} dins {file_name}"
        errors.append(msg)
        if settings.DEBUG:
            print(
                f"  - dataset anual: {dataset.nom} "
                f"**error, no trobada pestanya {sheet}**")
        return carregats, errors
    ws = wb.get_sheet_by_name(sheet)

    # Comprovar que hi ha totes les mètriques
    n = len(capcelera)
    found_headers = [cell.value for cell in ws[1][:n]]
    if found_headers != capcelera:
        msg = f"""A la pestanya {sheet} de {file_name}, no es
         corresponen les mètriques. Trobat {found_headers}
         i s'esperava {capcelera}"""
        errors.append(msg)
        if settings.DEBUG:
            print(
                f"  - dataset anual: {dataset.nom} "
                f"**error, a {sheet} no es corresponen les mètriques**")
        return carregats, errors

    # Cerco la classe model
    model_name = dataset.get_model_name()
    app_name = dataset.categoria.area.get_app_name("stage")
    Model = apps.get_model(app_label=app_name, model_name=model_name)

    # Esborro dades anteriors
    Model.objects.all().delete()

    # Carrego excel
    for row in list(ws.rows)[1:]:
        if row[0].value is None:
            break
        model = Model()
        cells = [cell for cell in row[:n]]
        data = dict(zip(capcelera, cells))
        model.any_dels_fets = data['any'].value

        for metrica in tots_els_dataentry:
            value = data[metrica.label].value
            propietat = metrica.get_metrica_anual_name()
            propietat_estimat = metrica.get_metrica_estimat_name()
            es_estimat = data[metrica.label].font.italic

            setattr(model, propietat, value)
            setattr(model, propietat_estimat, es_estimat)

        model.save()

    carregats += [f"{file_name} {sheet}"]

    if settings.DEBUG:
        amb_errors = " amb errors" if bool(errors) else "sense errors"
        print(
            f"  - dataset anual: {dataset.nom} "
            f"**carregat {sheet} ({amb_errors})**")

    return carregats, errors


def carrega_pestanya_mensual(dataset, wb, file_name):

    carregats, errors = [], []

    # Creem la capcelera amb la columna any
    capcelera = ['any', 'mes']

    # Cada mètrica dataentry és una columna del fitxer.
    tots_els_dataentry = [
        metrica
        for metrica in dataset.metrica_set.all()
        if (metrica.font_de_dades == Metrica.DATAENTRY and
            metrica.actualitzacio == Metrica.MENSUAL)
    ]
    te_mensuals = any(
        metrica
        for metrica in dataset.metrica_set.all()
        if metrica.actualitzacio == Metrica.MENSUAL
    )
    for metrica in tots_els_dataentry:
        capcelera.append(metrica.label)

    if not bool(tots_els_dataentry):
        if te_mensuals and settings.DEBUG:
            print(f"  - dataset mensual: {dataset.nom} (no té data entries)")
        return carregats, errors

    # Cada dataset serà una pestanya de l'excel
    # Carregar pestanya
    sheet = dataset.get_short_model_name() + "_xmes"
    if sheet not in wb.sheetnames:
        msg = f"No trobada la pestanya: {sheet} dins {file_name}"
        errors.append(msg)
        return carregats, errors
    ws = wb.get_sheet_by_name(sheet)

    # Comprovar que hi ha totes les mètriques
    n = len(capcelera)
    found_headers = [cell.value for cell in ws[1][:n]]
    if found_headers != capcelera:
        msg = f"""A la pestanya {sheet} de {file_name}, no es
         corresponen les mètriques. Trobat {found_headers}
         i s'esperava {capcelera}"""
        errors.append(msg)
        print(
            f"  - dataset anual: {dataset.nom} "
            f"**error, a {sheet} no es corresponen les mètriques**")
        return carregats, errors

    # Cerco la classe model
    mensual_model_name = dataset.get_model_name() + "_mensual"
    app_name = dataset.categoria.area.get_app_name("stage")
    MensualModel = apps.get_model(
        app_label=app_name,
        model_name=mensual_model_name)
    anual_model_name = dataset.get_model_name()
    AnualModel = apps.get_model(
        app_label=app_name,
        model_name=anual_model_name)

    # Esborro dades anteriors
    MensualModel.objects.all().delete()

    # Carrego excel
    for row in list(ws.rows)[1:]:
        if row[0].value is None:
            break
        model = MensualModel()
        cells = [cell for cell in row[:n]]
        data = dict(zip(capcelera, cells))
        model.mes_dels_fets = data['mes'].value

        # busco o creo el mestre (any)
        any_dels_fets = data['any'].value
        anualmodel, _ = AnualModel.objects.get_or_create(
            any_dels_fets=any_dels_fets)
        model.any_dels_fets = anualmodel

        # assigno valors a les propietats
        for metrica in tots_els_dataentry:
            value = data[metrica.label].value
            propietat = metrica.get_metrica_mensual_name()
            propietat_estimat = metrica.get_metrica_estimat_name()
            es_estimat = data[metrica.label].font.italic

            setattr(model, propietat, value)
            setattr(model, propietat_estimat, es_estimat)

        model.save()

    carregats += [f"{file_name} {sheet}"]

    if settings.DEBUG:
        amb_errors = " amb errors" if bool(errors) else "sense errors"
        print(
            f"  - dataset mensual: {dataset.nom} "
            f"**carregat {sheet} ({amb_errors})**")

    return carregats, errors
