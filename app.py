import streamlit as st
import pickle
import re
import string

# --- Fungsi Preprocessing ---
def clean_text(text):
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

# --- Load Model & Vectorizer ---
@st.cache_resource
def load_models():
    with open('tfidf_vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    with open('model_svm.pkl', 'rb') as f:
        model_svm = pickle.load(f)
    return vectorizer, model_svm

tfidf, model = load_models()

# --- Daftar Contoh Pesan ---
contoh_pesan = {
    "--- Pilih Contoh Pesan ---": "",
    "Tagihan Jatuh Tempo": "Peringatan! Tagihan PayLater Anda senilai Rp2.500.000 jatuh tempo hari ini. Segera bayar ke Virtual Account 8899001122 agar tidak terkena denda harian.",
    "Akun Diblokir": "Akun PayLater Anda ditangguhkan sementara karena aktivitas mencurigakan. Segera verifikasi data diri Anda di link: bit.ly/verif-paylater-aman",
    "Ancaman Debt Collector": "Denda keterlambatan Rp150.000 telah ditambahkan ke tagihan Paylater Anda. Lunasi sekarang untuk menghindari kunjungan debt collector ke rumah.",
    "Limit Naik (Phishing)": "Selamat! Limit Paylater Anda naik menjadi Rp50.000.000. Klik link ini untuk aktivasi kenaikan limit: www.paylater-limit-naik.com",
    "Diskon Denda Palsu": "Terakhir hari ini! Diskon pelunasan denda 50% jika Anda membayar tagihan tertunggak sekarang. Hubungi CS kami di WA 08123456789.",
    "Konfirmasi Pembayaran": "Pembayaran tagihan listrik bulan ini berhasil diproses. Terima kasih telah menggunakan layanan kami.",
    "Kode OTP": "Kode OTP untuk masuk ke akun Anda adalah 8821. Jangan berikan kode ini kepada siapapun, termasuk pihak yang mengaku dari bank.",
    "Info Paket Kurir": "Halo, paket pesananmu sedang dalam perjalanan bersama kurir. Mohon pastikan ada penerima di alamat tujuan.",
    "Janji Temu": "Selamat siang, apakah hari ini jadi meeting pukul 14.00? Tolong konfirmasinya ya.",
    "Ucapan Terima Kasih": "Terima kasih telah berbelanja di toko kami. Silakan hubungi kami jika ada kendala dengan produk yang diterima."
}

# --- Tampilan UI ---
st.title("🚫 Deteksi Spam Paylater")
st.markdown("Deteksi SMS Spam Paylater menggunakan TF-IDF dan Support Vector Machine")

st.info("💡 **Tips:** Gunakan menu di bawah untuk mencoba berbagai contoh pesan secara cepat.")

# Pilihan Contoh (Dropdown)
pilihan = st.selectbox("📋 Pilih Contoh Pesan:", list(contoh_pesan.keys()))

# Mengambil teks dari pilihan
isi_pesan_awal = contoh_pesan[pilihan]

# Input Teks (Bisa diedit manual)
input_sms = st.text_area(
    "📝 Pesan yang akan dianalisis:", 
    value=isi_pesan_awal,
    height=150,
    placeholder="Pilih contoh di atas atau ketik pesan Anda sendiri di sini..."
)

# Tombol Deteksi
if st.button("🔍 Analisis Pesan", type="primary"):
    if input_sms:
        # 1. Preprocessing
        cleaned_text = clean_text(input_sms)
        
        # 2. Prediksi
        text_vectorized = tfidf.transform([cleaned_text])
        prediction = model.predict(text_vectorized)[0]
        proba = model.predict_proba(text_vectorized)[0]
        
        # 3. Tampilkan Hasil
        st.divider()
        if prediction == 'spam':
            st.error(f"🚨 **HASIL: TERDETEKSI SPAM!**")
            st.write(f"Keyakinan Model: **{proba[1]*100:.1f}%**")
            st.warning("⚠️ Hati-hati! Pesan ini mengandung indikasi penipuan Paylater atau pencurian data.")
        else:
            st.success(f"✅ **HASIL: PESAN AMAN**")
            st.write(f"Keyakinan Model: **{proba[0]*100:.1f}%**")
            st.info("ℹ️ Pesan ini terlihat normal dan tidak berbahaya.")
            
    else:
        st.warning("⚠️ Silakan pilih contoh pesan atau ketik sesuatu.")

# Footer
st.markdown("---")
st.caption("Kelompok 1 UAS NLP - Spam SMS Paylater")
