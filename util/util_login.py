import json
from util.mostrar_mensajes import mostrar_error

file_path = 'file_configuracion/users.json'

def __cargar_configuracion(seccion_buscada=None):
    """
    Carga la configuración desde el archivo JSON. Si se proporciona `seccion_buscada`,
    devuelve solo esa sección, si no, devuelve toda la configuración.
    """
    try:
        with open(file_path, 'r') as archivo:
            configuracion = json.load(archivo)

        if seccion_buscada:
            if seccion_buscada in configuracion:
                return configuracion[seccion_buscada]
            else:
                return None
        else:
            return configuracion
    except FileNotFoundError:
        mostrar_error(f"Error: No se encontró el archivo de configuración en '{file_path}'.")
        return None
    except json.JSONDecodeError as e:
        mostrar_error(f"Error al leer el archivo JSON: {str(e)}")
        return None


def login_principal(usuario_entrada: str, contrasena_entrada: str):
    """
    Verifica las credenciales de un usuario en el archivo de configuración.
    Si las credenciales son correctas, devuelve True y los datos del usuario.
    """
    usuarios = __cargar_configuracion("users")
    if usuarios:
        for usuario, datos in usuarios.items():
            if datos["username"] == usuario_entrada and datos["password"] == contrasena_entrada:
                return True, {
                    "username": datos["username"],
                    "password": datos["password"],
                    "role": datos["role"]
                }
    return False, {}
