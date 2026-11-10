from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO
    def get_all_generi(self):
        conn = DBConnect.get_connection()
        result = []
        if conn is None:
            return result

        cursor = conn.cursor(dictionary=True)
        query = "SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL AND genere != '' ORDER BY genere"

        try:
            cursor.execute(query)
            for row in cursor:
                result.append(row['genere'])
        except Exception as e:
            print(f'Errore nella query generi:{e} ')
        finally:
            cursor.close()
            conn.close()
        return result

    def get_libri_filtrati(self, biblioteca_nome, genere):
        conn = DBConnect.get_connection()
        result = []
        if conn is None:
            return result
        cursor = conn.cursor(dictionary=True)
        query = """  
            SELECT DISTINCT l.*
            FROM libro l
            JOIN copia c ON l.id_libro = c.id_libro
            JOIN biblioteca b ON c.id_biblioteca = b.id_biblioteca 
            WHERE b.nome = COALESCE(%s, b.nome)
            AND l.genere = COALESCE(%S, l.genere)
        """
        try:
            cursor.execute(query, (biblioteca_nome, genere))
            for row in cursor:
                result.append(Libro(**row))
        except Exception as e:
            print(f'Errore nella query generi:{e} ')
        finally:
            cursor.close()
            conn.close()
        return result
