import openpyxl
from django.conf import settings
from django.template.defaultfilters import slugify
import os
from django.apps import apps


def run():

    carregats, errors = [], []
    
    # Per cada model, tindrem un fitxer a carregar
    fitxers = ['Provincia','Comarca','Municipi']
    # fitxers = apps.all_models

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
    carregats_aux, errors_aux = carrega_fitxer(wb, file_name, fitxer)
    carregats += carregats_aux
    errors += errors_aux
    
    return carregats, errors

def carrega_fitxer(wb, file_name, fitxer):    
   
    carregats, errors = [], []    

   # Creem la capcelera
   # capcelera = []

    # Cerco el model a carregar, és el nom de l'excel a carregar sense l'extenció   
    Model = apps.get_model(model_name=fitxer)

    # Esborro dades anteriors d'aquest model
    Model.objects.all().delete()
    
    # Carrego la pestanya
    ws = wb.active
    # Nombre de columnes
    n = ws.max_column

    # Creem la capcelera
    # capcelera = []
    # found_headers = [cell.value for cell in ws[1][:n]]
    
    # Recuperem els valors de la capcelera que coincideixen amb els noms del items del model
    capcelera = [cell.value for cell in ws[1][:n]]
      
    # David aqui això no funcionarà . . . millorar. AQUI ! ! ! 
    #   
    # Carrego excel
    for row in list(ws.rows)[1:]:
        if row[0].value is None:
            break
        model = Model()
        cells = [cell for cell in row[:n]]
        data = dict(zip(capcelera, cells))        

        for columna in capcelera:
            value = data[columna].value
            propietat = columna
            
            setattr(model, propietat, value)            

        model.save()

    carregats += [f"{file_name}"]

    if settings.DEBUG:
        amb_errors = " amb errors" if bool(errors) else "sense errors"
        print(            
            f"**carregat {file_name} ({amb_errors})**")

    return carregats, errors
