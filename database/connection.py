"""
=====================================================
Inventory ERP System
Database Connection Module
=====================================================

Module ini bertanggung jawab untuk:

1. Membuat koneksi ke SQLite
2. Mengembalikan objek connection
3. Menutup koneksi database

Author : Arif Fadi Maolana
Version: 1.0
"""

import sqlite3
from pathlib import Path


# =====================================================
# Lokasi database
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = BASE_DIR / "inventory.db"


# =====================================================
# Membuat koneksi database
# =====================================================

def get_connection():
    """
    Mengembalikan koneksi SQLite.

    Returns
    -------
    sqlite3.Connection
    """

    connection = sqlite3.connect(DATABASE_PATH)

    # Agar hasil query bisa dipanggil menggunakan nama kolom
    connection.row_factory = sqlite3.Row

    return connection


# =====================================================
# Menutup koneksi
# =====================================================

def close_connection(connection):
    """
    Menutup koneksi database.
    """

    if connection:
        connection.close()