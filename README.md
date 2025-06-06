# Sidra Brute Force Tool

Sidra Brute Force Tool adalah alat sederhana berbasis Python untuk melakukan serangan brute force pada form login berbasis HTTP, mendukung metode GET dan POST. Tool ini dirancang untuk latihan keamanan dan edukasi, memungkinkan pengguna menguji kekuatan username dan password pada aplikasi web yang rentan.

---

## Fitur Utama

- Mendukung metode HTTP GET dan POST  
- Menggunakan wordlist untuk username dan password  
- Mendeteksi keberhasilan login berdasarkan indikator teks pada respons halaman  
- Mendukung parameter custom untuk username dan password  
- Mudah digunakan melalui command line interface (CLI)  
- Cocok untuk pengujian keamanan aplikasi web, seperti DVWA

---

## Instalasi

1. Pastikan Python 3 sudah terpasang di sistem Anda.  
2. Install dependencies yang dibutuhkan (hanya `requests`):

```bash
pip install requests


## Penggunaan

sidra --url "http://localhost/DVWA/vulnerabilities/brute/" \
      --method GET \
      --userparam username \
      --passparam password \
      --userfile users.txt \
      --passfile passwords.txt \
      --success "Welcome to the password protected area" \
      --header "Cookie:"


## Note

Modifikasi File Wordlist sesuai kebutuhan

