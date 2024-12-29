import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QObject, Signal
from controller.login_controller import ControladorLogin
from controller.windows_edit_conexion_controller import ControladorEditWindows
from controller.window_main_principal_controller import ControladorReservas
from dao.reserva_dao import ReservaDAO
from dao.salon_dao import SalonDAO
from dao.tipo_reserva_dao import TipoReservaDAO
from dao.tipo_cocina_dao import TipoCocinaDAO


# Variables globales para los DAOs
salon_dao: SalonDAO = None
reserva_dao: ReservaDAO = None
tipo_reserva_dao: TipoReservaDAO = None
tipo_cocina_dao: TipoCocinaDAO = None


class ControladorAplicacion(QObject):
    configuracion_completada = Signal(dict)  # Señal para enviar el diccionario de DAOs


def manejar_login(app):
    """Método que maneja la ventana de login y devuelve True si el login es exitoso."""
    login_window = QMainWindow()
    controlador_login = ControladorLogin(login_window)

    # Mostrar la ventana de login
    login_window.show()

    # Ejecutar la aplicación para esperar la acción del usuario
    app.exec()

    # Devolver el resultado del login
    return controlador_login.obtener_resultado_login()


def manejar_configuracion(app, controlador):
    """Método que maneja la ventana de configuración y emite los DAOs como señal."""
    global salon_dao, reserva_dao, tipo_reserva_dao, tipo_cocina_dao

    ventana_configuracion = ControladorEditWindows()

    # Conectar la señal de configuración_exitosa a una función local para asignar los DAOs
    def asignar_daos(daos):
        global salon_dao, reserva_dao, tipo_reserva_dao, tipo_cocina_dao
        salon_dao = daos["salon_dao"]
        reserva_dao = daos["reserva_dao"]
        tipo_reserva_dao = daos["tipo_reserva_dao"]
        tipo_cocina_dao = daos["tipo_cocina_dao"]

        # Emitir la señal indicando que la configuración está completa
        controlador.configuracion_completada.emit(daos)

        # Cerrar la ventana y finalizar el bucle de eventos
        ventana_configuracion.close()
        app.quit()

    ventana_configuracion.configuracion_exitosa.connect(asignar_daos)

    # Mostrar la ventana de configuración
    ventana_configuracion.show()

    # Ejecutar la aplicación para esperar la acción del usuario
    app.exec()


def iniciar_ventana_principal(app):
    """Inicializa la ventana principal de ControladorReservas."""
    global salon_dao, reserva_dao, tipo_reserva_dao, tipo_cocina_dao

    controller = ControladorReservas(
        salon_dao=salon_dao,
        reserva_dao=reserva_dao,
        tipo_reserva_dao=tipo_reserva_dao,
        tipo_cocina_dao=tipo_cocina_dao
    )  # Inicializa el controlador
    controller.show()  # Muestra la ventana principal

    # Ejecutar la aplicación
    sys.exit(app.exec())


def main():
    app = QApplication(sys.argv)

    # Crear el controlador de la aplicación
    controlador = ControladorAplicacion()

    # Conectar la señal configuracion_completada a sys.exit para finalizar la aplicación
    controlador.configuracion_completada.connect(lambda _: app.quit())

    # Llamar al método de login
    if manejar_login(app):

        # Manejar la configuración
        manejar_configuracion(app, controlador)

        # Iniciar la ventana principal
        iniciar_ventana_principal(app)

    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
