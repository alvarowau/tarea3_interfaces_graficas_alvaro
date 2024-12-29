from config.configuracion_base_datos import ConfiguracionBaseDatos
from bbdd.data_base_manager import DatabaseManager
from dao.reserva_dao import ReservaDAO
from dao.salon_dao import SalonDAO
from dao.tipo_cocina_dao import TipoCocinaDAO
from dao.tipo_reserva_dao import TipoReservaDAO
from util.mostrar_mensajes import mostrar_error

def cargar_configuracion_db(data_base):
    """
    Carga la configuración de la base de datos desde un archivo JSON.

    Args:
        data_base (str): El tipo de base de datos a cargar (mysql, sqlite).

    Returns:
        dict: La configuración de la base de datos o None si ocurre un error.
    """
    config_database = ConfiguracionBaseDatos()
    config, err = config_database.cargar_configuracion(data_base)
    if err:
        mostrar_error("DIO ERROR")
        return None
    return config

def crear_conexion_mysql(mysql_config):
    """
    Crea una conexión a una base de datos MySQL.

    Args:
        mysql_config (dict): Configuración para la conexión a MySQL.

    Returns:
        DatabaseManager: Instancia de la clase DatabaseManager configurada para MySQL.
    """
    return DatabaseManager("mysql", **mysql_config)

def crear_conection_sqlite(sqlite_config):
    """
    Crea una conexión a una base de datos SQLite.

    Args:
        sqlite_config (dict): Configuración para la conexión a SQLite.

    Returns:
        DatabaseManager: Instancia de la clase DatabaseManager configurada para SQLite.
    """
    return DatabaseManager("sqlite", **sqlite_config)

def verificar_columnas(tabla_dao, columnas_esperadas):
    """
    Verifica si las columnas de una tabla coinciden con las esperadas.

    Args:
        tabla_dao (DAO): Objeto DAO para la tabla.
        columnas_esperadas (tuple): Lista de nombres de las columnas esperadas.

    Returns:
        bool, str: True si las columnas coinciden, False y un mensaje de error en caso contrario.
    """
    respuesta = tabla_dao.verificar_tabla()
    if not respuesta:
        return False, f"No existe la tabla {tabla_dao.nombre_tabla}."

    columnas_recibidas = []
    if tabla_dao.db_type == 'mysql':
        columnas_recibidas = [columna[0] for columna in tabla_dao.describe_tablas()]
    elif tabla_dao.db_type == 'sqlite':
        columnas_recibidas = [columna[1] for columna in tabla_dao.describe_tablas()]

    columnas_faltantes = set(columnas_esperadas) - set(columnas_recibidas)
    columnas_extra = set(columnas_recibidas) - set(columnas_esperadas)

    if columnas_faltantes or columnas_extra:
        return False, f"Las columnas no coinciden con las esperadas: faltantes {columnas_faltantes}, extra {columnas_extra}."

    return True, None

def probar_tipo_reserva(tipo_reserva_dao):
    """
    Realiza la prueba de verificación de la tabla 'Tipo Reserva' en la base de datos.

    Args:
        tipo_reserva_dao (DAO): Objeto DAO para la tabla 'Tipo Reserva'.

    Returns:
        bool, str: True si la tabla es correcta, False y un mensaje de error en caso contrario.
    """
    columnas_esperadas = ("tipo_reserva_id", "nombre", "requiere_jornadas", "requiere_habitaciones")
    success, error = verificar_columnas(tipo_reserva_dao, columnas_esperadas)
    if not success:
        return success, error

    existe_congreso = tipo_reserva_dao.existe_congreso()
    if existe_congreso == 1:
        return True, None
    else:
        return False, "No existe el tipo de reserva 'congreso'."

def probar_tipo_cocina(tipo_cocina_dao):
    """
    Realiza la prueba de verificación de la tabla 'Tipo Cocina' en la base de datos.

    Args:
        tipo_cocina_dao (DAO): Objeto DAO para la tabla 'Tipo Cocina'.

    Returns:
        bool, str: True si la tabla es correcta, False y un mensaje de error en caso contrario.
    """
    columnas_esperadas = ("tipo_cocina_id", "nombre")
    return verificar_columnas(tipo_cocina_dao, columnas_esperadas)

def probar_salon(salon_dao):
    """
    Realiza la prueba de verificación de la tabla 'Salon' en la base de datos.

    Args:
        salon_dao (DAO): Objeto DAO para la tabla 'Salon'.

    Returns:
        bool, str: True si la tabla es correcta, False y un mensaje de error en caso contrario.
    """
    columnas_esperadas = ("salon_id", "nombre")
    return verificar_columnas(salon_dao, columnas_esperadas)

def probar_reserva(reserva_dao):
    """
    Realiza la prueba de verificación de la tabla 'Reserva' en la base de datos.

    Args:
        reserva_dao (DAO): Objeto DAO para la tabla 'Reserva'.

    Returns:
        bool, str: True si la tabla es correcta, False y un mensaje de error en caso contrario.
    """
    columnas_esperadas = (
        'reserva_id', 'tipo_reserva_id', 'salon_id', 'tipo_cocina_id',
        'persona', 'telefono', 'fecha', 'ocupacion', 'jornadas', 'habitaciones'
    )
    return verificar_columnas(reserva_dao, columnas_esperadas)

def test_tablas_base_datos(tipo_reserva_dao, tipo_cocina_dao, salon_dao, reserva_dao):
    """
    Realiza las pruebas de verificación de las tablas en la base de datos.

    Args:
        tipo_reserva_dao (DAO): Objeto DAO para la tabla 'Tipo Reserva'.
        tipo_cocina_dao (DAO): Objeto DAO para la tabla 'Tipo Cocina'.
        salon_dao (DAO): Objeto DAO para la tabla 'Salon'.
        reserva_dao (DAO): Objeto DAO para la tabla 'Reserva'.

    Returns:
        bool, list: True si todas las tablas son correctas, False y una lista de errores en caso contrario.
    """
    tests = [
        ("Tipo Reserva", probar_tipo_reserva, tipo_reserva_dao ),
        ("Tipo Cocina", probar_tipo_cocina, tipo_cocina_dao),
        ("Salon", probar_salon, salon_dao),
        ("Reserva", probar_reserva, reserva_dao),
    ]

    errores = []

    for nombre, funcion, dao in tests:
        success, err = funcion(dao)
        if not success:
            errores.append(f"{nombre}: {err}")

    if not errores:
        return True, None
    else:
        return False, errores
