import streamlit as st

# # CSS to Streamlit
# st.markdown (
#     """
#     <style>
#     .stApp{
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
# CSS untuk mengatur warna font

st.markdown(
    """
    <style>
    .subheader {
        color: blue;
        font-size: 40px;
    }
    .description {
        color: green;
        font-size: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Data awal untuk stok barang
if 'stok' not in st.session_state:
    st.session_state['stok'] = {
        1: {'nama': 'Beras (1L)', 'harga': 10000, 'stok': 50},
        2: {'nama': 'Gula pasir (1kg)', 'harga': 13000, 'stok': 40},
        3: {'nama': 'Minyak Goreng (1L)', 'harga': 18000, 'stok': 30},
        4: {'nama': 'Telur (1 kg)', 'harga': 25000, 'stok': 70},
        5: {'nama': 'Garam (per 250 gram)', 'harga': 4000, 'stok': 60}
    }

#if 'rekapan' not in st.session_state:
    #st.session_state['rekapan'] = []

# Fungsi untuk menampilkan modal stok barang
def modal_stok():
    st.subheader("Modal Stok Barang")

    # Menampilkan data stok barang
    st.write("### Daftar Stok Barang")
    for key, value in st.session_state['stok'].items():
        #st.write(f"{key}. {value['nama']} - Harga Modal: Rp {value['harga_modal']} - Harga Jual: Rp {value['harga_jual']} - Stok: {value['stok']}")
        st.write(f"{key}. {value['nama']} - Harga Modal: Rp {value['harga_modal']} - Stok: {value['stok']}")

    # Input untuk menambah barang baru atau memperbarui stok
    st.write("### Tambahkan atau Perbarui Barang")
    with st.form("form_tambah_perbarui_barang"):
        nama_baru = st.text_input("Nama Barang Baru (Kosongkan jika hanya memperbarui stok):")
        barang_no = st.number_input("Pilih Barang no (opsional untuk memperbarui):", min_value=1, max_value=len(st.session_state['stok']), step=1)
        harga_modal_baru = st.number_input("Harga Modal Barang Baru (opsional):", min_value=0, step=100)
        harga_jual_baru = st.number_input("Harga Jual Barang Baru (opsional):", min_value=0, step=100)
        stok_baru = st.number_input("Jumlah Stok (Tambahan atau Stok Awal):", min_value=0, step=1)
        submitted = st.form_submit_button("Simpan Perubahan")
        if submitted:
            if nama_baru:
                # Tambahkan barang baru
                if harga_modal_baru > 0 and harga_jual_baru > 0 and stok_baru > 0:
                    key_baru = max(st.session_state['stok'].keys()) + 1
                    st.session_state['stok'][key_baru] = {'nama': nama_baru, 'harga_modal': harga_modal_baru, 'harga_jual': harga_jual_baru, 'stok': stok_baru}
                    st.success(f"Barang baru '{nama_baru}' berhasil ditambahkan!")
                else:
                    st.error("Mohon isi harga modal, harga jual, dan stok dengan benar untuk barang baru.")
            else:
                # Perbarui stok barang yang ada
                if barang_no in st.session_state['stok']:
                    st.session_state['stok'][barang_no]['stok'] += stok_baru
                    if harga_modal_baru > 0:
                        st.session_state['stok'][barang_no]['harga_modal'] = harga_modal_baru
                    if harga_jual_baru > 0:
                        st.session_state['stok'][barang_no]['harga_jual'] = harga_jual_baru
                    st.success(f"Stok {st.session_state['stok'][barang_no]['nama']} berhasil diperbarui.")
                else:
                    st.error("Barang tidak valid.")


modal_stok()