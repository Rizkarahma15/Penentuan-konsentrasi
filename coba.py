import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

def main():
    st.title('📊 Aplikasi Regresi Linear Deret Standar')
    st.write('Masukkan data X dan Y untuk menghitung persamaan regresi.')

    df = st.data_editor(pd.DataFrame({'X': [0.0]*4, 'Y': [0.0]*4}), num_rows="dynamic")

    var_name_x = st.text_input("Nama variabel X:", "x")
    var_name_y = st.text_input("Nama variabel Y:", "y")

    if not df.empty and 'X' in df.columns and 'Y' in df.columns:
        try:
            X = df['X'].astype(float).to_numpy()
            Y = df['Y'].astype(float).to_numpy()

            reg = calculate_regression_equation(X, Y, var_name_x, var_name_y)

            st.subheader("📈 Hasil Regresi")
            st.markdown(f"**Persamaan:** `{reg['equation']}`")
            st.write(f"Intercept (a): `{reg['intercept']:.2f}`")
            st.write(f"Slope (b): `{reg['slope']:.2f}`")
            st.write(f"Koefisien Korelasi (r): `{reg['r_value']:.4f}`")

            # Grafik
            fig, ax = plt.subplots()
            ax.scatter(X, Y, color='blue', label='Data Asli')
            ax.plot(X, reg['intercept'] + reg['slope'] * X, color='red', label='Regresi')
            ax.set_xlabel(var_name_x)
            ax.set_ylabel(var_name_y)
            ax.legend()
            st.pyplot(fig)

            # Perkiraan X dari Y
            st.subheader("🔍 Hitung X dari nilai Y")
            y_input = st.number_input(f'Masukkan nilai {var_name_y}:', value=0.0)
            if reg['slope'] != 0:
                x_calc = (y_input - reg['intercept']) / reg['slope']
                st.success(f"Nilai {var_name_x} untuk {var_name_y} = {y_input} adalah: **{x_calc:.2f}**")
            else:
                st.error("Slope = 0, tidak bisa menghitung X.")
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
    else:
        st.warning("⚠️ Harap masukkan data X dan Y yang valid.")

if __name__ == '__main__':
    main()
