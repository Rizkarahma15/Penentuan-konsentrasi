# ... bagian atas kode tetap sama ...

def main():
    st.title('✨ Penentuan Konsentrasi dari Persamaan Regresi Deret Standar ✨')
    st.write('Penentuan konsentrasi dari persamaan regresi deret standar yang dapat memudahkan analisis tanpa perlu menghitung secara manual. ENJOY FOR ACCESS 🧪👩‍🔬')

    # Gradasi CSS
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
        .floating-image {
            width: 60%;
            display: block;
            margin: auto;
            animation: float 4s ease-in-out infinite;
            border-radius: 20px;
            box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.2);
        }
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-15px); }
            100% { transform: translateY(0px); }
        }
        </style>
    """, unsafe_allow_html=True)

    # Gambar dan Tim
    img_url = "https://i.imgur.com/ZCCw6Ry.jpg"
    st.markdown(f'<img src="{img_url}" class="floating-image">', unsafe_allow_html=True)

    st.header("INTRODUCTION OUR TEAM")
    st.subheader("👥 Kelompok 11 (E2-PMIP)")
    st.write("""
    1. Kayla Nurrahma Siswoyo (2420606)  
    2. Nahda Rensa Subari (2420632)  
    3. Rizka Rahmawati Shavendira (2420656)  
    4. Ummu Nabiilah (2420676)  
    5. Dinda Aryantika (2320520)
    """)

    # Kalkulator Regresi
    st.header("📈 Kalkulator Regresi Linear")
    default_data = pd.DataFrame({'X': [0.0, 0.0, 0.0, 0.0], 'Y': [0.0, 0.0, 0.0, 0.0]})
    data_df = st.data_editor(default_data, num_rows="dynamic", use_container_width=True)

    var_name_x = st.text_input('Nama variabel X:', 'x')
    var_name_y = st.text_input('Nama variabel Y:', 'y')

    if not data_df.empty and 'X' in data_df.columns and 'Y' in data_df.columns:
        try:
            X = data_df['X'].astype(float).to_numpy()
            Y = data_df['Y'].astype(float).to_numpy()

            if len(X) < 2:
                st.warning("⚠️ Minimal diperlukan 2 titik data untuk regresi.")
            elif np.all(X == X[0]):
                st.warning("""
📝 **Petunjuk Penggunaan:**  
Silakan isi data X dan Y terlebih dahulu pada tabel di atas. Setelah data dimasukkan, aplikasi akan secara otomatis menampilkan:  
✅ Grafik regresi linear  
✅ Persamaan regresi  
✅ Koefisien korelasi  

Setelah itu, kamu bisa memasukkan nilai Y pada kolom yang tersedia untuk menghitung nilai X (konsentrasi) dengan cepat dan akurat.
""")
            else:
                reg = calculate_regression_equation(X, Y, var_name_x, var_name_y)

                st.markdown("## Hasil Regresi:")
                st.markdown(f"### 📌 {reg['equation']}")
                st.write(f"Slope (b): {reg['slope']:.2f}")
                st.write(f"Intercept (a): {reg['intercept']:.2f}")
                st.write(f"Koefisien Korelasi (r): {reg['r_value']:.4f}")

                # Grafik
                fig, ax = plt.subplots()
                ax.scatter(X, Y, color='blue', label='Data')
                ax.plot(X, reg['intercept'] + reg['slope'] * X, color='red', label='Regresi')
                ax.set_xlabel(var_name_x)
                ax.set_ylabel(var_name_y)
                ax.set_title('Grafik Regresi Linear')
                ax.legend()
                st.pyplot(fig)

                # Kalkulasi berdasarkan Y
                st.header("📊 Hitung Nilai X Berdasarkan Y")

                y_input = st.number_input(f'Masukkan nilai {var_name_y}:', value=0.0)

                # Tombol Hitung tepat di bawah input y_input
                tombol_hitung = st.button("🔍 Hitung")

                if tombol_hitung:
                    b = reg['slope']
                    a = reg['intercept']
                    if b != 0:
                        x_calc = (y_input - a) / b
                        st.success(f"Nilai {var_name_x} untuk {var_name_y} = {y_input} adalah: {x_calc:.2f}")
                    else:
                        st.error("Slope (b) = 0, tidak bisa menghitung X.")
        except Exception as e:
            st.error(f"❌ Terjadi kesalahan: {e}")
    else:
        st.warning("⚠️ Harap masukkan data X dan Y yang valid.")

if __name__ == '__main__':
    main()
