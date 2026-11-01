
# Pertemuan 13 - Debugging dan Testing

Nama: Meisya Khairunisha Priatna  
NIM: ...  
Kelas: ...

## Kasus

Program memproses data nilai mahasiswa untuk menghitung
rata-rata, menentukan status kelulusan, dan mencari nilai
tertinggi.

Program awal memiliki tiga bug logika yang diperbaiki
melalui debugging dan testing.

## Test Case

| ID | Input | Expected | Actual Awal | Status |
|---|---|---|---|---|
| T1 | [80,60,90,70] | 75.0 | 60.0 | FAIL |
| T2 | [100,80] | 90.0 | 36.0 | FAIL |
| T3 | 60 | Lulus | Tidak lulus | FAIL |
| T4 | 59 | Tidak lulus | Tidak lulus | PASS |
| T5 | [80,60,90,70] | 90 | 0 | FAIL |

## Bug Report

### B01 - Bug Rata-rata
Gejala: Hasil rata-rata tidak sesuai jumlah data.

Akar penyebab: Pembagi ditetapkan secara tetap, yaitu 5.

Perbaikan: Menggunakan len(nilai) sebagai pembagi.

### B02 - Bug Status Kelulusan
Gejala: Nilai 60 dianggap tidak lulus.

Akar penyebab: Operator pembanding menggunakan >.

Perbaikan: Mengubah operator menjadi >=.

### B03 - Bug Nilai Tertinggi
Gejala: Nilai tertinggi menghasilkan 0.

Akar penyebab: Kondisi perbandingan menggunakan <.

Perbaikan: Mengubah kondisi menjadi x > tertinggi
dan memulai nilai tertinggi dari elemen pertama.

## Retest

Seluruh lima test case dijalankan kembali.
Hasil pengujian menunjukkan semua test case PASS.

## Cara Menjalankan

python praktik/praktik_4_debugging.py

## Refleksi

Teknik debugging yang paling membantu adalah tracing
dan testing menggunakan test case.

Tracing membantu mengetahui perubahan nilai variabel,
sedangkan test case membantu membuktikan kesalahan
program melalui perbandingan expected result dan
actual result.

Setelah perbaikan, program perlu diuji kembali untuk
memastikan bug sudah teratasi dan tidak menimbulkan
masalah baru.
