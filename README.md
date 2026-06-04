## Proyek ini tidak langsung menggunakan dataset mentah untuk proses analisis. Pada tahap **Data Wrangling** dilakukan beberapa proses pembersihan dan transformasi data secara manual, antara lain:

* Menghapus kolom yang tidak relevan (`Errors?`).
* Membersihkan kolom `Amount` dengan menghapus simbol mata uang (`$`) dan mengubah tipe data menjadi numerik.
* Mengonversi nilai transaksi dari USD ke Rupiah melalui kolom `Amount_Rupiah`.
* Membuat kolom tanggal (`date`) dari kombinasi kolom `Year`, `Month`, dan `Day`.
* Menangani missing value pada kolom `Merchant State` dengan mengisi nilai `"Unknown"`.
* Menghapus kolom-kolom yang tidak digunakan dalam proses analisis.

Dengan demikian, dataset telah melalui proses pembersihan dan transformasi sebelum digunakan pada tahap analisis.

---

## Setiap tahapan analisis dalam notebook disertai dengan penjelasan menggunakan markdown, seperti:

* Penentuan pertanyaan bisnis.
* Insight setelah proses pengumpulan data.
* Insight setelah proses pembersihan data.
* Penjelasan hasil analisis dan visualisasi.

Selain itu, dashboard Streamlit juga memberikan keterangan pada setiap visualisasi dan hasil prediksi sehingga pengguna dapat memahami informasi yang ditampilkan.

---

## Seluruh kesimpulan yang dihasilkan didukung oleh visualisasi data, antara lain:

* Grafik tren total pengeluaran bulanan.
* Grafik perbandingan pengeluaran tertinggi dan terendah.
* Grafik Top 10 kategori transaksi berdasarkan MCC.
* Diagram distribusi metode pembayaran.
* Grafik perbandingan transaksi fraud dan non-fraud.
* Visualisasi prediksi pengeluaran bulan berikutnya menggunakan Linear Regression.

Kesimpulan yang diberikan berasal dari hasil observasi terhadap visualisasi tersebut.

---

## Dataset akhir telah dipersiapkan agar siap digunakan untuk proses analisis maupun pemodelan dengan cara:

* Membersihkan nilai non-numerik pada kolom transaksi.
* Mengubah tipe data ke format yang sesuai.
* Menangani missing value.
* Membuat fitur baru yang diperlukan seperti `Amount_Rupiah` dan `date`.
* Menghapus atribut yang tidak digunakan dalam analisis.

Hasil preprocessing menghasilkan dataset yang lebih konsisten dan siap digunakan pada tahap analisis maupun pemodelan sederhana.

---

## Model prediksi menggunakan algoritma **Linear Regression** untuk memperkirakan total pengeluaran bulan berikutnya.

Pada proses pelatihan model:

* Fitur yang digunakan hanya kolom `Index` yang merepresentasikan urutan waktu.
* Target yang diprediksi adalah `Amount_Rupiah`.
* Kolom target tidak dimasukkan kembali ke dalam fitur pelatihan.

Karena fitur dan target dipisahkan dengan jelas, maka tidak terjadi **data leakage** pada proses pemodelan yang dilakukan dalam proyek ini.
