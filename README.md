# SISTEM VOTING ONLINE - KELOMPOK 2

## Deskripsi Singkat
Proyek ini merupakan aplikasi **Sistem Voting Online** yang dikembangkan sebagai Proyek Akhir Mata Kuliah Backend Development. Aplikasi ini berbasis web (Fullstack) yang terdiri dari Backend API menggunakan **FastAPI** dan Frontend menggunakan **HTML/JS Native**.

Tujuan utama sistem ini adalah memfasilitasi proses pemungutan suara digital yang aman, transparan, dan akurat. Sistem menerapkan validasi ketat di mana setiap pengguna hanya memiliki hak satu suara (*One User One Vote*) dan seluruh data transaksi disimpan dalam database relasional.

---

## Daftar Anggota Tim

| No | Nama | NIM | Username GitHub | Peran/Tugas |
|----|------|-----|-----------------|-------------|
| 1 | Anak Agung Made Agung Dananjaya | 230030447 | [gungdanan2005-maker](https://github.com/gungdanan2005-maker) | Inisialisasi proyek, setup FastAPI, konfigurasi database |
| 2 | Ida Bagus Gde Yoga Pramana | 240030457 | [Yoga240030457](https://github.com/Yoga240030457) | Pembuatan model database dan schema |
| 3 | Zacky Cahya Afrizai | 240030268 | [ZCASTUDIO](https://github.com/ZCASTUDIO) | Implementasi repository (CRUD database) |
| 4 | I Dewa Gede Punia Atmaja | 220030750 | [dodepunia2002](https://github.com/dodepunia2002) | Implementasi router, endpoint API, & Frontend |
| 5 | I Made Anom Wibawa | 240030465 | [AnomWibawa](https://github.com/AnomWibawa) | Dokumentasi sistem dan penulisan README |

---

## Lingkungan Pengembangan

Alat dan teknologi yang digunakan dalam pengembangan aplikasi ini meliputi:

* **Sistem Operasi:** macOS / Windows
* **Bahasa Pemrograman:** Python 3.11+, JavaScript (ES6)
* **Framework Backend:** FastAPI
* **Web Server:** Uvicorn
* **Database:** SQLite
* **ORM:** SQLAlchemy
* **Autentikasi:** Python-Jose (JWT), Passlib (Bcrypt)
* **Frontend:** HTML5, CSS3, Fetch API
* **IDE:** Visual Studio Code
* **Version Control:** Git & GitHub

---

## Proses Bisnis

1.  **Pendaftaran & Login:** Pengguna mendaftar dan login untuk mendapatkan token akses (Session).
2.  **Manajemen Kandidat:** Admin dapat menambah, mengedit, atau menghapus kandidat.
3.  **Voting:** Sistem memvalidasi token dan memastikan pengguna belum pernah memilih sebelumnya (*One User One Vote*).
4.  **Perhitungan Suara:** Sistem menampilkan total suara kandidat secara *real-time*.

---

## ERD (Entity Relationship Diagram)

Model data dirancang menggunakan relasi **One-to-Many**.
*(Gambar ERD berikut tersimpan dalam file `erd.png` di folder proyek)*

![!\[ERD Sistem Voting\](erd.png)](document/erd_sistem_voting_online_kelompok2.png)

---

## Tampilan Aplikasi

### 1. Swagger UI (Dokumentasi API)
Tampilan interaktif untuk menguji endpoint backend secara langsung.
![!\[Swagger UI\](swagger.png)](document/swaggerui.png)

### 2. Frontend (Antarmuka Pengguna)
Tampilan web sederhana untuk user melakukan voting dan melihat hasil.
![!\[Frontend UI\](frontend.png)](document/frontend.png)

---

## Struktur Tabel Database

### 1. Tabel `users`
* **id** (PK), **email** (Unique), **username**, **password** (Hash), **is_active**.

### 2. Tabel `candidates`
* **id** (PK), **name**, **description**.

### 3. Tabel `votes`
* **id** (PK), **user_id** (FK, Unique Constraint), **candidate_id** (FK).

---

## Hasil Pengembangan

Fitur-fitur utama yang telah berhasil diimplementasikan:
1.  **Auth:** Register & Login (JWT).
2.  **Candidates:** Full CRUD (Create, Read, Update, Delete).
3.  **Votes:** Voting & Result Aggregation.
4.  **Frontend:** Dashboard Interaktif.

---

## Struktur Folder

```text
Proyek-Akhir-backend-voting/
│
├── .gitignore                  # File konfigurasi Git (mengabaikan venv & pycache)
├── README.md                   # Dokumentasi Lengkap Proyek
├── requirements.txt            # Daftar library Python (FastAPI, SQLAlchemy, dll)
├── voting.db                   # File Database SQLite (Berisi data User, Candidate, Vote)
├── database_dump.sql           # Backup Data SQL (Untuk restore data)
│
├── erd.png                     # Gambar ERD (Untuk ditampilkan di README)
├── swagger.png                 # Screenshot Swagger UI (Untuk README)
├── frontend.png                # Screenshot Frontend (Untuk README)
│
├── frontend/                   #  FOLDER FRONTEND (Tampilan Web)
│   ├── index.html              # Halaman Utama (HTML)
│   ├── style.css               # Desain Tampilan (CSS)
│   └── script.js               # Logika & Koneksi ke API (JavaScript)
│
└── app/                        #  FOLDER BACKEND (Logika Utama)
    ├── __init__.py             # Penanda Package Python
    ├── main.py                 # Entry Point (File utama untuk menjalankan server)
    │
    ├── core/                   #  Konfigurasi & Keamanan
    │   ├── __init__.py
    │   ├── config.py           # Setting Env/Config
    │   ├── security.py         # Fungsi Hash Password & JWT
    │   └── deps.py             # Dependency Injection (misal: get_current_user)
    │
    ├── database/               #  Koneksi Database
    │   ├── __init__.py
    │   └── database.py         # Setup SessionLocal & Base Engine
    │
    ├── models/                 # Definisi Tabel Database (SQLAlchemy)
    │   ├── __init__.py
    │   ├── user.py             # Tabel Users
    │   ├── candidate.py        # Tabel Candidates
    │   └── vote.py             # Tabel Votes
    │
    ├── schemas/                # Validasi Data (Pydantic)
    │   ├── __init__.py
    │   ├── user.py             # Schema Input/Output User
    │   ├── candidate.py        # Schema Input/Output Candidate
    │   ├── vote.py             # Schema Input/Output Vote
    │   └── token.py            # Schema Token JWT
    │
    ├── repositories/           #  Logika CRUD Database
    │   ├── __init__.py
    │   ├── user_repository.py
    │   ├── candidate_repository.py
    │   └── vote_repository.py
    │
    └── routers/                # Endpoint API (URL)
        ├── __init__.py
        ├── auth.py             # URL Login & Register
        ├── candidate.py        # URL CRUD Kandidat
        └── vote.py             # URL Voting & Hasil


---


##  Cara Instalasi dan Menjalankan

### 1. Menjalankan Backend
Buka terminal di folder proyek, lalu jalankan:
\`\`\`bash
# 1. Install library
pip install -r requirements.txt

# 2. Jalankan Server
uvicorn app.main:app --reload
\`\`\`
*Server akan berjalan di: http://127.0.0.1:8000*

### 2. Menjalankan Frontend
* Buka folder **\`frontend/\`**.
* Klik dua kali file **\`index.html\`** (atau *drag & drop* ke browser).

---

##  Akun Demo (Data Dummy)

Gunakan akun berikut untuk mencoba aplikasi (semua password sama).

 **Password:** \`123456\`

| Pemilik Akun | Email Login |
|--------------|-------------|
| Agung D. | \`agung@example.com\` |
| Yoga P. | \`yoga@example.com\` |
| Zacky C. | \`zacky@example.com\` |
| Dode Punia | \`dodepunia@example.com\` |
| Anom W. | \`anom@example.com\` |

---