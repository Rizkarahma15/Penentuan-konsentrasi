import os

# Bagian tambahan: Membuat requirements.txt kalau belum ada
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

# --- Mulai coding asli kamu ---
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Fungsi untuk menghitung persamaan regresi linier dan koefisien korelasi
def calculate_regression_equation(X, Y, var_name_x='x', var_name_y='y'):
    n = len(X)
    sum_x = np.sum(X)
    sum_y = np.sum(Y)
    sum_xy = np.sum(X * Y)
    sum_x_squared = np.sum(X**2)
    sum_y_squared = np.sum(Y**2)

    # Menghitung koefisien regresi
    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    a = (sum_y - b * sum_x) / n

    # Menghitung koefisien korelasi
    r = (n * sum_xy - sum_x * sum_y) / np.sqrt((n * sum_x_squared - sum_x**2) * (n * sum_y_squared - sum_y**2))

    equation = f'{var_name_y} = {a:.2f} + {b:.2f}{var_name_x}'
    regression_info = {'equation': equation, 'intercept': a, 'slope': b, 'r_value': r}
    return regression_info

# Halaman aplikasi Streamlit
def main():
    st.title('✨ Penentuan Konsentrasi Dari Persam
