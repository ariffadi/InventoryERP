from database.connection import get_connection


class TransactionRepository:

    def add(
        self,
        tanggal,
        product_id,
        jenis,
        qty,
        harga,
        total,
        keterangan=""
    ):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO transactions
            (
                tanggal,
                product_id,
                jenis,
                qty,
                harga,
                total,
                keterangan
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            tanggal,
            product_id,
            jenis,
            qty,
            harga,
            total,
            keterangan
        ))

        connection.commit()
        connection.close()

    def get_all(self):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                t.id,
                t.tanggal,
                t.product_id,
                p.kode,
                p.nama,
                t.jenis,
                t.qty,
                t.harga,
                t.total,
                t.keterangan
            FROM transactions t
            JOIN products p
                ON p.id = t.product_id
            ORDER BY t.tanggal DESC
        """)

        rows = cursor.fetchall()

        connection.close()

        return rows

    def search(self, keyword):

        connection = get_connection()
        cursor = connection.cursor()

        keyword = f"%{keyword}%"

        cursor.execute("""
            SELECT
                t.id,
                t.tanggal,
                t.product_id,
                p.kode,
                p.nama,
                t.jenis,
                t.qty,
                t.harga,
                t.total,
                t.keterangan
            FROM transactions t
            JOIN products p
                ON p.id = t.product_id
            WHERE
                p.kode LIKE ?
                OR p.nama LIKE ?
                OR t.jenis LIKE ?
                OR t.keterangan LIKE ?
            ORDER BY t.tanggal DESC
        """, (
            keyword,
            keyword,
            keyword,
            keyword
        ))

        rows = cursor.fetchall()

        connection.close()

        return rows

    def get_by_type(self, jenis):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                t.id,
                t.tanggal,
                t.product_id,
                p.kode,
                p.nama,
                t.jenis,
                t.qty,
                t.harga,
                t.total,
                t.keterangan
            FROM transactions t
            JOIN products p
                ON p.id = t.product_id
            WHERE t.jenis = ?
            ORDER BY t.tanggal DESC
        """, (jenis,))

        rows = cursor.fetchall()

        connection.close()

        return rows

    def get_by_date(self, tanggal):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                t.id,
                t.tanggal,
                t.product_id,
                p.kode,
                p.nama,
                t.jenis,
                t.qty,
                t.harga,
                t.total,
                t.keterangan
            FROM transactions t
            JOIN products p
                ON p.id = t.product_id
            WHERE DATE(t.tanggal) = DATE(?)
            ORDER BY t.tanggal DESC
        """, (tanggal,))

        rows = cursor.fetchall()

        connection.close()

        return rows

    def get_daily_transactions(self):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                DATE(tanggal) AS tanggal,
                COUNT(*) AS total
            FROM transactions
            GROUP BY DATE(tanggal)
            ORDER BY DATE(tanggal)
        """)

        rows = cursor.fetchall()

        connection.close()

        return rows

    def has_transaction(self, product_id):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT COUNT(*) AS total
            FROM transactions
            WHERE product_id = ?
        """, (product_id,))

        result = cursor.fetchone()

        connection.close()

        return result["total"] > 0

    def get_by_id(self, transaction_id):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM transactions
            WHERE id = ?
        """, (transaction_id,))

        row = cursor.fetchone()

        connection.close()

        return row

    def delete(self, transaction_id):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM transactions
            WHERE id = ?
        """, (transaction_id,))

        connection.commit()
        connection.close()

    def update(
        self,
        transaction_id,
        tanggal,
        product_id,
        jenis,
        qty,
        harga,
        total,
        keterangan=""
    ):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE transactions
            SET
                tanggal=?,
                product_id=?,
                jenis=?,
                qty=?,
                harga=?,
                total=?,
                keterangan=?
            WHERE id=?
        """, (
            tanggal,
            product_id,
            jenis,
            qty,
            harga,
            total,
            keterangan,
            transaction_id
        ))

        connection.commit()
        connection.close()