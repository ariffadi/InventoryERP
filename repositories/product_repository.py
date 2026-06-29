from database.connection import get_connection


class ProductRepository:

    def get_all(self):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                p.id,
                p.kode,
                p.nama,
                c.nama AS kategori,
                p.stok_awal,
                p.stok_minimum,
                p.harga,

                COALESCE((
                    SELECT SUM(qty)
                    FROM transactions
                    WHERE product_id = p.id
                    AND jenis='IN'
                ),0) AS masuk,

                COALESCE((
                    SELECT SUM(qty)
                    FROM transactions
                    WHERE product_id = p.id
                    AND jenis='OUT'
                ),0) AS keluar

            FROM products p
            JOIN categories c
                ON p.kategori_id=c.id

            ORDER BY p.nama
        """)

        rows = cursor.fetchall()

        connection.close()

        return rows

    def get_by_id(self, product_id):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM products
            WHERE id=?
        """, (product_id,))

        row = cursor.fetchone()

        connection.close()

        return row

    def get_by_code(self, kode):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM products
            WHERE kode=?
        """, (kode,))

        row = cursor.fetchone()

        connection.close()

        return row

    def add(
        self,
        kode,
        nama,
        kategori_id,
        stok_awal,
        stok_minimum,
        harga
    ):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO products
            (
                kode,
                nama,
                kategori_id,
                stok_awal,
                stok_minimum,
                harga
            )
            VALUES
            (?, ?, ?, ?, ?, ?)
        """, (
            kode,
            nama,
            kategori_id,
            stok_awal,
            stok_minimum,
            harga
        ))

        connection.commit()
        connection.close()

    def update(
        self,
        product_id,
        kode,
        nama,
        kategori_id,
        stok_awal,
        stok_minimum,
        harga
    ):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE products
            SET
                kode=?,
                nama=?,
                kategori_id=?,
                stok_awal=?,
                stok_minimum=?,
                harga=?
            WHERE id=?
        """, (
            kode,
            nama,
            kategori_id,
            stok_awal,
            stok_minimum,
            harga,
            product_id
        ))

        connection.commit()
        connection.close()

    def delete(self, product_id):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM products
            WHERE id=?
        """, (product_id,))

        connection.commit()
        connection.close()

    def search(self, keyword):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                p.id,
                p.kode,
                p.nama,
                c.nama AS kategori,
                p.stok_awal,
                p.stok_minimum,
                p.harga,

                COALESCE((
                    SELECT SUM(qty)
                    FROM transactions
                    WHERE product_id = p.id
                    AND jenis='IN'
                ),0) AS masuk,

                COALESCE((
                    SELECT SUM(qty)
                    FROM transactions
                    WHERE product_id = p.id
                    AND jenis='OUT'
                ),0) AS keluar

            FROM products p
            JOIN categories c
                ON c.id = p.kategori_id

            WHERE
                p.kode LIKE ?
                OR p.nama LIKE ?
                OR c.nama LIKE ?

            ORDER BY p.nama
        """, (
            f"%{keyword}%",
            f"%{keyword}%",
            f"%{keyword}%"
        ))

        rows = cursor.fetchall()

        connection.close()

        return rows