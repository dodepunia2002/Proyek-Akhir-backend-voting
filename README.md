# Proyek Akhir Backend – Sistem Voting Online

##  Deskripsi Proyek
Proyek ini merupakan aplikasi **backend Sistem Voting Online** yang dikembangkan menggunakan **FastAPI**.  
Aplikasi menyediakan REST API untuk mengelola **User, Candidate, dan Vote** dengan database **SQLite**.

Proyek ini dibuat sebagai **Proyek Akhir Mata Kuliah Backend Development** dan seluruh implementasi telah disesuaikan dengan struktur serta kode pada repository GitHub.



## Anggota Tim & Pembagian Peran

| No | Nama & NIM | Peran | GitHub |
|----|-----------|------|--------|
| 1 | **Anak Agung Made Agung Dananjaya**<br>230030447<br>*(Ketua Kelompok)* | Inisialisasi proyek, setup FastAPI, konfigurasi database, main application | [gungdanan2005-maker](https://github.com/gungdanan2005-maker) |
| 2 | **Ida Bagus Gde Yoga Pramana**<br>240030457 | Pembuatan model database (SQLAlchemy) dan schema (Pydantic) | [Yoga240030457](https://github.com/Yoga240030457) |
| 3 | **Zacky Cahya Afrizai**<br>240030268 | Implementasi repository layer (CRUD database) | [ZCASTUDIO](https://github.com/ZCASTUDIO) |
| 4 | **I Dewa Gede Punia Atmaja**<br>220030750 | Implementasi router & endpoint API | [dodepunia2002](https://github.com/dodepunia2002) |
| 5 | **I Made Anom Wibawa**<br>240030465 | Dokumentasi sistem & penulisan README | [AnomWibawa](https://github.com/AnomWibawa) |



## Lingkungan Pengembangan

- **Bahasa Pemrograman**: Python 3.10+
- **Framework**: FastAPI
- **Web Server**: Uvicorn
- **ORM**: SQLAlchemy
- **Validasi Data**: Pydantic
- **Database**: SQLite
- **Dokumentasi API**: Swagger (OpenAPI)



##  Struktur Folder

Struktur folder sesuai dengan repository:

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
│   └── laporan.pdf
├── voting.db
├── requirements.txt
└── README.md


## Proses Bisnis Sistem

1. Sistem menyimpan dan mengelola data **User**.
2. Sistem mengelola data **Candidate (kandidat voting)**.
3. User dapat melakukan **Voting** terhadap kandidat.
4. Data voting disimpan ke dalam database dan dapat diakses melalui API.



## Endpoint API

| Endpoint | Method | Deskripsi |
|---------|--------|-----------|
| `/` | GET | Root endpoint |
| `/users/` | GET, POST | Manajemen user |
| `/candidates/` | GET, POST | Manajemen kandidat |
| `/votes/` | POST | Proses voting |



## Cara Instalasi & Menjalankan Aplikasi

Jalankan perintah berikut secara berurutan melalui terminal:

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

Jika server berhasil dijalankan, aplikasi dapat diakses melalui:

http://127.0.0.1:8000




 Dokumentasi API (Swagger)

FastAPI menyediakan dokumentasi API otomatis menggunakan Swagger.

Akses melalui browser:

http://127.0.0.1:8000/docs




 Database
	•	Jenis Database: SQLite
	•	Nama File: voting.db

Database digunakan untuk menyimpan data:
	•	User
	•	Candidate
	•	Vote

Database akan otomatis digunakan saat aplikasi dijalankan tanpa konfigurasi tambahan.



Contoh Pengujian API

 Menambahkan User

Endpoint

POST /users/

Request Body

{
  "name": "User Contoh"
}



Melihat Daftar User

Endpoint

GET /users/


