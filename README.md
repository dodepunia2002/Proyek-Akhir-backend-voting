# SISTEM VOTING ONLINE - KELOMPOK 2

## Deskripsi Singkat
Proyek ini merupakan aplikasi **SISTEM Voting Online** yang dikembangkan menggunakan **FastAPI**.  
Aplikasi menyediakan REST API untuk mengelola **User, Candidate, dan Vote** dengan database **SQLite**.

Sistem dirancang dengan arsitektur berlapis (Router – Repository – Model – Schema) sehingga mudah dikembangkan dan dipelihara.
Proyek ini dibuat sebagai Proyek Akhir Mata Kuliah Backend Development dan telah diuji melalui Swagger UI(OpenAPI).

---

## Daftar Anggota Tim

| No | Nama | NIM | GitHub | Peran |
|----|------|-----|--------|------|
| 1 | Anak Agung Made Agung Dananjaya | 230030447 | gungdanan2005-maker | Inisialisasi proyek, setup FastAPI, konfigurasi database |
| 2 | Ida Bagus Gde Yoga Pramana | 240030457 | Yoga240030457 | Pembuatan model database dan schema |
| 3 | Zacky Cahya Afrizai | 240030268 | ZCASTUDIO | Implementasi repository (CRUD database) |
| 4 | I Dewa Gede Punia Atmaja | 220030750 | dodepunia2002 | Implementasi router dan endpoint API |
| 5 | I Made Anom Wibawa | 240030465 | AnomWibawa | Dokumentasi sistem dan penulisan README |

---

## Lingkungan Pengembangan

- **Bahasa Pemrograman**: Python 3.10+
- **Framework**: FastAPI
- **Web Server**: Uvicorn
- **ORM**: SQLAlchemy
- **Validasi Data**: Pydantic
- **Database**: SQLite
- **Dokumentasi API**: Swagger UI & ReDoc

---

## Proses Bisnis Sistem

1. Sistem menyimpan dan mengelola data **User**.
2. Sistem menyimpan dan mengelola data **Candidate (kandidat)**.
3. User dapat melakukan **voting** terhadap kandidat yang tersedia.
4. Sistem memvalidasi bahwa user dan kandidat tersedia.
5. Data voting disimpan ke dalam database.
6. Hasil voting dapat digunakan untuk proses perhitungan suara.

---

## Entity Relationship Diagram (ERD)

ERD menggambarkan relasi antara tabel **User**, **Candidate**, dan **Vote**.  
Relasi yang digunakan adalah **One-to-Many**:
- Satu User dapat melakukan banyak Vote
- Satu Candidate dapat menerima banyak Vote

![ERD SISTEM VOTING ONLINE](document/erd_sistem_voting_online_kelompok2.png)

---

## Struktur Tabel Database

### Tabel `users`
| Field | Tipe Data | Keterangan |
|------|-----------|------------|
| id | Integer (PK) | ID User |
| name | String | Nama User |

### Tabel `candidates`
| Field | Tipe Data | Keterangan |
|------|-----------|------------|
| id | Integer (PK) | ID Kandidat |
| name | String | Nama Kandidat |

### Tabel `votes`
| Field | Tipe Data | Keterangan |
|------|-----------|------------|
| id | Integer (PK) | ID Vote |
| user_id | Integer (FK) | Relasi ke User |
| candidate_id | Integer (FK) | Relasi ke Candidate |

---

## Hasil Pengembangan

### Modul User
- Menambahkan user
- Menampilkan daftar user

### Modul Candidate
- Menambahkan kandidat
- Menampilkan daftar kandidat

### Modul Vote
- User melakukan voting terhadap kandidat
- Validasi user dan kandidat sebelum voting

### Dokumentasi API
- Swagger UI (`/docs`)
- ReDoc (`/redoc`)

---

## Struktur Folder

Proyek-Akhir-backend-voting/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models/
│   │   ├── user.py
│   │   ├── candidate.py
│   │   └── vote.py
│   ├── schemas/
│   │   ├── user_schema.py
│   │   ├── candidate_schema.py
│   │   └── vote_schema.py
│   ├── repositories/
│   │   ├── user_repository.py
│   │   ├── candidate_repository.py
│   │   └── vote_repository.py
│   ├── routers/
│   │   ├── user_router.py
│   │   ├── candidate_router.py
│   │   └── vote_router.py
│   └── services/
│       └── .gitkeep
├── document/
│   ├── laporan.pdf
│   └── erd_sistem_voting.png
├── voting.db
├── requirements.txt
└── README.md

---

## Cara Instalasi dan Menjalankan Aplikasi

```bash
# Clone repository
git clone https://github.com/dodepunia2002/Proyek-Akhir-backend-voting.git
cd Proyek-Akhir-backend-voting

# Membuat virtual environment
python3 -m venv venv

# Mengaktifkan virtual environment
source venv/bin/activate

# Install dependency
pip install -r requirements.txt

# Menjalankan server aplikasi
uvicorn app.main:app --reload

Akses aplikasi melalui browser:
	•	API Root: http://127.0.0.1:8000
	•	Swagger UI: http://127.0.0.1:8000/docs
	•	ReDoc: http://127.0.0.1:8000/redoc

⸻

Contoh Pengujian API

Menambahkan User

POST /users/

{
  "name": "User Contoh"
}

Menambahkan Candidate

POST /candidates/

{
  "name": "Candidate Contoh"
}

Melakukan Voting

POST /votes/

{
  "user_id": 1,
  "candidate_id": 1
}


