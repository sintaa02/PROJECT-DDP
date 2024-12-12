import streamlit as st

# Using object notation
menu = st.sidebar.selectbox(
    "PILIH MENU KASIR PINTAR",
    ("modal_stok", "jumlah_penjualan", "pendapatan", "rekap_penjualan")
)

# Fungsi untuk menampilkan modal stok barang
def modal_stok():
    st.subheader("Modal Stok Barang")
    st.write("Detail stok barang yang tersedia...")
    # Tambahkan input atau visualisasi stok barang di sini

# Fungsi untuk menampilkan detail pendapatan
def pendapatan():
    st.subheader("Rincian Pendapatan")
    


# Fungsi lain berdasarkan pilihan menu
def jumlah_penjualan():
    st.write("## Menu Sembako:")
    st.write("1. Beras (1L) - Rp 12.000")
    st.write("2. Gula pasir (1kg) - Rp 15.000")
    st.write("3. Minyak Goreng (1L) - Rp 20.000")
    st.write("4. Telur (per butir) - Rp 2.000")
    st.write("5. Garam (per 250 gram) - Rp 5.000")
    st.subheader("Input Barang Pembeli")
    jumlah = st.number_input("Masukkan jumlah penjualan:", min_value=0, step=1)
    if st.button("Simpan"):
        st.session_state['jumlah'] = jumlah

def rekap_penjualan():
    st.subheader("Rekap Penjualan")
    if 'jumlah' in st.session_state:
        jumlah = st.session_state['jumlah']
        st.write(f"Jumlah penjualan saat ini: {jumlah}")
    else:
        st.write("Tidak ada data jumlah penjualan yang disimpan.")


if menu == "modal_stok":
    modal_stok()
elif menu == "jumlah_penjualan":
    jumlah_penjualan()
elif menu == "pendapatan":
    pendapatan()
elif menu == "rekap_penjualan":
    rekap_penjualan()
