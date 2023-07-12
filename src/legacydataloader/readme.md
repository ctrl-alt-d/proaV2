Execució:

```
rm db.sqlite3
./manage.py makemigrations
./manage.py migrate
export DJANGO_SUPERUSER_PASSWORD=i; ./manage.py createsuperuser --noinput --username d@dani.com --email  d@dani.com 
./manage.py loadlegacy
./manage.py excelsgeografia2model
```


```
from legacydataloader.relacionarpreguntatipus import relacionapreguntaambtipus
relacionapreguntaambtipus()
```

Items a carregar:

* [x] Discapacitats
* [x] Preguntes
* [x] Respostes
* [x] Tipus d'Espai
* [x] Agrupació de preguntes (dins tipus espai)
* [x] PreguntaDinsTipusEspai: Relació Pregunta-Agrupació (amb camp importància)
* [x] PuntuacioMaxima (d'una pregunta per una discapacitat) 
* [x] AportacioResposta (percentatge que aporta cada resposta respecte la PuntuacioMaxima)
* [x] Exclusions