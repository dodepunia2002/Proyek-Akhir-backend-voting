-- DATABASE DUMP SISTEM VOTING ONLINE (KELOMPOK 2)
-- Dialect: SQLite
-- Members: Agung Dananjaya, Yoga Pramana, Zacky Cahya, Dode Punia, Anom Wibawa

BEGIN TRANSACTION;

-- ==========================================
-- 1. STRUKTUR TABEL (DDL)
-- ==========================================

CREATE TABLE IF NOT EXISTS "users" (
	"id"	INTEGER NOT NULL,
	"email"	VARCHAR NOT NULL UNIQUE,
	"username"	VARCHAR NOT NULL UNIQUE,
	"password"	VARCHAR,
	"is_active"	BOOLEAN DEFAULT 1,
	"role"	VARCHAR DEFAULT 'user',
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "polls" (
	"id"	INTEGER NOT NULL,
	"title"	VARCHAR,
	"description"	VARCHAR,
	"deadline"	DATETIME,
	"is_active"	BOOLEAN DEFAULT 1,
	"creator_id"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("creator_id") REFERENCES "users"("id")
);

CREATE TABLE IF NOT EXISTS "candidates" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR,
	"description"	VARCHAR,
	"poll_id"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("poll_id") REFERENCES "polls"("id")
);

CREATE TABLE IF NOT EXISTS "votes" (
	"id"	INTEGER NOT NULL,
	"user_id"	INTEGER,
	"candidate_id"	INTEGER,
	"poll_id"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "users"("id"),
	FOREIGN KEY("candidate_id") REFERENCES "candidates"("id"),
	FOREIGN KEY("poll_id") REFERENCES "polls"("id")
);

-- ==========================================
-- 2. DATA DUMMY (DML) - ANGGOTA KELOMPOK
-- ==========================================

-- Password Hash Placeholder: '$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWrn96pzvPnEyezRI.qKGyXv5.JL66'
-- (Ini adalah hash untuk password 'rahasia'. Silakan ganti dengan hash '123456' dari hasil register manual Anda)

-- 1. Project Manager (Admin)
INSERT INTO "users" ("email", "username", "password", "is_active", "role") 
VALUES ('gungdanan@voting.com', 'gungdanan2005-maker', '$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWrn96pzvPnEyezRI.qKGyXv5.JL66', 1, 'admin');

-- 2. Database Designer (Admin)
INSERT INTO "users" ("email", "username", "password", "is_active", "role") 
VALUES ('yoga@voting.com', 'Yoga240030457', '$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWrn96pzvPnEyezRI.qKGyXv5.JL66', 1, 'admin');

-- 3. Repository Engineer (User)
INSERT INTO "users" ("email", "username", "password", "is_active", "role") 
VALUES ('zacky@voting.com', 'ZCASTUDIO', '$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWrn96pzvPnEyezRI.qKGyXv5.JL66', 1, 'user');

-- 4. Auth & Integration (User)
INSERT INTO "users" ("email", "username", "password", "is_active", "role") 
VALUES ('dode@voting.com', 'dodepunia2002', '$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWrn96pzvPnEyezRI.qKGyXv5.JL66', 1, 'user');

-- 5. QA & Documentation (User)
INSERT INTO "users" ("email", "username", "password", "is_active", "role") 
VALUES ('anom@voting.com', 'AnomWibawa', '$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWrn96pzvPnEyezRI.qKGyXv5.JL66', 1, 'user');


-- ==========================================
-- 3. DATA DUMMY - CONTOH POLLING & KANDIDAT
-- ==========================================

-- Polling: Pemilihan Ketua Kelompok
INSERT INTO "polls" ("title", "description", "deadline", "is_active", "creator_id") 
VALUES ('Pemilihan Ketua Tim', 'Voting internal untuk menentukan ketua tim project backend', '2026-12-31 23:59:59', 1, 1);

-- Kandidat (Opsi)
INSERT INTO "candidates" ("name", "description", "poll_id") 
VALUES ('Agung Dananjaya', 'Visi: Memimpin dengan tegas dan terstruktur.', 1);

INSERT INTO "candidates" ("name", "description", "poll_id") 
VALUES ('Yoga Pramana', 'Visi: Mengutamakan efisiensi database.', 1);

-- Contoh Vote (Zacky memilih Agung)
INSERT INTO "votes" ("user_id", "candidate_id", "poll_id") 
VALUES (3, 1, 1);

COMMIT;