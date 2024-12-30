import streamlit as st

# Inisialisasi session state untuk halaman dashboard
if 'dashboard' not in st.session_state:
    st.session_state['dashboard'] = True  # Atur nilai untuk halaman dashboard aktif

# Cek apakah ini adalah halaman dashboard
if st.session_state['dashboard']:
    # Menggunakan kolom untuk menempatkan gambar di tengah
    col1, col2, col3 = st.columns([1, 5, 1])  # Kolom dengan proporsi 1:2:1

    with col2:  # Gambar ditaruh di kolom tengah
        st.title("🛍️ SELAMAT DATANG DI KASIR PINTAR")
        st.image("image/4.png")
    # Teks di bawah gambar
    st.write(
        """
        Pada era digital, pemrograman memainkan peran penting dalam pengembangan aplikasi untuk kebutuhan spesifik, termasuk pengelolaan bisnis. 
        Teknologi modern dapat dimanfaatkan untuk menciptakan sistem yang efisien dan akurat, seperti aplikasi kasir pintar. 
        Aplikasi ini dirancang untuk menggantikan metode manual yang rentan terhadap kesalahan, mempercepat pelaporan, meningkatkan akurasi, 
        dan menyediakan data yang transparan untuk pengelolaan keuangan yang lebih efektif.
        """
    )

# Menambahkan gaya CSS untuk mengubah ukuran font