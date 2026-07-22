import streamlit as st
import base64
import os

# 1. Atur halaman (Wajib paling atas sebelum elemen UI lainnya)
st.set_page_config(
    page_title="KASIR PINTAR",
    layout="wide",
    page_icon="🛍️"
)

# 2. Fungsi menambahkan background (dilengkapi penanganan error biar gak crash)
def add_bg_from_local(image_file):
    if os.path.exists(image_file):
        with open(image_file, "rb") as image:
            encoded_image = base64.b64encode(image.read()).decode()
        
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpg;base64,{encoded_image}");
                background-size: cover;
                background-position: center;
                background-color: black;
                background-repeat: no-repeat;
            }}

            [data-testid="stHeader"] {{
                background-color: #E8CAA8;
            }}

            [data-testid="stSidebar"] * {{
                background-color: #E8CAA8;
                color: black !important;
                font-size: 20px;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        # Jika gambar background tidak ditemukan, app TETAP JALAN (nggak bakal crash)
        st.warning(f"Sistem: File background tidak ditemukan di '{image_file}', melewati latar belakang kustom.")

# Mencari jalur folder tempat app.py berada
dir_path = os.path.dirname(os.path.realpath(__file__))
# Menggunakan os.path.join agar kompatibel penuh antar sistem (Windows / Linux Streamlit Cloud)
image_path = os.path.join(dir_path, "image", "background.jpg")

# Panggil fungsi background
add_bg_from_local(image_path)


# 3. Data dan Inisialisasi Session State
def initialize_session_state():
    if 'stok' not in st.session_state:
        st.session_state['stok'] = {
            1: {'nama': 'Beras (1L)', 'harga_modal': 10000, 'harga_jual': 12000, 'stok': 50},
            2: {'nama': 'Gula pasir (1kg)', 'harga_modal': 13000, 'harga_jual': 15000, 'stok': 40},
            3: {'nama': 'Minyak Goreng (1L)', 'harga_modal': 18000, 'harga_jual': 20000, 'stok': 30},
            4: {'nama': 'Telur (1 kg)', 'harga_modal': 25000, 'harga_jual': 28000, 'stok': 70},
            5: {'nama': 'Garam (per 250 gram)', 'harga_modal': 4000, 'harga_jual': 5000, 'stok': 60}
        }

    if 'rekapan' not in st.session_state:
        st.session_state['rekapan'] = []

initialize_session_state()

# 4. Navigasi Halaman
dasboard = st.Page("./fitur/dasboard.py", title="Dasboard")
modal_stok = st.Page("./fitur/modal_stok.py", title="Modal Stok")
jumlah_penjualan = st.Page("./fitur/jumlah_penjualan.py", title="Jumlah Penjualan")
pendapatan = st.Page("./fitur/pendapatan.py", title="Pendapatan")
rekapan_penjualan = st.Page("./fitur/rekapan_penjualan.py", title="Rekapan Penjualan")

pg = st.navigation(
    {
        "HOME": [dasboard],
        "Menu Utama": [modal_stok, jumlah_penjualan, pendapatan, rekapan_penjualan],
    }
)
pg.run()
