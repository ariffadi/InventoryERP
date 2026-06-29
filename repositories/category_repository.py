from database.connection import get_connection


class CategoryRepository:

    def get_all(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, nama
            FROM categories
            ORDER BY nama
        """)

        rows = cursor.fetchall()

        connection.close()

        return rows

    def get_by_id(self, category_id):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM categories
            WHERE id = ?
        """, (category_id,))

        row = cursor.fetchone()

        connection.close()

        return row

    def get_by_name(self, nama):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM categories
            WHERE nama = ?
        """, (nama,))

        row = cursor.fetchone()

        connection.close()

        return row