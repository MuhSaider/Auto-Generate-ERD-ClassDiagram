# 🚀 SQL to Draw.io Diagram Generator (ERD & Class Diagram)

Sistem otomatisasi berbasis Web (Flask) untuk mengubah skema database SQL (khususnya dump phpMyAdmin) menjadi diagram **ERD (Notasi Chen)** dan **Class Diagram (UML)** dalam format asli `.drawio`.

Berbeda dengan generator diagram lainnya yang menghasilkan gambar statis, proyek ini menghasilkan file XML Draw.io yang **dapat diedit sepenuhnya** (drag-and-drop, ubah warna, dan modifikasi teks) di [app.diagrams.net](https://app.diagrams.net).

## 🌟 Fitur Unggulan

- **Native Draw.io Format**: Hasil berupa file `.drawio` yang fleksibel, bukan gambar mati (`.png`/`.jpg`).
- **ERD Notasi Chen**: Visualisasi otomatis entitas (kotak), atribut (oval), dan relasi (belah ketupat).
- **Class Diagram UML**: Pemetaan tabel menjadi Class lengkap dengan atribut, detail tipe data (termasuk ENUM dan INT), serta simulasi method CRUD.
- **Smart Connection**: Garis relasi otomatis menempel pada objek dan menggunakan *Orthogonal Edge Style* (garis siku) agar tetap rapi saat objek digeser.
- **Deteksi Kardinalitas**: Otomatis menambahkan label kardinalitas `1` ke `N` berdasarkan *Foreign Key*.
- **Antarmuka Web**: Dilengkapi dengan dashboard sederhana berbasis Flask untuk memudahkan proses *copy-paste* SQL.

## 🛠️ Teknologi yang Digunakan

- **Python 3.10+**
- **Flask**: Sebagai penggerak antarmuka web.
- **XML DOM (minidom)**: Untuk membangun struktur XML Draw.io dari nol.
- **Bootstrap 5**: Untuk tampilan UI website yang bersih dan responsif.

## 📁 Struktur Proyek

```text
.
├── app.py                      # Server Web Flask & Integrasi
├── auto_erd.py                 # Engine Generator ERD (Chen Notation)
├── auto_classdiagram_drawio.py # Engine Generator Class Diagram (UML)
├── templates/
│   └── index.html              # Interface untuk Input SQL
├── static/                     # Folder penyimpanan hasil generate
└── README.md                   # Dokumentasi
🚀 Cara Instalasi
Clone Repositori:

Bash

git clone [https://github.com/username/sql-to-drawio.git](https://github.com/username/sql-to-drawio.git)
cd sql-to-drawio
Install Flask:

Bash

pip install flask
Jalankan Aplikasi:

Bash

python app.py
Akses di Browser: Buka http://127.0.0.1:5000.

📖 Cara Penggunaan
Export database kamu dari phpMyAdmin (pilih format SQL).

Salin seluruh isi file SQL tersebut.

Tempelkan (Paste) pada kotak teks di website.

Klik tombol Generate.

Unduh file .drawio dan buka melalui app.diagrams.net.

📊 Detail Teknis Generator
ERD (Notasi Chen)
Generator mendeteksi tabel sebagai Entitas dan kolom sebagai Atribut. Relasi dideteksi melalui perintah ALTER TABLE ... ADD CONSTRAINT yang menghubungkan antar tabel.

Class Diagram (UML)
Generator membagi setiap class menjadi 3 kompartemen:

Header: Nama tabel.

Attributes: Daftar kolom beserta tipe datanya (seperti int(11) atau enum).

Methods: Simulasi operasi dasar create(), update(), dan delete().

<img width="1286" height="587" alt="image" src="https://github.com/user-attachments/assets/db8ef770-fd6b-4e33-845c-d2e17e545f64" />
