import sys, os

def resource_path(relative_path):
    """ Devuelve la ruta absoluta a un recurso, compatible con PyInstaller """
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
