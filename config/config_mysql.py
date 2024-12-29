from config.configuracion_base_datos import ConfiguracionBaseDatos
from config.configuracion_mysql import ConfiguracionMysql

class UtilConfigMysqlDatos(ConfiguracionBaseDatos):
    """
    Clase para gestionar la configuración de MySQL.

    Esta clase hereda de `ConfiguracionBaseDatos` y permite cargar y actualizar
    la configuración de MySQL desde un archivo JSON. También valida que la configuración
    contenga las claves necesarias.

    Atributos:
        CLAVES_REQUERIDAS (set): Conjunto de claves requeridas para la configuración de MySQL.
        configuracion_actual (ConfiguracionMysql): Objeto que almacena la configuración actual de MySQL.

    Métodos:
        cargar(): Carga la configuración de MySQL y crea un objeto `ConfiguracionMysql`.
        actualizar(): Actualiza la configuración de MySQL utilizando un objeto `ConfiguracionMysql`.
        _validar_configuracion(): Valida que la configuración contenga las claves requeridas.
    """
    CLAVES_REQUERIDAS = {"host", "port", "user", "password", "database"}

    def __init__(self, ruta_archivo="file_configuracion/bbdd.json"):
        """
        Inicializa la clase con el archivo de configuración especificado.

        Parámetros:
            ruta_archivo (str): Ruta del archivo JSON que contiene la configuración de la base de datos.
        """
        super().__init__(ruta_archivo)
        self.configuracion_actual = None

    def cargar(self):
        """
        Carga la configuración de MySQL y crea un objeto `ConfiguracionMysql`.

        Retorna:
            Tuple[bool, Union[None, str]]: `True` si la carga fue exitosa, `False` y un mensaje de error en caso contrario.
        """
        configuracion, error = self.cargar_configuracion("mysql")
        if error:
            return False, error

        if not self._validar_configuracion(configuracion):
            return False, "Error: La configuración de MySQL no contiene las claves requeridas."

        self.configuracion_actual = ConfiguracionMysql.desde_diccionario(configuracion)
        return True, None

    def actualizar(self, nuevo_objeto_config: ConfiguracionMysql):
        """
        Actualiza la configuración de MySQL utilizando un objeto `ConfiguracionMysql`.

        Parámetros:
            nuevo_objeto_config (ConfiguracionMysql): Objeto con la nueva configuración de MySQL.

        Retorna:
            Tuple[bool, Union[None, str]]: `True` si la actualización fue exitosa, `False` y un mensaje de error en caso contrario.
        """
        if not isinstance(nuevo_objeto_config, ConfiguracionMysql):
            return False, "Error: El nuevo valor debe ser un objeto `ConfiguracionMysql`."

        nuevo_config_dict = nuevo_objeto_config.a_diccionario()

        if not self._validar_configuracion(nuevo_config_dict):
            return False, "Error: Las claves no coinciden con las requeridas."

        exito, mensaje = self._actualizar_configuracion("mysql", nuevo_config_dict)
        if exito:
            self.configuracion_actual = nuevo_objeto_config
        return exito, mensaje

    def _validar_configuracion(self, configuracion):
        """
        Valida que la configuración contenga las claves requeridas.

        Parámetros:
            configuracion (dict): Diccionario con la configuración de MySQL.

        Retorna:
            bool: `True` si la configuración contiene las claves requeridas, `False` en caso contrario.
        """
        if not isinstance(configuracion, dict):
            return False
        return self.CLAVES_REQUERIDAS <= set(configuracion.keys())
