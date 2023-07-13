Càrrega:

```
. ./vev/bin/activate
cd src
rm db.sqlite3
./manage.py makemigrations
./manage.py migrate
export DJANGO_SUPERUSER_PASSWORD=i; ./manage.py createsuperuser --noinput --username gestor@mailinator.com --email gestor@mailinator.com
./manage.py loadlegacy
./manage.py excelsgeografia2model
```

Testos:

```
pytest
```
