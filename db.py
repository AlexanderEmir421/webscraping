import sqlite3

class DatabaseManager:
    def __init__(self):
        self.connection = sqlite3.connect("scraping_data.db")
        self.cursor = self.connection.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        query = """
        CREATE TABLE IF NOT EXISTS datos (
            id_unico INTEGER PRIMARY KEY AUTOINCREMENT,
            Expediente TEXT NOT NULL UNIQUE,
            Jurisdiccion TEXT NOT NULL,
            Dependencia TEXT NOT NULL,
            Sit_Actual TEXT NOT NULL,
            Caratula TEXT NOT NULL,
            Demandante TEXT,
            Demandado TEXT,
            Fecha TEXT
        );
        """
        self.cursor.execute(query)
        self.connection.commit()

    def expediente_existe(self, expediente):
        query = "SELECT 1 FROM datos WHERE Expediente = ?"
        self.cursor.execute(query, (expediente,))
        return self.cursor.fetchone() is not None

    def guardar_dato(self, datos):
        
        if self.expediente_existe(datos[0]):
            return False

        query = """
        INSERT INTO datos (Expediente, Jurisdiccion, Dependencia, Sit_Actual, Caratula, Demandante, Demandado, Fecha) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.cursor.execute(query, (datos[0], datos[1], datos[2], datos[3], datos[4], None, None, None))
        self.connection.commit()
        return True

    def cerrar(self):
        self.connection.close()
