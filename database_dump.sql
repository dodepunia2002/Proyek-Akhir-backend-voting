PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

-- 1. TABEL USERS (Anggota Kelompok) --
CREATE TABLE IF NOT EXISTS "users" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "email" VARCHAR,
    "username" VARCHAR,
    "password" VARCHAR,
    "is_active" BOOLEAN
);

-- Password untuk SEMUA akun di bawah adalah: '123456'
-- (Hash Bcrypt: $2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxh96pPrEOOeE31E32GVgBnGdOHnu)

-- Anggota 1: Agung Dananjaya
INSERT INTO users VALUES(1,'agung@example.com','gungdanan2005-maker','b',1);

-- Anggota 2: Yoga Pramana
INSERT INTO users VALUES(2,'yoga@example.com','Yoga240030457','b',1);

-- Anggota 3: Zacky Cahya
INSERT INTO users VALUES(3,'zacky@example.com','ZCASTUDIO','b',1);

-- Anggota 4: Dode Punia (Anda)
INSERT INTO users VALUES(4,'dodepunia@example.com','dodepunia2002','b',1);

-- Anggota 5: Anom Wibawa
INSERT INTO users VALUES(5,'anom@example.com','AnomWibawa','b',1);


-- 2. TABEL CANDIDATES --
CREATE TABLE IF NOT EXISTS "candidates" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" VARCHAR,
    "description" VARCHAR
);
INSERT INTO candidates VALUES(1,'Kandidat 01: Budi Santoso','Mewujudkan organisasi yang transparan, akuntabel, dan berbasis teknologi.');
INSERT INTO candidates VALUES(2,'Kandidat 02: Siti Aminah','Meningkatkan kreativitas mahasiswa melalui program kerja kolaboratif.');
INSERT INTO candidates VALUES(3,'Kandidat 03: Andi Pratama','Fokus pada pengembangan soft skill dan jaringan eksternal kampus.');


-- 3. TABEL VOTES (Sampel Suara) --
CREATE TABLE IF NOT EXISTS "votes" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "user_id" INTEGER,
    "candidate_id" INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(candidate_id) REFERENCES candidates(id)
);

-- Agung (ID 1) memilih Kandidat 1
INSERT INTO votes VALUES(1,1,1);

-- Yoga (ID 2) memilih Kandidat 2
INSERT INTO votes VALUES(2,2,2);

COMMIT;
