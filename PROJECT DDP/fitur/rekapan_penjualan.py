import streamlit as st
import pandas as pd

# Fungsi untuk menampilkan rekap penjualan
def rekap_penjualan():
    st.subheader("Rekap Penjualan")

    # Contoh data
    # if 'rekapan' not in st.session_state:
    #     st.session_state['rekapan'] = [
    #         {
    #             "tanggal": "2024-12-30 11:16:01",
    #             "barang": "Beras (1L)",
    #             "jumlah": 1,
    #             "total_harga": 12000,
    #             "keuntungan": 2000,
    #             "uang_dibayar": 15000,
    #             "kembalian": 3000,
    #         }
    #     ]
    
    if st.session_state['rekapan']:
        df = pd.DataFrame(st.session_state['rekapan'])

        st.write("### Data Rekap Penjualan")

        # CSS untuk memastikan semua sisi tabel (termasuk index) memiliki border tebal
        st.markdown(
            """
            <style>
            .custom-table {
                border-collapse: collapse;
                width: 100%;
            }
            .custom-table th, .custom-table td {
                border: 2px solid black !important; /* Garis tabel lebih tebal */
                padding: 8px;
                text-align: left;
            }
            .custom-table tbody tr th {
                border: 4px solid black !important; /* Border untuk kolom index */
                padding: 8px;
                text-align: left;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        # Render tabel sebagai HTML dengan kelas CSS
        st.markdown(
            df.style.set_table_styles(
                [
                    {"selector": "thead th", "props": [("border", "2px solid black"), ("text-align", "left")]},
                    {"selector": "tbody td", "props": [("border", "2px solid black"), ("text-align", "left")]},
                    {"selector": "tbody tr th", "props": [("border", "2px solid black"), ("text-align", "left")]},
                ]
            ).to_html(index_names=False), unsafe_allow_html=True
        )

    else:
        st.warning("Belum ada data rekapan.")

rekap_penjualan()
