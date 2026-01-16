import sqlite3
# Kita gunakan library yang sama dengan aplikasi untuk membuat password
from passlib.context import CryptContext

print("⏳ Sedang mereset database...")

# 1. Setup Password Hash (Bcrypt)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# Hash password '123456' secara fresh menggunakan Python
hashed_password = pwd_context.hash("123456")

# 2. Koneksi ke Database voting.db
conn = sqlite3.connect("voting.db")
cursor = conn.cursor()

# 3. Hapus Tabel Lama (Biar bersih total)
cursor.executescript("""
    PRAGMA foreign_keys=OFF;
    DROP TABLE IF EXISTS votes;
    DROP TABLE IF EXISTS candidates;
    DROP TABLE IF EXISTS users;
    PRAGMA foreign_keys=ON;
""")

# 4. Buat Tabel Baru (Sesuai Struktur Project)
cursor.executescript("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email VARCHAR UNIQUE,
        username VARCHAR,
        password VARCHAR,
        is_active BOOLEAN
    );

    CREATE TABLE candidates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR,
        description VARCHAR
    );

    CREATE TABLE votes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE,
        candidate_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(candidate_id) REFERENCES candidates(id)
    );
""")

# 5. Masukkan Data Anggota Kelompok (5 Orang)
# Format: (email, username)
members = [
    ('agung@example.com', 'gungdanan2005-maker'),
    ('yoga@example.com', 'Yoga240030457'),
    ('zacky@example.com', 'ZCASTUDIO'),
    ('dodepunia@example.com', 'dodepunia2002'),
    ('anom@example.com', 'AnomWibawa')
]

print("👤 Menambahkan User...")
for email, username in members:
    # Semua user passwordnya sama: 123456 (yang sudah di-hash di atas)
    cursor.execute(
        "INSERT INTO users (email, username, password, is_active) VALUES (?, ?, ?, ?)", 
        (email, username, hashed_password, True)
    )

# 6. Masukkan Data Kandidat
print("🗳️ Menambahkan Kandidat...")
candidates = [
    ('Kandidat 01: Budi Santoso', 'Mewujudkan organisasi yang transparan & modern.'),
    ('Kandidat 02: Siti Aminah', 'Meningkatkan kreativitas & kolaborasi seni budaya.'),
    ('Kandidat 03: Andi Pratama', 'Fokus pengembangan kewirausahaan mahasiswa.')
]

for name, desc in candidates:
    cursor.execute("INSERT INTO candidates (name, description) VALUES (?, ?)", (name, desc))

# 7. Masukkan Contoh Vote (Agung & Yoga sudah memilih)
print("✅ Menambahkan Data Vote Dummy...")
cursor.execute("INSERT INTO votes (user_id, candidate_id) VALUES (1, 1)") # User 1 pilih Kandidat 1
cursor.execute("INSERT INTO votes (user_id, candidate_id) VALUES (2, 2)") # User 2 pilih Kandidat 2

conn.commit()
conn.close()

print("🎉 SELESAI! Database voting.db berhasil dibuat ulang.")
print("👉 Silakan login dengan password: 123456")