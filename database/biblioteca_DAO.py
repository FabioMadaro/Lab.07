from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO
    def get_all_biblioteche(self):
        conn = DBConnect.get_connection()
        result = []
        if conn is None:
            return result

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM biblioteca"

        try:
            cursor.execute(query)
            for row in cursor:
                result.append(Biblioteca(**row))
        except Exception as e:
            print(f"Errore nella query biblioteche: {e}")
        finally:
            cursor.close()
            conn.close()

        return result
