import os
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --- Bagian membuat requirements.txt ---
if not os.path.exists('requirements.txt'):
    requirements = [
        "streamlit",
        "numpy",
        "pandas",
        "matplotlib"
    ]
    with open('requirements.txt', 'w') as f:
        for package in requirements:
            f.write(package + '\n')
    print("✅ File requirements.txt berhasil dibuat!")

# --- Fungsi Regresi Linier ---
def calculate_regression_equation(X, Y, var_name_x='x', var_name_y='y'):
    n = len(X)
    sum_x = np.sum(X)
    sum_y = np.sum(Y)
    sum_xy = np.sum(X * Y)
    sum_x_squared = np.sum(X**2)
    sum_y_squared = np.sum(Y**2)

    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    a = (sum_y - b * sum_x) / n

    r = (n * sum_xy - sum_x * sum_y) / np.sqrt((n * sum_x_squared - sum_x**2) * (n * sum_y_squared - sum_y**2))

    equation = f'{var_name_y} = {a:.2f} + {b:.2f}{var_name_x}'
    return {'equation': equation, 'intercept': a, 'slope': b, 'r_value': r}

# --- Aplikasi Streamlit ---
def main():
    st.set_page_config(page_title="Regresi Linear Konsentrasi", layout="centered")

    # CSS custom untuk gradasi dan animasi
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #FFB6C1, #B0E0E6);
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }
        h1 {
            text-align: center;
            color: #8B4513;
            animation: floating 3s ease-in-out infinite;
        }
        @keyframes floating {
            0% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0); }
        }
        </style>
    """, unsafe_allow_html=True)

    st.title('✨ Penentuan Konsentrasi dari Persamaan Regresi ✨')
    st.markdown("Aplikasi ini menghitung konsentrasi dari data absorbansi menggunakan persamaan regresi linier.")

    # Gambar ilustrasi (ganti link jika perlu)
    st.image("https://i.imgur.com/dC1lzOj.png", caption="Ilustrasi Analisis Laboratorium", use_column_width=True)

    # Identitas kelompok
    st.header("👥 Kelompok 11 (E2-PMIP)")
    st.markdown("""
    - Kayla Nurrahma Siswoyo (2420606)  
    - Nahda Rensa Subari (2420632)  
    - Rizka Rahmawati Shavendira (2420656)  
    - Ummu Nabiilah (2420676)  
    - Dinda Aryantika (2320520)
    """)

    st.divider()

    # Input data
    st.subheader("📊 Masukkan Data Deret Standar (X = Konsentrasi, Y = Absorbansi)")
    default_data = pd.DataFrame({'X': [1, 2, 3, 4], 'Y': [0.1, 0.2, 0.3, 0.4]})
    data_df = st.data_editor(default_data, num_rows="dynamic", use_container_width=True)

    var_name_x = st.text_input("Nama variabel X:", "Konsentrasi")
    var_name_y = st.text_input("Nama variabel Y:", "Absorbansi")

    if not data_df.empty and 'X' in data_df.columns and 'Y' in data_df.columns:
        try:
            X = data_df['X'].astype(float).to_numpy()
            Y = data_df['Y'].astype(float).to_numpy()

            regression_info = calculate_regression_equation(X, Y, var_name_x, var_name_y)

            # Tampilkan persamaan regresi
            st.markdown("## Hasil Regresi:")
            st.success(f"📌 Persamaan: **{regression_info['equation']}**")
            st.info(f"Nilai slope (b): {regression_info['slope']:.4f}")
            st.info(f"Nilai intercept (a): {regression_info['intercept']:.4f}")
            st.info(f"Koefisien korelasi (r): {regression_info['r_value']:.4f}")

            # Grafik regresi
            st.subheader("📈 Grafik Regresi Linear")
            fig, ax = plt.subplots()
            ax.scatter(X, Y, color='blue', label='Data')
            ax.plot(X, regression_info['intercept'] + regression_info['slope'] * X, color='red', label='Regresi')
            ax.set_xlabel(var_name_x)
            ax.set_ylabel(var_name_y)
            ax.set_title('Grafik Regresi Linear')
            ax.legend()
            plt.tight_layout()
            st.pyplot(fig)

            # Hitung konsentrasi dari absorbansi input
            st.subheader("🔍 Hitung Konsentrasi Berdasarkan Absorbansi")
            y_input = st.number_input(f"Masukkan nilai {var_name_y} (absorbansi):", value=0.0, step=0.01)

            b = regression_info['slope']
            a = regression_info['intercept']

            if b != 0:
                x_result = (y_input - a) / b
                st.success(f"Nilai {var_name_x} (konsentrasi) adalah: **{x_result:.4f}**")
            else:
                st.warning("Slope (b) = 0, tidak bisa menghitung konsentrasi.")

        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
    else:
        st.warning("Harap isi data X dan Y dengan benar.")

# --- Jalankan aplikasi ---
if __name__ == '__main__':
    main()
