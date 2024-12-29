import json

class ConfiguracionBaseDatos:
    """
    Clase base para gestionar la configuración de bases de datos.

    Esta clase proporciona métodos para cargar y actualizar la configuración de bases de datos
    desde un archivo JSON.

    Atributos:
        ruta_archivo (str): Ruta del archivo JSON que contiene la configuración de la base de datos.

    Métodos:
        cargar_configuracion(tipo_base_datos): Carga la configuración de un tipo de base de datos desde el archivo JSON.
        _actualizar_configuracion(tipo_base_datos, nueva_configuracion): Actualiza la configuración de un tipo de base de datos en el archivo JSON.
    """
    def __init__(self, ruta_archivo="file_configuracion/bbdd.json"):
        """
        Inicializa la clase con la ruta al archivo de configuración.

        Args:
            ruta_archivo (str): Ruta al archivo JSON que contiene la configuración de la base de datos.
        """
        self.ruta_archivo = ruta_archivo

    def cargar_configuracion(self, tipo_base_datos):
        """
        Carga la configuración de un tipo de base de datos específico desde el archivo JSON.

        Args:
            tipo_base_datos (str): El tipo de base de datos para cargar la configuración.

        Returns:
            dict, str: La configuración del tipo de base de datos o un mensaje de error.
        """
        try:
            with open(self.ruta_archivo, 'r') as archivo:
                configuracion = json.load(archivo)

            if tipo_base_datos not in configuracion:
                return None, f"Error: No se encontró configuración para '{tipo_base_datos}'."

            return configuracion.get(tipo_base_datos), None

        except FileNotFoundError as error:
            return None, f"Error: No se encontró el archivo de configuración en '{self.ruta_archivo}'. Detalles: {error}"
        except json.JSONDecodeError as error:
            return None, f"Error al leer el archivo JSON: {error}"
        except Exception as error:
            return None, f"Error inesperado: {error}"

    def _actualizar_configuracion(self, tipo_base_datos, nueva_configuracion):
        """
        Actualiza la configuración de un tipo de base de datos específico en el archivo JSON.

        Args:
            tipo_base_datos (str): El tipo de base de datos a actualizar.
            nueva_configuracion (dict): La nueva configuración a añadir al archivo.

        Returns:
            bool, str: True si la actualización fue exitosa, False y un mensaje de error en caso contrario.
        """
        try:
            with open(self.ruta_archivo, 'r') as archivo:
                configuracion = json.load(archivo)

            if tipo_base_datos not in configuracion:
                return False, f"Error: No se encontró la configuración para '{tipo_base_datos}' en el archivo."

            configuracion[tipo_base_datos].update(nueva_configuracion)

            with open(self.ruta_archivo, 'w') as archivo:
                json.dump(configuracion, archivo, indent=4)

            return True, None

        except FileNotFoundError as error:
            return False, f"Error: No se encontró el archivo de configuración en '{self.ruta_archivo}'. Detalles: {error}"
        except json.JSONDecodeError as error:
            return False, f"Error al leer el archivo JSON: {error}"
        except PermissionError as error:
            return False, f"Error de permisos al acceder al archivo: {error}"
        except Exception as error:
            return False, f"Error inesperado: {error}"
