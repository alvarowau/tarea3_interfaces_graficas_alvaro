MYSQL_QUERIES = {
    'get_all_cocinas': "SELECT * FROM tipos_cocina",
    'get_cocina_by_id': "SELECT * FROM tipos_cocina WHERE tipo_cocina_id = %s",
    'existe_tabla': "SHOW TABLES LIKE 'tipos_cocina'",
    'describe_tabla': "DESCRIBE tipos_cocina"
}

# Consultas para SQLite
SQLITE_QUERIES = {
    'get_all_cocinas': "SELECT * FROM tipos_cocina",
    'get_cocina_by_id': "SELECT * FROM tipos_cocina WHERE tipo_cocina_id = ?",
    'existe_tabla': "SELECT name FROM sqlite_master WHERE type='table' AND name='tipos_cocina'",
    'describe_tabla': "PRAGMA table_info(tipos_cocina)"
}
