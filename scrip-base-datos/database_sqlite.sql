-- Tabla para tipos de reserva
CREATE TABLE IF NOT EXISTS tipos_reservas (
    tipo_reserva_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    requiere_jornadas INTEGER NOT NULL DEFAULT 0,
    requiere_habitaciones INTEGER NOT NULL DEFAULT 0
);

-- Tabla para tipos de cocina
CREATE TABLE IF NOT EXISTS tipos_cocina (
    tipo_cocina_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
);

-- Tabla para salones
CREATE TABLE IF NOT EXISTS salones (
    salon_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
);

-- Tabla para reservas
CREATE TABLE IF NOT EXISTS reservas (
    reserva_id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo_reserva_id INTEGER NOT NULL,
    salon_id INTEGER NOT NULL,
    tipo_cocina_id INTEGER NOT NULL,
    persona TEXT NOT NULL,
    telefono TEXT NOT NULL,
    fecha TEXT NOT NULL,
    ocupacion INTEGER NOT NULL,
    jornadas INTEGER NOT NULL,
    habitaciones INTEGER NOT NULL DEFAULT 0,
    UNIQUE(salon_id, fecha),
    FOREIGN KEY (tipo_reserva_id) REFERENCES tipos_reservas(tipo_reserva_id),
    FOREIGN KEY (tipo_cocina_id) REFERENCES tipos_cocina(tipo_cocina_id),
    FOREIGN KEY (salon_id) REFERENCES salones(salon_id)
);

-- Insertar datos de prueba en la tabla tipos_reservas
INSERT INTO tipos_reservas (nombre, requiere_jornadas, requiere_habitaciones)
VALUES
    ('Banquete', 0, 0),
    ('Jornada', 0, 0),
    ('Congreso', 1, 1);

-- Insertar datos en la tabla tipos_cocina
INSERT INTO tipos_cocina (nombre)
VALUES
    ('Bufé'),
    ('Carta'),
    ('Pedir cita con el chef'),
    ('No precisa');

-- Insertar datos en la tabla salones
INSERT INTO salones (nombre)
VALUES
    ('Salón Habana'),
    ('Otro Salón');

-- Insertar datos en la tabla reservas
INSERT INTO reservas (tipo_reserva_id, salon_id, tipo_cocina_id, persona, telefono, fecha, ocupacion, jornadas, habitaciones)
VALUES
    (1, 1, 1, 'David', '600123456', '2024-12-20', 35, 0, 0),
    (2, 2, 2, 'Juan', '123456780', '2024-11-17', 2, 0, 0),
    (1, 2, 1, 'Juan', '123456789', '2024-11-16', 1, 0, 0),
    (2, 2, 1, 'Perico', '666778899', '2024-11-15', 3, 0, 0),
    (1, 1, 2, 'David', '111223344', '2024-11-20', 35, 0, 0),
    (1, 1, 1, 'David', '222334455', '2024-11-21', 3, 0, 0),
    (3, 2, 3, 'Jacinto', '333445566', '2024-12-21', 2, 2, 0),
    (1, 1, 1, 'Jacinto', '444556677', '2024-10-21', 1, 0, 0),
    (1, 2, 1, 'Fernando', '555667788', '2024-10-21', 1, 0, 0),
    (3, 1, 2, 'Luis', '645704341', '2024-12-01', 3, 1, 1),
    (2, 1, 2, 'Azucena', '345243654', '2024-10-01', 5, 0, 0),
    (2, 1, 2, 'Azucena', '345243654', '2024-10-02', 5, 0, 0),
    (1, 1, 1, 'Carlos', '987654321', '2024-12-23', 20, 0, 0),
    (2, 2, 2, 'Luisa', '543216789', '2024-12-24', 5, 0, 0),
    (1, 1, 1, 'María', '987654312', '2024-12-25', 15, 0, 0),
    (3, 2, 3, 'Pedro', '654987123', '2024-12-26', 50, 3, 2),
    (2, 1, 2, 'Sofia', '321654987', '2024-12-27', 8, 0, 0),
    (3, 1, 4, 'Ana', '456789321', '2024-12-28', 30, 3, 1),
    (1, 2, 1, 'Tomás', '321987654', '2024-12-29', 25, 0, 0),
    (3, 1, 2, 'Alberto', '654321987', '2024-12-30', 40, 4, 2),
    (2, 1, 3, 'Beatriz', '789654321', '2024-12-31', 10, 0, 0),
    (1, 2, 1, 'Ricardo', '432165987', '2024-12-22', 12, 0, 0);