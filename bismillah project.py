stok_barang = []

def tambah_barang():
    print('-'*40)
    print(" TAMBAH BARANG ".center(40, '='))
    print('-'*40)
    print("Kode Barang | Nama Barang    | Harga Modal | Stok Barang | Satuan")
    print("---------------------------------------------------------------")
    print("BS          | Beras          | 100.000     | 20          | Karung ")

    while True:
        # Input data barang
        kode_brg = input("Masukkan kode barang: ").strip().upper()
        nama_brg = input("Masukkan nama barang: ").strip()
        harga_modal = float(input("Masukkan harga modal: ").strip())
        stok = int(input("Masukkan stok barang: ").strip())
        satuan = input("Masukkan satuan barang: ").strip()
        barang = {
            "Kode Barang": kode_brg,
            "Nama Barang": nama_brg,
            "Harga Modal": harga_modal,
            "Stok Barang": stok,
            "Satuan": satuan
        }
        stok_barang.append(barang)
        # Tampilkan daftar barang
        print("\nLIST BARANG")
        print("Kode Barang | Nama Barang    | Harga Modal | Stok Barang | Satuan")
        print("---------------------------------------------------------------")
        
        # Iterasi melalui setiap barang di stok_barang
        for barang in stok_barang:
            print(barang["Kode Barang"], "|", barang["Nama Barang"], "|", barang["Harga Modal"], "|", barang["Stok Barang"], "|", barang["Satuan"])
# Jalankan fungsi tambah_barang
tambah_barang()
