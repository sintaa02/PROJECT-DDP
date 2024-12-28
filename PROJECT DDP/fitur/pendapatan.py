import streamlit as st
# Fungsi untuk menghitung pendapatan bersih
def pendapatan():
    st.subheader("Pendapatan dan Keuntungan")

    if st.session_state['rekapan']:
        total_pendapatan = sum(item['total_harga'] for item in st.session_state['rekapan'])
        total_keuntungan = sum(item['keuntungan'] for item in st.session_state['rekapan'])
        st.write(f"### Total Pendapatan: Rp {total_pendapatan:,}")
        st.write(f"### Total Keuntungan: Rp {total_keuntungan:,}")
    else:
        st.warning("Belum ada data penjualan untuk dihitung.")
pendapatan()