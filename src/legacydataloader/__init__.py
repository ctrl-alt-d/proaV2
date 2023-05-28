from legacydataloader.agrupaciopreguntes import importagrupaciopreguntes
from legacydataloader.preguntes import importpreguntes
from legacydataloader.relacionarpreguntatipus import relacionapreguntaambtipus
from legacydataloader.discapacitats import importdiscapacitats

def run():
    importdiscapacitats()
    importpreguntes()
    importagrupaciopreguntes()
    relacionapreguntaambtipus()