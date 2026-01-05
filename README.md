# 🚫 Deteksi Spam SMS Paylater & Tagihan Palsu

**Spam Detection System** adalah aplikasi cerdas berbasis Web yang dirancang untuk mendeteksi pesan SMS penipuan, khususnya yang bermodus **tagihan Paylater palsu**, ancaman blokir akun, dan link phishing.

Dibangun menggunakan **Python** dan **Streamlit**, aplikasi ini memanfaatkan kecerdasan buatan (Machine Learning) dengan algoritma **Support Vector Machine (SVM)** dan ekstraksi fitur **TF-IDF** untuk membedakan pesan aman (*Ham*) dan pesan penipuan (*Spam*) dengan tingkat akurasi tinggi.

---

##  Fitur Utama

* **Real-time Detection:** Masukkan teks pesan, dan sistem akan langsung menganalisis apakah itu spam atau aman.
* **Confidence Score:** Menampilkan tingkat keyakinan (persentase) dari prediksi model.
* **Quick Test Examples:** Tersedia tombol contoh pesan otomatis (Tagihan Palsu, Ancaman Blokir, Pesan Kurir, dll) untuk pengujian cepat.
* **Hybrid Dataset:** Dilatih menggunakan gabungan dataset SMS Spam umum dan dataset spesifik Paylater berbahasa Indonesia.
* **Simple UI:** Antarmuka yang bersih, responsif, dan mudah digunakan oleh siapa saja.

---

## 🛠️ Teknologi yang Digunakan

Aplikasi ini dibangun dengan *Tech Stack* berikut:

* **Bahasa:** [Python 3.10+](https://www.python.org/)
* **Framework UI:** [Streamlit](https://streamlit.io/)
* **Machine Learning:** [Scikit-learn](https://scikit-learn.org/) (SVM Algorithm)
* **NLP Tools:** TF-IDF Vectorizer, RegEx (Text Preprocessing)
* **Data Processing:** Pandas, NumPy

---

## 📦 Cara Instalasi & Menjalankan (Lokal)

Ingin menjalankan aplikasi ini di komputer sendiri? Ikuti langkah berikut:

1.  **Clone Repository ini**
    ```bash
    git clone [https://github.com/username-kamu/deteksi-spam-paylater.git](https://github.com/username-kamu/deteksi-spam-paylater.git)
    cd deteksi-spam-paylater
    ```

2.  **Install Dependencies**
    Pastikan Python sudah terinstall, lalu jalankan:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Jalankan Aplikasi**
    ```bash
    streamlit run app.py
    ```

4.  **Buka di Browser**
    Aplikasi akan berjalan otomatis di `http://localhost:8501`.

---

## 🧠 Cara Kerja Model

Model ini bekerja melalui beberapa tahapan *Natural Language Processing* (NLP):

1.  **Preprocessing:** Membersihkan teks dari tanda baca, angka yang tidak relevan, dan mengubah huruf menjadi kecil (*lowercase*).
2.  **Feature Extraction (TF-IDF):** Mengubah kata-kata menjadi vektor angka berdasarkan bobot kepentingannya. Kata seperti "blokir", "denda", "segera" memiliki bobot tinggi pada kelas Spam.
3.  **Classification (SVM):** Algoritma *Support Vector Machine* memisahkan data menggunakan *hyperplane* untuk menentukan apakah pesan masuk kategori **Spam** atau **Ham** (Aman).

---

## 📁 Struktur Folder

```text
deteksi-spam-paylater/
├── app.py                  # File utama aplikasi Streamlit
├── model_svm.pkl           # Model SVM yang sudah dilatih
├── tfidf_vectorizer.pkl    # Vectorizer TF-IDF yang sudah dilatih
├── dataset_spam_paylater.csv # (Opsional) Sampel data latih
├── requirements.txt        # Daftar library yang dibutuhkan
└── README.md               # Dokumentasi proyek
