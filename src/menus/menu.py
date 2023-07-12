from django.urls import NoReverseMatch, Resolver404, resolve, reverse
from django.template.defaultfilters import safe
from django.utils.translation import gettext as _

from menus.estructures import MenuItem, MenuPrint, MenuPrintItem

PERFIL_BIM = "bim"


def calcula_menu(user, path):

    if not user.is_authenticated:
        return

    perfil = _determina_perfil(user)
    menu_id, submenu_id, subsubmenu_id = _extreu_ids(path)
    arbre = _construeix_arbre(perfil)
    menu = _processa_arbre(arbre, menu_id, submenu_id, subsubmenu_id)

    return menu


def _determina_perfil(user):

    return PERFIL_BIM


def _extreu_ids(path):

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

    except (NoReverseMatch, Resolver404, ValueError):
        return novalue

    return menu_id, submenu_id, subsubmenu_id


def _construeix_arbre(perfil):

    espais = MenuItem(
            text=_("Els meus espais"),
            visible=True,
            viewprefix="llista",
            viewdefault="espais:espais__llista__blank",
            submenus=[]
        )

    validacions = MenuItem(
            text=_("Les meves validacions"),
            visible=True,
            viewprefix="xxx",
            viewdefault="admin:index",
            submenus=[]
        )

    arbre = [
        MenuItem(
            text=_("Espais i validacions"),
            visible=True,
            viewprefix="espais",
            viewdefault="espais:espais__llista__blank",
            submenus=[espais, validacions]
        ),
        MenuItem(
            text=_("Enquesta"),
            visible=True,
            viewprefix="enquesta",
            viewdefault="portal:enquesta__blank__blank",
            submenus=[]
        ),
        MenuItem(
            text=_("Admin"),
            visible=True,
            viewprefix="admin",
            viewdefault="admin:index",
            submenus=[]
        ),
    ]

    return arbre


def _processa_arbre(arbre, menu_id, submenu_id, subsubmenu_id):

    activarmenuusuari = (
        menu_id == 'usuaris' or
        menu_id == 'account'
    )

    itemsvisiblesnivell1 = [
        item for item in arbre if item.visible]
    primernivell = _calcula_primernivell(menu_id, itemsvisiblesnivell1)

    itemsvisiblesnivell2 = _getitemsvisiblesfrom(
        itemsvisiblesnivell1,
        menu_id)
    segonnivell = _calcula_segonnivell(submenu_id, itemsvisiblesnivell2)

    itemsvisiblesnivell3 = _getitemsvisiblesfrom(
        itemsvisiblesnivell2,
        submenu_id)
    tercernivell = _calcula_tercernivell(subsubmenu_id, itemsvisiblesnivell3)

    return MenuPrint(
        activarmenuusuari=activarmenuusuari,
        primernivell=primernivell,
        segonnivell=segonnivell,
        tercernivell=tercernivell)


def _calcula_primernivell(menu_id, itemsvisiblesnivell1):

    primernivell = []
    for item in itemsvisiblesnivell1:
        label = safe(item.text)
        actiu = item.viewprefix == menu_id
        url = reverse(item.viewdefault)
        menuprintitem = MenuPrintItem(text=label, actiu=actiu, url=url)
        primernivell.append(menuprintitem)
    return primernivell


def _calcula_segonnivell(submenu_id, itemsvisiblesnivell2):

    segonnivell = []
    for item in itemsvisiblesnivell2:
        label = safe(item.text)
        actiu = item.viewprefix == submenu_id
        url = reverse(item.viewdefault)
        menuprintitem = MenuPrintItem(text=label, actiu=actiu, url=url)
        segonnivell.append(menuprintitem)
    return segonnivell


def _calcula_tercernivell(subsubmenu_id, itemsvisiblesnivell3):

    tercernivell = []
    for item in itemsvisiblesnivell3:
        label = safe(item.text)
        actiu = item.viewprefix == subsubmenu_id
        url = reverse(item.viewdefault)
        menuprintitem = MenuPrintItem(text=label, actiu=actiu, url=url)
        tercernivell.append(menuprintitem)
    return tercernivell


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
