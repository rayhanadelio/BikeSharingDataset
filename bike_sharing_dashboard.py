import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Mengatur tampilan tema
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Fungsi untuk membaca data dari GitHub
@st.cache
def load_data():
    data_hour = pd.read_csv('https://raw.githubusercontent.com/rayhanadelio/BikeSharingDataset/refs/heads/main/hour.csv')
    data_day = pd.read_csv('https://raw.githubusercontent.com/rayhanadelio/BikeSharingDataset/refs/heads/main/day.csv')
    return data_hour, data_day

# Memuat dataset
data_hour, data_day = load_data()

# Judul Dashboard
st.title("Bike Sharing Dashboard")

# Menu untuk memilih analisis
menu = st.sidebar.selectbox("Pilih Analisis", ["Analisis Cuaca", "Analisis Pengguna"])

# Analisis Cuaca
if menu == "Analisis Cuaca":
    st.header("Pengaruh Cuaca terhadap Penyewaan Sepeda")
    
    # Mengelompokkan data berdasarkan cuaca
    weather_rentals = data_hour.groupby(['weathersit', 'workingday'])['cnt'].sum().unstack()
    
    # Membuat grafik batang
    plt.figure(figsize=(10, 6))
    weather_rentals.plot(kind='bar', color=['#1f77b4', '#ff7f0e'])
    plt.title('Jumlah Penyewaan Sepeda berdasarkan Cuaca', fontsize=16)
    plt.xlabel('Kondisi Cuaca', fontsize=14)
    plt.ylabel('Jumlah Penyewaan Sepeda', fontsize=14)
    plt.xticks(rotation=0)
    plt.legend(title='Jenis Hari', labels=['Hari Kerja', 'Hari Libur'])
    plt.grid(axis='y')
    st.pyplot(plt)

# Analisis Pengguna
if menu == "Analisis Pengguna":
    st.header("Perbandingan Penyewaan Sepeda: Pengguna Kasual vs Terdaftar")
    
    # Mengelompokkan data pengguna
    user_rentals = data_day.groupby(['workingday'])[['casual', 'registered']].sum()
    
    # Membuat grafik batang
    plt.figure(figsize=(10, 6))
    user_rentals.plot(kind='bar', color=['#2ca02c', '#d62728'])
    plt.title('Penyewaan Sepeda: Kasual vs Terdaftar', fontsize=16)
    plt.xlabel('Jenis Hari', fontsize=14)
    plt.ylabel('Jumlah Penyewaan Sepeda', fontsize=14)
    plt.xticks([0, 1], ['Hari Kerja', 'Hari Libur'], rotation=0)
    plt.legend(title='Tipe Pengguna', labels=['Kasual', 'Terdaftar'])
    plt.grid(axis='y')
    st.pyplot(plt)

# Menambahkan informasi tentang dashboard
st.sidebar.header("Informasi")
st.sidebar.text("Dashboard ini menampilkan analisis tentang\n"
                 "penyewaan sepeda berdasarkan cuaca dan jenis pengguna.")

