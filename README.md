# SISTEM VOTING ONLINE - KELOMPOK 2

## Deskripsi Singkat
Proyek ini merupakan aplikasi **Sistem Voting Online** berbasis web yang terdiri dari Backend (FastAPI) dan Frontend (HTML/CSS/JS Native). Aplikasi ini dirancang untuk memfasilitasi proses pemilihan umum secara digital yang aman, transparan, dan efisien. Sistem menerapkan prinsip **"Satu Pengguna Satu Suara"** dan menggunakan keamanan berbasis token (JWT).

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

Alat dan teknologi yang digunakan dalam pengembangan proyek ini:

* **Sistem Operasi:** macOS / Windows / Linux
* **Bahasa Pemrograman:** Python 3.11+
* **Framework Backend:** FastAPI
* **Database:** SQLite (Relational Database)
* **ORM:** SQLAlchemy
* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Authentication:** JWT (JSON Web Token) dengan algoritma HS256 & Bcrypt Hashing
* **Tools:** Visual Studio Code, SQLite3, Swagger UI, Git & GitHub

---

## Proses Bisnis

Alur kerja aplikasi berjalan sebagai berikut:

1.  **Registrasi Pengguna:** Pengunjung mendaftar akun baru dengan memasukkan username, email, dan password. Password disimpan dalam database dalam bentuk *hash* (terenkripsi).
2.  **Autentikasi (Login):** Pengguna login menggunakan email dan password. Jika valid, sistem memberikan **Access Token (JWT)**.
3.  **Melihat Kandidat:** Pengguna yang sudah login dapat melihat daftar kandidat beserta visi-misinya di dashboard.
4.  **Proses Voting:**
    * Pengguna memilih salah satu kandidat.
    * Sistem memvalidasi Token untuk memastikan identitas pengguna.
    * Sistem mengecek di database apakah pengguna tersebut sudah pernah melakukan voting sebelumnya.
    * Jika belum, suara disimpan dan status pengguna ditandai sudah memilih. Jika sudah, permintaan ditolak.
5.  **Melihat Hasil:** Semua pengguna (baik yang sudah memilih atau belum) dapat melihat hasil perolehan suara secara *real-time* dalam bentuk tabel rekapitulasi.

---

## ERD (Entity Relationship Diagram)

Berikut adalah desain model data yang digunakan. Sistem menggunakan relasi **One-to-Many** antara User/Candidate dengan Vote.

![ERD Sistem Voting Online](document/erd_sistem_voting_online_kelompok2.png)



---

## Struktur/Informasi Detil Tabel Database

Database `voting.db` terdiri dari 3 tabel utama:

### 1. Tabel \`users\`
Menyimpan data pengguna aplikasi.
* **id** (Integer, Primary Key): ID unik pengguna.
* **email** (String, Unique): Alamat email pengguna (digunakan untuk login).
* **username** (String, Unique): Nama pengguna.
* **password** (String): Password yang sudah di-hash (bukan plain text).
* **is_active** (Boolean): Status aktif akun (Default: True).

### 2. Tabel \`candidates\`
Menyimpan data kandidat yang akan dipilih.
* **id** (Integer, Primary Key): ID unik kandidat.
* **name** (String): Nama lengkap kandidat.
* **description** (String): Visi misi atau deskripsi singkat kandidat.

### 3. Tabel \`votes\`
Menyimpan data transaksi suara (Junction Table).
* **id** (Integer, Primary Key): ID unik suara.
* **user_id** (Integer, ForeignKey): Merujuk ke tabel \`users\`. Kolom ini memiliki *Unique Constraint* terhadap user (satu user hanya boleh ada satu kali di tabel ini).
* **candidate_id** (Integer, ForeignKey): Merujuk ke tabel \`candidates\`.

---

## Hasil Pengembangan

Implementasi fitur dibagi menjadi modul-modul berikut:

1.  **Modul Autentikasi (Auth Router):**
    * Register User baru.
    * Login & Generate JWT Token.
2.  **Modul Kandidat (Candidate Router):**
    * Menampilkan seluruh daftar kandidat (GET).
    * Menambah kandidat baru (POST).
3.  **Modul Voting (Vote Router):**
    * Melakukan voting dengan validasi token & *double-voting check*.
    * Menghitung rekapitulasi hasil suara (Aggregation).
4.  **Frontend Interface:**
    * Halaman Login & Register yang responsif.
    * Dashboard User untuk melihat kandidat.
    * Tampilan hasil voting real-time.

---

## Struktur Folder

```text
Proyek-Akhir-backend-voting/
├── app/                        # Source code Backend
│   ├── core/                   # Konfigurasi Security & CORS
│   ├── database/               # Setup koneksi Database
│   ├── models/                 # Definisi Tabel (SQLAlchemy)
│   ├── repositories/           # Logika akses data (CRUD)
│   ├── routers/                # Endpoint API (Controller)
│   ├── schemas/                # Validasi data (Pydantic)
│   ├── services/               # Logika bisnis utama
│   └── main.py                 # Entry point aplikasi
├── frontend/                   # Source code Frontend
│   ├── index.html              # Halaman Utama
│   ├── style.css               # File Styling
│   └── script.js               # File Logika JavaScript
├── voting.db                   # File Database SQLite
├── database_dump.sql           # Backup data SQL
├── requirements.txt            # Daftar library Python
└── README.md                   # File dokumentasi ini

```

---

## Cara Instalasi dan Menjalankan Aplikasi

Ikuti langkah-langkah berikut untuk menjalankan proyek di komputer lokal:

### 1. Persiapan Backend

1. Buka terminal dan masuk ke folder proyek.
2. Buat Virtual Environment (opsional tapi disarankan):
```bash
python3 -m venv venv
source venv/bin/activate  # (Mac/Linux)
# atau venv\Scripts\activate (Windows)


```
3. Install library yang dibutuhkan:
```bash
pip install -r requirements.txt
```
4. Jalankan Server Backend:
```bash
uvicorn app.main:app --reload
```
*Server akan aktif di https://www.google.com/search?q=http://127.0.0.1:8000*

### 2. Menjalankan Frontend

1. Pastikan server backend sudah berjalan.
2. Buka folder **`frontend`**.
3. Klik dua kali file **`index.html`** untuk membukanya di browser.
4. Aplikasi siap digunakan (Login, Daftar, Voting).

---



```

