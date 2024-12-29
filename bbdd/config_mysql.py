import mysql.connector
from mysql.connector import Error as err_mysql
from typing import Tuple, Union

def test_bbdd_mysql(config_nueva: dict) -> Tuple[bool, Union[None, err_mysql]]:
    """
    Establece una conexión con la base de datos MySQL utilizando la configuración proporcionada
    y devuelve el resultado de la conexión.

    Args:
        config_nueva (dict): Diccionario con la configuración necesaria para la conexión a MySQL,
                              como usuario, contraseña, host, base de datos, etc.

    Returns:
        Tuple[bool, Union[None, err_mysql]]: Retorna un valor booleano que indica si la conexión
                                             fue exitosa, junto con un posible error en caso de fallo.
                                             - True, None si la conexión fue exitosa.
                                             - False, err_mysql si ocurrió un error durante la conexión.
    """
    conexion = None
    try:
        conexion = mysql.connector.connect(**config_nueva)
        if conexion.is_connected():
            return True, None
        else:
            return False, None
    except err_mysql as err:
        return False, err
    finally:
        if conexion:
            conexion.close()

