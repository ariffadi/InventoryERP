from database.connection import get_connection


def migrate():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kode TEXT NOT NULL UNIQUE,
            nama TEXT NOT NULL,
            kategori_id INTEGER NOT NULL,
            stok_awal INTEGER NOT NULL,
            stok_minimum INTEGER NOT NULL,
            harga REAL NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (kategori_id) REFERENCES categories(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tanggal TEXT NOT NULL,
            product_id INTEGER NOT NULL,
            jenis TEXT NOT NULL CHECK(jenis IN ('IN','OUT')),
            qty INTEGER NOT NULL,
            harga REAL NOT NULL,
            total REAL NOT NULL,
            keterangan TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    """)

    categories = [
        ("Elektronik",),
        ("ATK",),
        ("Furniture",),
        ("Makanan",),
        ("Minuman",)
    ]

    cursor.executemany(
        "INSERT OR IGNORE INTO categories (nama) VALUES (?)",
        categories
    )

    connection.commit()
    connection.close()

    print("✅ Database berhasil dimigrasi.")