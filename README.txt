# Bike Sharing Analysis Dashboard

Dashboard ini menampilkan analisis interaktif tentang penyewaan sepeda menggunakan Streamlit. Anda dapat melihat pengaruh cuaca dan perbedaan antara pengguna kasual dan terdaftar.

 Cara Cepat Menjalankan Dashboard

1. Clone repositori:
    
    git clone https://github.com/username/BikeSharingDataset.git
    cd BikeSharingDataset
    

2. Buat virtual environment (Opsional):
    
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows
    

3. Instal dependensi:
    
    pip install -r requirements.txt
    

4. Jalankan dashboard:
    
    streamlit run bike_sharing_dashboard.py
    

 Fitur Dashboard
- Analisis Cuaca: Pengaruh cuaca terhadap penyewaan sepeda.
- Pengguna Kasual vs Terdaftar: Perbandingan penyewaan di hari kerja dan hari libur.

 Struktur File
- `hour.csv` & `day.csv`: Dataset penyewaan sepeda.
- `bike_sharing_dashboard.py`: Script utama Streamlit.
- `requirements.txt`: Dependensi.

 Catatan
- Repositori harus bersifat Public agar dataset dapat diakses.
- Pastikan menggunakan Python 3.7+.
