PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

-- 1. TABEL USERS (Anggota Kelompok)
CREATE TABLE IF NOT EXISTS "users" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "email" VARCHAR,
    "username" VARCHAR,
    "password" VARCHAR,
    "is_active" BOOLEAN
);

-- Password untuk semua akun adalah: '123456'
-- Hash: $2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxh96pPrEOOeE31E32GVgBnGdOHnu

INSERT INTO users VALUES(1,'agung@example.com','gungdanan2005-maker','b',1);
INSERT INTO users VALUES(2,'yoga@example.com','Yoga240030457','b',1);
INSERT INTO users VALUES(3,'zacky@example.com','ZCASTUDIO','b',1);
INSERT INTO users VALUES(4,'dodepunia@example.com','dodepunia2002','b',1);
INSERT INTO users VALUES(5,'anom@example.com','AnomWibawa','b',1);

-- 2. TABEL CANDIDATES (Calon Ketua)
CREATE TABLE IF NOT EXISTS "candidates" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" VARCHAR,
    "description" VARCHAR
);

INSERT INTO candidates VALUES(1,'Kandidat 01: Budi Santoso','Mewujudkan organisasi yang transparan, modern, dan berbasis teknologi.');
INSERT INTO candidates VALUES(2,'Kandidat 02: Siti Aminah','Meningkatkan kreativitas dan kolaborasi antar anggota melalui seni & budaya.');
INSERT INTO candidates VALUES(3,'Kandidat 03: Andi Pratama','Fokus pada pengembangan kewirausahaan (Entrepreneurship) mahasiswa.');

-- 3. TABEL VOTES (Contoh Suara Masuk)
CREATE TABLE IF NOT EXISTS "votes" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "user_id" INTEGER,
    "candidate_id" INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(candidate_id) REFERENCES candidates(id)
);

-- Simulasi: Agung (ID 1) memilih Kandidat 1
INSERT INTO votes VALUES(1,1,1);

-- Simulasi: Yoga (ID 2) memilih Kandidat 2
INSERT INTO votes VALUES(2,2,2);

COMMIT;
