import streamlit as st
import base64

# Fungsi untuk menambahkan gambar latar belakang
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        # Encode gambar sebagai base64
        encoded_image = base64.b64encode(image.read()).decode()  # Gunakan base64.b64encode
    # Sisipkan CSS untuk gambar latar belakang
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_image}");
            background-size: cover;
            background-position: center;
            background-color: black;  /* Warna latar belakang */
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
        unsafe_allow_html=True  # Izinkan HTML kustom
    )

# Atur halaman
st.set_page_config(
    page_title="KASIR PINTAR",
    layout="wide",
    page_icon="🛍️"
)

# Menambahkan gambar latar belakang
add_bg_from_local("image/background.jpg")  # Pastikan jalur file benar

# Data dan fungsi lainnya
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

# Navigasi halaman (pastikan struktur sesuai aplikasi Anda)
dasboard = st.Page("./fitur/dasboard.py", title="Dasboard")
modal_stok = st.Page("./fitur/modal_stok.py")
jumlah_penjualan = st.Page("./fitur/jumlah_penjualan.py")
pendapatan = st.Page("./fitur/pendapatan.py")
rekapan_penjualan = st.Page("./fitur/rekapan_penjualan.py")

pg = st.navigation(
    {
        "HOME": [dasboard],
        "Menu Utama": [modal_stok, jumlah_penjualan, pendapatan, rekapan_penjualan],
    }
)
pg.run()
