# data buku
from tabulate import tabulate
books = [
    {"ISBN":"9786237121144", "Judul":"ILMU FALSAFAT", "pengarang":"Bambang simajuntak", "jumlah":9, "terpinjam":7},
    {"ISBN":"9786231800718", "Judul":"LOGIKA FALLACY", "pengarang":"Muhammad Nurudin", "jumlah":12, "terpinjam":9},
    {"ISBN":"9786026163905", "Judul":"MADILOG", "pengarang":"Tan Malaka", "jumlah":13, "terpinjam":12},
    {"ISBN":"9786022912828", "Judul":"PSYCHOLOGY OF MONEY", "pengarang":"George Orwell", "jumlah":15, "terpinjam":6}
]

# data peminjaman
records = [
    {"ISBN":"9786022912828", "status":"Selesai", "tanggal_pinjam":"2025-03-21", "tanggal_kembali":"2025-03-28"},
    {"ISBN":"9786026163905", "status":"Belum", "tanggal_pinjam":"2025-07-22", "tanggal_kembali":"none"}
]

def tampilkan_data():
    print(tabulate(books,headers="keys", tablefmt="grid"))
        

def tambah_data():
    print("Menambahkan Data")
    ISBN = int(input("Masukan ISBN berupa angka :"))
    Judul = input("Masukan Judul Buku :")
    pengarang = (input("Masukan Nama Pengarang :"))
    jumlah = int(input("Masukan jumlah buku :"))
    terpinjam = int(input("Masukan jumlah terpinjam :"))
    book = {"ISBN":ISBN, "Judul":Judul, "pengarang":pengarang, "jumlah":jumlah, "terpinjam":terpinjam}
    books.append(book)

def edit_data():
    edit = input("Masukkan Nama Buku Yang mau Diupdate: ").upper()
    for book in books:
            if book["Judul"].upper() == edit:
                print(f"Data saat ini: {book}")
                book["ISBN"] = int(input("Masukkan ISBN baru : "))
                book["Judul"] = input("Masukkan judul baru: ")
                book["pengarang"] = input("Masukkan Nama pengarang baru: ")
                book["jumlah"] = int(input("Masukkan Jumlah buku baru : "))
                book["terpinjam"] = int(input("Masukkan data buku terpinjam baru : "))
                print("Buku berhasil diupdate!")
                tampilkan_data()
                return
    print("Data buku tidak ditemukan!")


def hapus_data():
    hapus = input("Masukkan Judul buku  Yang mau Dihapus: ").upper()
    for i in range(len(books)):
        if books[i]["Judul"].upper() == hapus:
            del books[i]
            print("Buku berhasil dihapus!")
            tampilkan_data
            return
    print("Data buku tidak ditemukan!")

def tampilkan_peminjaman():
    print("|===============> DATA PEMINJAMAN <===============|")
    print(tabulate(records,headers="keys", tablefmt="grid"))
            
def tampilkan_belum():
    print(tabulate([records for records in records if records['tanggal_kembali'] is None], headers="keys", tablefmt="grid"))

def peminjaman():
    print("======Peminjaman Buku=====")
    tampilkan_data
    ISBN = input("Masukan ISBN buku yang ingin di pinjam :")
    Nama = ("Masukan Nama Peminjam :")
    tanggal_pinjam = input("Masukan tanggal pinjam (YYYY-MM-DD) :")
    for book in books:
        if book['ISBN'] == ISBN:
            if book['jumlah'] > book['terpinjam']:
                book['jumlah'] -= 1
                book['terpinjam'] +=1
                records.append({"ISBN" :ISBN, "Nama" :Nama, "status": "Belum", "tanggal_pinjam" : tanggal_pinjam, "tanggal_kembali":""})
                print("Peminjaman Berhasil")
def pengembalian():
    print("=====Pengembalian Buku=====")
    ISBN = input("Masukkan ISBN buku yang dikembalikan: ")
    tanggal_kembali = input("Masukkan tanggal kembali (YYYY-MM-DD): ")

    for record in records:
        if record["isbn"] == ISBN and record["status"] == "Belum":
            record["status"] = "Selesai"
            record["tanggal_kembali"] = tanggal_kembali
            for book in books:
                if book["isbn"] == ISBN:
                    book["terpinjam"] -= 1
                    print("Pengembalian berhasil")
                    return
    print("Data peminjaman belum ditemukan atau sudah dikembalikan.")


while True:
    print("|===============> MENU <===============|")
    print("|[1] Tampilkan Data                    |")
    print("|[2] Tambah Data                       |")
    print("|[3] Edit Data                         |")
    print("|[4] Hapus Data                        |")
    print("|--------------------------------------|")
    print("|[5] Tampilkan Semua Peminjaman        |")
    print("|[6] Tampilkan Peminjaman Belum Kembali|")
    print("|[7] Peminjaman                        |")
    print("|[8] Pengembalian                      |")
    print("|[x] Keluar                            |")
    print("|===============>      <===============|")
    menu = input("Masukkan pilihan menu (1-8 atau x): ")
    match menu:
        case "1":
            tampilkan_data()
        case "2":
            tambah_data()
        case "3":
            edit_data()
        case "4":
            hapus_data()
        case "5":
            tampilkan_peminjaman()
        case "6":
            tampilkan_belum() 
        case "7":
            peminjaman()
        case "8":
            pengembalian()
        case "x":
            print("Telah keluar dari sistem")
            break     
        case _:
            print("Pilihan tidak valid")