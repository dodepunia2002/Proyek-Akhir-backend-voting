# Studi Kasus Sistem Voting Online - Kelompok 2

##  Deskripsi Proyek
Proyek ini merupakan aplikasi **backend Sistem Voting Online** yang dikembangkan menggunakan **FastAPI**.  
Aplikasi menyediakan REST API untuk mengelola **User, Candidate, dan Vote** dengan database **SQLite**.

Sistem dirancang dengan arsitektur berlapis (Router – Repository – Model – Schema) sehingga mudah dikembangkan dan dipelihara.
Proyek ini dibuat sebagai Proyek Akhir Mata Kuliah Backend Development dan telah diuji melalui Swagger (OpenAPI).



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
│   └── erd_sistem_voting.png
├── voting.db
├── requirements.txt
└── README.md


## Proses Sistem

1. Sistem menyimpan dan mengelola data **User**.
2. Sistem mengelola data **Candidate (kandidat voting)**.
3. User dapat melakukan **Voting** terhadap kandidat.
4. Data voting disimpan ke dalam database dan dapat diakses melalui API.
5.	Data voting disimpan ke dalam database SQLite.



## Endpoint API

| Endpoint | Method | Deskripsi |
|---------|--------|-----------|
| `/` | GET | Root endpoint untuk mengecek status API |
| `/users/` | GET | Menampilkan daftar seluruh user |
| `/users/` | POST | Menambahkan user baru |
| `/candidates/` | GET | Menampilkan daftar kandidat |
| `/candidates/` | POST | Menambahkan kandidat baru |
| `/votes/` | POST | Proses voting oleh user |



## Cara Instalasi & Menjalankan Aplikasi

Jalankan perintah berikut secara berurutan melalui terminal:

1.	Clone repository
git clone https://github.com/dodepunia2002/Proyek-Akhir-backend-voting.git
cd Proyek-Akhir-backend-voting

2.	Membuat virtual environment
python3 -m venv venv

3.	Mengaktifkan virtual environment
source venv/bin/activate

4.	Install dependency
pip install -r requirements.txt

5.	Menjalankan server
uvicorn app.main:app --reload

#Jika server berhasil dijalankan, aplikasi dapat diakses melalui:
http://127.0.0.1:8000




 ## Dokumentasi API (Swagger)

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



## Contoh Pengujian API

Pengujian API dilakukan menggunakan **Swagger UI (OpenAPI)** yang disediakan oleh FastAPI serta dapat diuji menggunakan tools lain seperti **curl** atau **Postman**.

1. Pengujian Root Endpoint

GET /

**Deskripsi**  
Digunakan untuk memastikan bahwa API berjalan dengan baik.

**Response Berhasil (200 OK)**
```json
{
  "message": "API berjalan"
}


2.	Pengujian Menambahkan User

#Endpoint
POST /users/

#Request Body
{
  "name": "Dewa"
}

#Response Berhasil (200 OK)
{
  "id": 1,
  "name": "Dewa"
}

3. Pengujian Melihat Daftar User

#Endpoint
GET /users/

#Response Berhasil (200 OK)
[
  {
    "id": 1,
    "name": "Dewa"
  }
]

4. Pengujian Menambahkan Kandidat

#Endpoint
POST /candidates/

#Request Body
{
  "name": "Kandidat A"
}

#Response Berhasil (200 OK)
{
  "id": 1,
  "name": "Kandidat A"
}

5. Pengujian Melihat Daftar Kandidat

#Endpoint
GET /candidates/

#Response Berhasil (200 OK)
[
  {
    "id": 1,
    "name": "Kandidat A"
  }
]

6. Pengujian Proses Voting

#Endpoint
POST /votes/

#Request Body
{
  "user_id": 1,
  "candidate_id": 1
}

#Response Berhasil (200 OK)
{
  "message": "Vote berhasil disimpan"
}

7. Contoh Error (User Tidak Ditemukan)

#Endpoint
POST /votes/

#Request Body
{
  "user_id": 99,
  "candidate_id": 1
}

#Response Error (404 Not Found)
{
  "detail": "User tidak ditemukan"
}




## Hasil Pengujian

Berdasarkan pengujian API yang telah dilakukan menggunakan Swagger UI, seluruh endpoint pada Sistem Voting Online dapat berjalan dengan baik.  

Hasil pengujian menunjukkan bahwa:
- Endpoint **Root (`/`)** berhasil menampilkan status API berjalan.
- Endpoint **User (`/users/`)** berhasil menambahkan dan menampilkan data user.
- Endpoint **Candidate (`/candidates/`)** berhasil menambahkan dan menampilkan data kandidat.
- Endpoint **Vote (`/votes/`)** berhasil menyimpan data voting sesuai dengan relasi user dan kandidat.
- Sistem berhasil menolak proses voting apabila user atau kandidat tidak ditemukan di database.

Dengan demikian, sistem backend telah memenuhi kebutuhan fungsional dasar dari Sistem Voting Online.




## Kesimpulan

Berdasarkan hasil implementasi dan pengujian yang telah dilakukan, dapat disimpulkan bahwa:

1. Sistem Voting Online berhasil dibangun menggunakan FastAPI dengan arsitektur REST API.
2. Penggunaan SQLite sebagai database berjalan dengan baik untuk pengelolaan data user, kandidat, dan voting.
3. Validasi data dan penanganan error telah berjalan sesuai dengan kebutuhan sistem.
4. Dokumentasi API menggunakan Swagger UI mempermudah proses pengujian dan pengembangan sistem.

Sistem ini dapat dikembangkan lebih lanjut dengan menambahkan fitur autentikasi, otorisasi, dan rekapitulasi hasil voting.