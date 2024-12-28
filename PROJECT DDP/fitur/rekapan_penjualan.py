import streamlit as st
import pandas as pd 
import datetime as dt
from datetime import datetime
# Fungsi untuk menampilkan rekap penjualan
def rekap_penjualan():
    st.subheader("Rekap Penjualan")

    if st.session_state['rekapan']:
        df = pd.DataFrame(st.session_state['rekapan'])
        st.write("### Data Rekap Penjualan")
        st.table(df)
    else:
        st.warning("Belum ada data rekapan.")
rekap_penjualan()