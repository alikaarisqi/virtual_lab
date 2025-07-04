

import streamlit as st

# --- Fungsi Konversi Suhu ---
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# --- Aplikasi Streamlit ---
st.set_page_config(page_title="Kalkulator Konverter Suhu")

st.title("🌡️ Kalkulator Konverter Suhu Interaktif")
st.write("Ubah suhu antara Celsius, Fahrenheit, dan Kelvin dengan mudah.")

# Pilihan konversi
konversi_options = {
    "Celsius ke Fahrenheit": "C_F",
    "Celsius ke Kelvin": "C_K",
    "Fahrenheit ke Celsius": "F_C",
    "Fahrenheit ke Kelvin": "F_K",
    "Kelvin ke Celsius": "K_C",
    "Kelvin ke Fahrenheit": "K_F",
}

pilihan = st.selectbox(
    "Pilih jenis konversi:",
    list(konversi_options.keys())
)

# Input suhu
nilai_suhu = st.number_input("Masukkan nilai suhu:", value=0.0)

hasil_konversi = None
unit_asal = ""
unit_tujuan = ""

# Melakukan konversi berdasarkan pilihan
if pilihan == "Celsius ke Fahrenheit":
    hasil_konversi = celsius_to_fahrenheit(nilai_suhu)
    unit_asal = "°C"
    unit_tujuan = "°F"
elif pilihan == "Celsius ke Kelvin":
    hasil_konversi = celsius_to_kelvin(nilai_suhu)
    unit_asal = "°C"
    unit_tujuan = "K"
elif pilihan == "Fahrenheit ke Celsius":
    hasil_konversi = fahrenheit_to_celsius(nilai_suhu)
    unit_asal = "°F"
    unit_tujuan = "°C"
elif pilihan == "Fahrenheit ke Kelvin":
    hasil_konversi = fahrenheit_to_kelvin(nilai_suhu)
    unit_asal = "°F"
    unit_tujuan = "K"
elif pilihan == "Kelvin ke Celsius":
    hasil_konversi = kelvin_to_celsius(nilai_suhu)
    unit_asal = "K"
    unit_tujuan = "°C"
elif pilihan == "Kelvin ke Fahrenheit":
    hasil_konversi = kelvin_to_fahrenheit(nilai_suhu)
    unit_asal = "K"
    unit_tujuan = "°F"

# Menampilkan hasil
if hasil_konversi is not None:
    st.markdown(f"---")
    st.subheader("Hasil Konversi:")
    st.success(f"{nilai_suhu:.2f}{unit_asal} setara dengan {hasil_konversi:.2f}{unit_tujuan}")
