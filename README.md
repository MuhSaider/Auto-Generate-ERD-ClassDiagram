# SQL to Draw.io Diagram Generator (ERD & Class Diagram)

Sistem otomatisasi berbasis Web (Flask) untuk mengubah skema database SQL menjadi diagram **ERD (Notasi Chen)** dan **Class Diagram (UML)** dalam format `.drawio` yang dapat diedit sepenuhnya.

## Deskripsi

Proyek ini mengubah dump SQL dari phpMyAdmin menjadi file XML Draw.io yang fleksibel. Berbeda dengan generator lain yang menghasilkan gambar statis, hasil dari aplikasi ini dapat diedit sepenuhnya (drag-and-drop, ubah warna, modifikasi teks) di [app.diagrams.net](https://app.diagrams.net).

## Fitur

- **Native Draw.io Format**: Menghasilkan file `.drawio` yang dapat diedit, bukan gambar statis (`.png`/`.jpg`)
- **ERD Notasi Chen**: Visualisasi entitas, atribut, dan relasi dengan notasi Chen standard
- **Class Diagram UML**: Pemetaan tabel menjadi class dengan atribut, tipe data, dan method CRUD
- **Smart Connection**: Relasi otomatis dengan Orthogonal Edge Style yang rapi
- **Deteksi Kardinalitas**: Label kardinalitas (1:N) berdasarkan Foreign Key
- **Antarmuka Web**: Dashboard Flask untuk memudahkan input SQL

## Persyaratan

- Python 3.10 atau lebih tinggi
- pip (Python package manager)

## Teknologi

- **Python 3.10+**
- **Flask**: Framework web untuk antarmuka
- **XML DOM (minidom)**: Untuk membangun struktur XML Draw.io
- **Bootstrap 5**: Framework UI responsif

## Struktur Proyek

```
.
├── app.py                           # Server Flask utama
├── auto_erd.py                      # Generator ERD (notasi Chen)
├── auto_classdiagram_drawio.py      # Generator Class Diagram (UML)
├── auto_drawio.py                   # Utility Draw.io
├── generate_all.py                  # Script untuk generate semua
├── database.sql                     # Contoh database
├── database_example.sql             # Contoh database lain
├── class_diagram_detail.drawio      # Template class diagram
├── templates/
│   └── index.html                   # Interface web
├── static/
│   ├── auto_drawio.drawio           # Hasil generate auto_drawio
│   └── auto_classdiagram_drawio.drawio  # Hasil generate class diagram
├── __pycache__/                     # Cache Python
└── README.md                        # Dokumentasi ini
```## Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/username/sql-to-drawio.git
cd sql-to-drawio
```

### 2. Install Dependensi

```bash
pip install flask
```

### 3. Jalankan Aplikasi

```bash
python app.py
```

### 4. Akses Browser

Buka browser dan akses: `http://127.0.0.1:5000`

## Cara Penggunaan

1. **Export Database**: Export database dari phpMyAdmin dalam format SQL
2. **Salin SQL**: Salin seluruh isi file SQL
3. **Paste ke Web**: Tempelkan SQL di kotak teks website
4. **Generate**: Klik tombol "Generate"
5. **Download**: Unduh file `.drawio` dan buka di [app.diagrams.net](https://app.diagrams.net)

## Detail Teknis

### ERD (Notasi Chen)

Generator mendeteksi:
- **Entitas**: Setiap tabel dalam database
- **Atribut**: Setiap kolom dalam tabel
- **Relasi**: Dideteksi melalui perintah `ALTER TABLE ... ADD CONSTRAINT`

Visualisasi menggunakan notasi Chen standard dengan bentuk entitas (kotak), atribut (oval), dan relasi (belah ketupat).

### Class Diagram (UML)

Setiap class terdiri dari 3 kompartemen:

1. **Header**: Nama tabel
2. **Attributes**: Daftar kolom dengan tipe data (int, varchar, enum, dll)
3. **Methods**: Operasi dasar (create, read, update, delete)

## Lisensi

Proyek ini dilisensikan di bawah MIT License.

## Author

Dikembangkan oleh tim pengembang.

## Kontribusi

Kontribusi sangat diterima! Silakan buat Pull Request dengan perubahan yang Anda usulkan.