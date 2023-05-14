from django.urls import NoReverseMatch, Resolver404, resolve, reverse
from django.template.defaultfilters import safe
from django.utils.translation import gettext as _

from menus.estructures import MenuItem, MenuPrint, MenuPrintItem

PERFIL_BIM = "bim"


class classebuida(object):
    pass


def calcula_menu(user, path):

    if not user.is_authenticated:
        return

    perfil = determina_perfil(user)
    menu_id, submenu_id, subsubmenu_id = extreu_ids(path)
    arbre = construeix_arbre(perfil)
    menu = processa_arbre(arbre, menu_id, submenu_id, subsubmenu_id)

    return menu


def determina_perfil(user):

    return PERFIL_BIM


def extreu_ids(path):
    novalue = (None, None, None)
    try:
        nom_path = resolve(path).url_name

        if not nom_path:
            return novalue

        if nom_path.startswith("account_"):
            menu_id, submenu_id, subsubmenu_id = (
                "usuaris", "canvia", "password")
        else:
            menu_id, submenu_id, subsubmenu_id = nom_path.split('__')[:3]

    except (NoReverseMatch, Resolver404):
        return novalue

    return menu_id, submenu_id, subsubmenu_id


def construeix_arbre(perfil):

    arbre = [
        MenuItem(
            text=_("Pàgina Principal"),
            visible=True,
            viewprefix="home",
            viewdefault="home__blank__blank",
            submenus=[]
        )
    ]

    return arbre


def processa_arbre(arbre, menu_id, submenu_id, subsubmenu_id):
    primernivell = []
    segonnivell = []
    tercernivell = []

    itemsvisiblesnivell1 = [
        item for item in arbre if item.visible]
    
    itemsvisiblesnivell2 = _getitemsvisiblesfrom(
        itemsvisiblesnivell1,
        menu_id)
    
    itemsvisiblesnivell3 = _getitemsvisiblesfrom(
        itemsvisiblesnivell2,
        submenu_id)

    for item in itemsvisiblesnivell1:

        label = safe(item.text)
        actiu = item.viewprefix == menu_id
        url = reverse(item.viewdefault)
        menuprintitem = MenuPrintItem(text=label, actiu=actiu, url=url)
        primernivell.append(menuprintitem)

    for item in itemsvisiblesnivell2:

        label = safe(item.text)
        actiu = item.viewprefix == submenu_id
        url = reverse(item.viewdefault)
        menuprintitem = MenuPrintItem(text=label, actiu=actiu, url=url)
        segonnivell.append(menuprintitem)

    for item in itemsvisiblesnivell3:

        label = safe(item.text)
        actiu = item.viewprefix == subsubmenu_id
        url = reverse(item.viewdefault)
        menuprintitem = MenuPrintItem(text=label, actiu=actiu, url=url)
        tercernivell.append(menuprintitem)

    return MenuPrint(
        primernivell=primernivell,
        segonnivell=segonnivell,
        tercernivell=tercernivell)


def _getitemsvisiblesfrom(items, id):
    itemsactius = [item for item in items if item.viewprefix == id]

    # no hi ha item actiu
    if not itemsactius:
        return []

    # hi ha item actiu
    return [
        item
        for item in (itemsactius[0].submenus or [])
        if item.visible
    ]
