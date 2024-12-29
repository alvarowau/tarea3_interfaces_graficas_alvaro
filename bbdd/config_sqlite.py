import sqlite3
import os
from sqlite3 import Error as error_sqlite
from typing import Tuple, Union

def test_bbdd_sqlite(config_nueva: dict) -> Tuple[bool, Union[None, str]]:
    """
    Intenta establecer una conexión con una base de datos SQLite utilizando la configuración proporcionada.

    Args:
        config_nueva (dict): Diccionario con la configuración de la base de datos SQLite.
                              Debe contener la clave 'file_path' con la ruta del archivo de base de datos.

    Returns:
        Tuple[bool, Union[None, str]]:
            - bool: True si la conexión fue exitosa, False en caso de error.
            - Union[None, str]: None si la conexión es exitosa, o un mensaje de error en caso de fallo.
    """
    if not os.path.isfile(config_nueva.get("file_path", "")):
        return False, "El archivo especificado no existe"

    conexion = None
    try:
        conexion = sqlite3.connect(config_nueva["file_path"])
        cursor = conexion.cursor()
        cursor.execute("SELECT 1;")
        return True, None
    except error_sqlite as err:
        return False, str(err)
    finally:
        if conexion:
            conexion.close()
