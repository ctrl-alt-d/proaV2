from .frontend import CSSAmplades


def utils(request):

    return {
        'CSSAmpladaMitja': CSSAmplades.MITJA,
        'CSSAmpladaPetit': CSSAmplades.PETIT,
    }
