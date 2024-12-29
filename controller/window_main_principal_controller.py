from datetime import datetime, date

from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QMainWindow, QHeaderView, QAbstractItemView, QDialog

from controller.windows_reserva_controller import ControladorReserva
from dao.reserva_dao import ReservaDAO
from dao.salon_dao import SalonDAO
from dao.tipo_cocina_dao import TipoCocinaDAO
from dao.tipo_reserva_dao import TipoReservaDAO
from files_ui.ui_windows_main_principal import Ui_windows_main_principal
from util.mostrar_mensajes import mostrar_error


def _es_editable(estado):
    """Verifica si una reserva es editable basado en su estado."""
    return estado == "Editar"

class ControladorReservas(QMainWindow):
    salon_mapping = {}

    def __init__(self, salon_dao: SalonDAO, reserva_dao: ReservaDAO, tipo_reserva_dao: TipoReservaDAO,
                 tipo_cocina_dao: TipoCocinaDAO):
        """Inicializa el controlador de reservas con los DAOs necesarios y configura la UI.

        Args:
            salon_dao (SalonDAO): DAO para manejar salones.
            reserva_dao (ReservaDAO): DAO para manejar reservas.
            tipo_reserva_dao (TipoReservaDAO): DAO para manejar tipos de reserva.
            tipo_cocina_dao (TipoCocinaDAO): DAO para manejar tipos de cocina.
        """
        super().__init__()
        try:
            self.ui = Ui_windows_main_principal()
            self.ui.setupUi(self)
            self.setWindowTitle("Centro de reservas")
            self.salon_dao = salon_dao
            self.reserva_dao = reserva_dao
            self.tipo_reserva_dao = tipo_reserva_dao
            self.tipo_cocina_dao = tipo_cocina_dao

            self._inicializar_ui()
            self._conectar_senates()
            self.ui.a_tableView_table.setColumnHidden(5, True)
            self.cargar_salones()
        except Exception as e:
            mostrar_error("Error al iniciar la app", str(e))

    def _inicializar_ui(self):
        """Configura la interfaz de usuario inicial."""
        try:
            self.modelo_tabla = QStandardItemModel()
            self.modelo_tabla.setHorizontalHeaderLabels([
                "Fecha", "Persona", "Teléfono", "Tipo de Reserva", "Acción", "ID Reserva"
            ])
            self.ui.a_tableView_table.setModel(self.modelo_tabla)
            self.ui.a_tableView_table.resizeColumnsToContents()
            self.ui.a_tableView_table.horizontalHeader().setStretchLastSection(True)
            self.ui.a_tableView_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.ui.a_tableView_table.setColumnHidden(5, True)
            self.ajustar_tamanio_columnas()
        except Exception as e:
            mostrar_error("Error al inicializar UI", str(e))

    def _conectar_senates(self):
        """Conecta las señales de los widgets a los manejadores."""
        try:
            self.ui.a_listWidget_list.currentTextChanged.connect(self.cargar_reservas)
            self.ui.a_pushButton_new_reserva.clicked.connect(self._mostrar_ventana_reserva)
            self.ui.a_pushButton_modi_reserva.clicked.connect(self.modificar_reserva)
            self.ui.a_pushButton_exit.clicked.connect(self.close)
            self.ui.a_tableView_table.doubleClicked.connect(self.manejar_doble_click)
        except Exception as e:
            mostrar_error("Error al conectar señales", str(e))

    def cargar_salones(self):
        """Carga los salones desde la base de datos y actualiza la lista de salones."""
        try:
            salones, error = self.salon_dao.get_all_salones()
            if error:
                mostrar_error("Error al obtener salones", str(error))
                return

            self.salon_mapping = {salon.salon_id: salon.nombre for salon in salones}
            nombres_salones = ["TODOS"] + [salon.nombre for salon in salones]
            self.ui.a_listWidget_list.addItems(nombres_salones)
        except Exception as e:
            mostrar_error("Error al cargar salones", str(e))

    def cargar_reservas(self, salon_seleccionado):
        """Carga las reservas según el salón seleccionado."""
        self._reiniciar_modelo_tabla()

        if salon_seleccionado == "TODOS":
            self._mostrar_todas_las_reservas()
        else:
            salon_id = self._obtener_id_salon_por_nombre(salon_seleccionado)
            if salon_id:
                self._mostrar_todas_las_reservas(salon_id)
            else:
                mostrar_error("No se pudo hacer la filtración por id")

    def _obtener_id_salon_por_nombre(self, nombre_salon):
        """Obtiene el ID de un salón dado su nombre."""
        return next((key for key, value in self.salon_mapping.items() if value == nombre_salon), None)

    def _mostrar_todas_las_reservas(self, salon_id=None):
        """Muestra todas las reservas o las reservas de un salón específico."""
        reservas, error = (
            self.reserva_dao.get_all_reservas_by_salon_id(salon_id)
            if salon_id
            else self.reserva_dao.get_all_reservas()
        )
        if error:
            mostrar_error("Error al obtener reservas", str(error))
            return

        filas = self._convertir_reservas_a_filas(reservas)
        self._mostrar_reservas(filas)

    def _convertir_reservas_a_filas(self, reservas):
        """Convierte las reservas a formato de filas para la tabla."""
        hoy = datetime.now().date()
        tipos_reserva = self._obtener_tipos_reserva()

        return [
            [
                self._formatear_fecha(res.fecha),
                res.persona,
                res.telefono,
                tipos_reserva.get(res.tipo_reserva_id, "Desconocido"),
                "Editar" if res.fecha >= hoy else "No editable",
                str(res.reserva_id)
            ]
            for res in reservas
        ]

    def _obtener_tipos_reserva(self):
        """Obtiene los tipos de reserva desde la base de datos."""
        return {res.tipo_reserva_id: res.nombre for res in self.tipo_reserva_dao.get_all_tipo_reservas()}

    def _formatear_fecha(self, fecha_entrada):
        """Formatea la fecha en formato dd/mm/aaaa."""
        if isinstance(fecha_entrada, (datetime, date)):
            return fecha_entrada.strftime("%d/%m/%Y")
        return datetime.strptime(fecha_entrada, "%Y-%m-%d").strftime("%d/%m/%Y")

    def _mostrar_reservas(self, filas):
        """Muestra las filas de reservas en la tabla."""
        self._reiniciar_modelo_tabla()
        for fila in filas:
            self.modelo_tabla.appendRow([QStandardItem(str(col)) for col in fila])
        self.ui.a_tableView_table.setColumnHidden(5, True)

    def _reiniciar_modelo_tabla(self):
        """Reinicia el modelo de la tabla con los encabezados predefinidos."""
        self.modelo_tabla.clear()
        self.modelo_tabla.setHorizontalHeaderLabels([
            "Fecha", "Persona", "Teléfono", "Tipo de Reserva", "Acción", "ID Reserva"
        ])

    def _mostrar_ventana_reserva(self, reserva_modificacion=None, es_editar=False):
        """Muestra la ventana de reserva.

        Args:
            reserva_modificacion: Datos de la reserva a modificar (si aplica).
            es_editar (bool): Indica si la acción es de edición.
        """
        try:
            self.controlador = ControladorReserva(
                reserva_dao=self.reserva_dao,
                tipo_reserva_dao=self.tipo_reserva_dao,
                salon_dao=self.salon_dao,
                tipo_cocina_dao=self.tipo_cocina_dao,
                reserva_modificacion=reserva_modificacion,
                es_editar=es_editar
            )
            if not isinstance(self.controlador, QDialog):
                raise TypeError("El controlador debe heredar de QDialog para ser modal.")

            self.controlador.setModal(True)
            self.controlador.exec_()
        except Exception as e:
            mostrar_error("Error al mostrar ventana de reserva", str(e))

    def modificar_reserva(self):
        """Modifica la reserva seleccionada."""
        seleccion = self.ui.a_tableView_table.selectedIndexes()
        if not seleccion:
            mostrar_error("Por favor, seleccione una reserva para editar.")
            return

        reserva_id = self._obtener_id_reserva_seleccionada(seleccion)
        columna4 = self._obtener_estado_reserva_seleccionada(seleccion)

        if _es_editable(columna4):
            reserva = self._obtener_reserva_por_id(reserva_id)
            if reserva:
                self._mostrar_ventana_reserva(reserva_modificacion=reserva, es_editar=True)
        else:
            mostrar_error("No se puede editar con fecha posterior")

    def manejar_doble_click(self, indice):
        """Maneja el evento de doble clic en una fila."""
        reserva_id = self.modelo_tabla.item(indice.row(), 5).text()
        columna4 = self.modelo_tabla.item(indice.row(), 4).text()

        if _es_editable(columna4):
            reserva = self._obtener_reserva_por_id(reserva_id)
            if reserva:
                self._mostrar_ventana_reserva(reserva_modificacion=reserva, es_editar=True)
        else:
            mostrar_error("No se puede editar con fecha posterior")

    def _obtener_reserva_por_id(self, reserva_id):
        """Obtiene una reserva por su ID.

        Args:
            reserva_id: ID de la reserva a buscar.

        Returns:
            Reserva encontrada o None si ocurre un error.
        """
        reserva, error = self.reserva_dao.get_reserva_by_id(reserva_id)
        if error or not reserva:
            mostrar_error("No se ha encontrado la reserva para editar.")
            return None
        return reserva

    def _obtener_id_reserva_seleccionada(self, seleccion):
        """Obtiene el ID de la reserva seleccionada en la tabla."""
        return self.modelo_tabla.item(seleccion[0].row(), 5).text()

    def _obtener_estado_reserva_seleccionada(self, seleccion):
        """Obtiene el estado de la reserva seleccionada en la tabla."""
        return self.modelo_tabla.item(seleccion[0].row(), 4).text()

    def ajustar_tamanio_columnas(self):
        """Ajusta el tamaño de las columnas de la tabla."""
        header = self.ui.a_tableView_table.horizontalHeader()
        for i in range(self.modelo_tabla.columnCount()):
            header.setSectionResizeMode(i, QHeaderView.Stretch)
