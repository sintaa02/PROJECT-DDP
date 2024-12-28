import streamlit as st
import datetime as dt

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

# Fungsi untuk menambahkan jumlah penjualan
def jumlah_penjualan():
    st.subheader("Input Penjualan Barang")
    st.date_input('Input tanggal sekarang: ')

    # Menampilkan data stok barang
    st.write("### Daftar Barang")
    for key, value in st.session_state['stok'].items():
        st.write(f"{key}. {value['nama']} - Harga Jual: Rp {value['harga_jual']} - Stok: {value['stok']}")

    # Pilih barang dan jumlah terjual
    barang_id = st.selectbox("Pilih Barang:", options=list(st.session_state['stok'].keys()), format_func=lambda x: f"{x} - {st.session_state['stok'][x]['nama']}")
    jumlah = st.number_input("Masukkan jumlah yang terjual:", min_value=1, step=1)

    # Hitung total harga
    if st.button("Hitung Total Harga"):
        stok = st.session_state['stok']
        if barang_id in stok:
            if jumlah <= stok[barang_id]['stok']:
                total_harga = jumlah * stok[barang_id]['harga_jual']
                keuntungan = jumlah * (stok[barang_id]['harga_jual'] - stok[barang_id]['harga_modal'])
                st.session_state['total_harga'] = total_harga
                st.session_state['barang_id'] = barang_id
                st.session_state['jumlah'] = jumlah
                st.session_state['keuntungan'] = keuntungan
                st.success(f"Total Harga: Rp {total_harga:,} - Keuntungan: Rp {keuntungan:,}")
            else:
                st.error("Jumlah melebihi stok yang tersedia!")
        else:
            st.error("Barang tidak ditemukan, mungkin Anda salah input.")

    # Input uang yang dibayarkan pembeli
    if 'total_harga' in st.session_state and 'barang_id' in st.session_state:
        total_harga = st.session_state['total_harga']
        barang_id = st.session_state['barang_id']
        jumlah = st.session_state['jumlah']
        keuntungan = st.session_state['keuntungan']

        uang_dibayar = st.number_input("Masukkan jumlah uang yang dibayar oleh pembeli:", min_value=0, step=1000)
        if st.button("Hitung Kembalian"):
            if uang_dibayar < total_harga:
                st.error("Uang yang dibayarkan kurang!")
            else:
                kembalian = uang_dibayar - total_harga
                st.success(f"Kembalian: Rp {kembalian:,}")

                # Kurangi stok dan simpan transaksi ke rekapan
                st.session_state['stok'][barang_id]['stok'] -= jumlah
                st.session_state['rekapan'].append({
                    "tanggal": dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "barang": st.session_state['stok'][barang_id]['nama'],
                    "jumlah": jumlah,
                    "total_harga": total_harga,
                    "keuntungan": keuntungan,
                    "uang_dibayar": uang_dibayar,
                    "kembalian": kembalian
                })
                st.success(f"Penjualan {st.session_state['stok'][barang_id]['nama']} berhasil disimpan!", icon="✅")
            # # Kurangi stok
            # st.session_state['stok'][barang_id]['stok'] -= jumlah
            # st.success(f"Stok {barang['nama']} berhasil diperbarui.")
jumlah_penjualan()
