# Documentació

## FrontEnd: scss

* El css el gestionem amb scss, tenim un compilador de scss que és `django-libsass`. A continuació s'exposa el css que fem servir:

### Icones

* Fem servir fontawesome. Tenim ara la versió 6.4.0 by @fontawesome - https://fontawesome.com - License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License)
* Tenim els fonts copiats a [static/fontawesome](./../src/static/fontawesome)
* S'inclouen gràcies als includes que trobem dins [theme.css](./../src/static/theme.scss)

### Bootstrap

* Tenim copiats els fonts de bootstrap 5.3.0 a  [static/bootstrap](../src/static/bootstrap)
* S'inclouen gràcies als includes que trobem dins [theme.css](./../src/static/theme.scss)

### Bootswatch

* Són temes de Bootstrap. https://bootswatch.com/
* S'inclouen gràcies als includes que trobem dins [theme.css](./../src/static/theme.scss)
* MIT License.

## Backend

### crispy-bootstrap5

* Llibreria per crear els formularis des del backend.

### easy-thumbnails

* Llibreria python per processar els fitxers d'imatges.
* Exemples i info: https://easy-thumbnails.readthedocs.io/en/latest/usage/#overview

## Backend: Testing

* Fem servir: pytest, Faker i factory-boy. Aquestes darreres per crear els Mocks de les classes.
* Mirar els fitxers `factories.py` de les aplicacions. Exemple: [espais/factories.py](../src/espais/factories.py)
