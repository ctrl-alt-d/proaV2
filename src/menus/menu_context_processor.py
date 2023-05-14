from .menu import calcula_menu


def menu(request):

    return {
        'menu': calcula_menu(request.user, request.path_info)
    }
