# OCR Receipt Analytics Dashboard

## Deskripsi

Project ini bertujuan untuk mengekstraksi informasi transaksi dari gambar receipt menggunakan Optical Character Recognition (OCR). Data hasil OCR kemudian melalui proses Data Wrangling, Cleaning, dan Transformasi sebelum divisualisasikan menggunakan Streamlit Dashboard.

## Dataset

Dataset yang digunakan adalah **SROIE 2019 Receipt Dataset**, yang berisi kumpulan gambar receipt untuk proses ekstraksi informasi transaksi.

## Tools & Libraries

- Python
- EasyOCR
- Pandas
- Regex
- Matplotlib
- Streamlit

## Workflow Project

1. Data Gathering (SROIE Dataset)
2. OCR Text Extraction menggunakan EasyOCR
3. Data Assessing dan Cleaning
4. Feature Extraction (Tanggal & Nominal Transaksi)
5. Konversi Mata Uang Dollar ke Rupiah
6. Penyimpanan Dataset Bersih (.csv)
7. Visualisasi Dashboard dengan Streamlit

## Dataset Output

Kolom yang dihasilkan:

| Kolom | Deskripsi |
|--------|------------|
| image_name | Nama file receipt |
| date | Tanggal transaksi |
| total_amount_dollar | Nominal transaksi (USD) |
| total_amount_rupiah | Nominal transaksi (IDR) |
| raw_text | Hasil OCR setelah preprocessing |

## Menjalankan Dashboard

```bash
pip install streamlit pandas matplotlib
streamlit run app.py
```

## Hasil Dashboard

Dashboard menampilkan:

- Jumlah Receipt
- Total Transaksi
- Rata-rata Transaksi
- Transaksi Tertinggi
- Top 10 Transaksi Terbesar
- Statistik Dataset
- Informasi Kualitas Data

## Author

Anita Widyastini  
Capstone Project – Data Science Path