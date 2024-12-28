import streamlit as st
import base64

# # CSS to Streamlit
# st.markdown (
#     """
#     <style>
#     .stApp{
#         background-color: pink;
#         background-image: url("data:img/bg;base64,{encoded_image}");
#         background-size: cover;
#         background-position: center;
#         #background-color: black;  /* Warna latar belakang */
#         background-repeat: no-repeat;
#         color: white;  /* Mengubah warna font */
#     }
#     [data-testid="stSidebar"]{
#         backround-color: pink;
#         color: white;
#     }
#     [data-testid="stSidebar"]*{
#         font-size: 16px:
#         color: white !important;
#     }
#     </style>
#     """,
#     unsafe_allow_html= True
# )

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
            #background-color: black;  /* Warna latar belakang */
            background-repeat: no-repeat;
            ;  /* Mengubah warna font */
        }}

        [data-testid="stHeader"] {{
            color: black;
        }}

        [data-testid="stSidebar"] {{
            background-color: #252c2b;
            color: white;
        }}
    
        [data-testid="stSidebar"] * {{
            color: white !important;
            font-size: 20px;
        }}

        </style>
        """,
        unsafe_allow_html=True  # Izinkan HTML kustom
        )


st.set_page_config(
    page_title="KASIR PINTAR", layout="wide",page_icon="pop"
)
dasboard = st.Page("./fitur/dasboard.py", title="Dasboard")
modal_stok = st.Page("./fitur/modal_stok.py")
jumlah_penjualan = st.Page("./fitur/jumlah_penjualan.py")
pendapatan = st.Page("./fitur/pendapatan.py")
rekapan_penjualan = st.Page("./fitur/rekapan_penjualan.py")

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

# Menjalankan fungsi utama
initialize_session_state()


pg = st.navigation(
    {
        "HOME" : [dasboard],
        "Menu Utama" : [modal_stok, jumlah_penjualan, pendapatan, rekapan_penjualan],
    }
)
pg.run()

# Memanggil fungsi dengan jalur ke file gambar
add_bg_from_local("image/background.jpg")  # Pastikan jalur benar


