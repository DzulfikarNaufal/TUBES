#importspace
import getpass
from utils.cli_fx import clear_screen, loading
from utils.data_manager import formatteddata
#from data_manager import simpan_mahasiswa, baca_mahasiswa
#from utils.validator import validasi_input_lengkap

#kode ansi kabur 0-dim, 1-bold, 2-reset, 3-italic, 4-Red, 5-Cyan, 6-Magenta, 7-Yellow
sft = ["\033[90m", "\033[1m", "\033[0m", "\033[3m", "\033[91m", "\033[96m", "\033[95m", "\033[93m"]

while True:
    clear_screen()
    choice = input(f"{sft[1]}\n ======] Sistem Inventaris Lab Kampus {sft[3]}(v. 0.1){sft[2]}{sft[1]} [======{sft[2]}\n\n{sft[1]}   1. Tampilkan Data\n   0. Keluar\n\n   Pilih program yang ingin dijalankan: {sft[2]}{sft[3]}")
    print()

    if choice == "0":
        loading("Program dihentikan")
        clear_screen()
        break
        
    elif choice == "1":
        clear_screen()
        formatteddata()

    else:
        clear_screen()
        print(f"\n{sft[2]}{sft[1]}{sft[4]}   Pilihan invalid!{sft[2]}\n")
        time.sleep(0.8)



 
"""
    elif choice == "1":
        clear_screen()
        nama = input(f"\n{sft[2]}{sft[1]}   Masukan Nama: {sft[2]}")
        nim = input(f"   {sft[1]}Masukan NIM: {sft[2]}")
        ipk = input(f"   {sft[1]}Masukan IPK: {sft[2]}")

        valid, hasil = validasi_input_lengkap(nim, nama, ipk)

        if valid:
            simpan_mahasiswa(hasil["nama"], hasil["nim"], hasil["ipk"])
            print(f"\n   {sft[1]}Data berhasil ditambahkan!{sft[2]}")
        else:
            print()
            for field, pesan in hasil["errors"].items():
                print(f"   {sft[4]}{field.upper()}: {pesan}{sft[2]}")
        input(f"\n   {sft[1]}Kembali? {sft[2]}")

    elif choice == "2":
        formatteddata()
        input(f"\n   {sft[2]}{sft[1]}Kembali? {sft[2]}")

    elif choice == "3":
        formatteddata()
        baris = int(input(f"   {sft[2]}{sft[1]}Masukan urut data yang akan dihapus:{sft[2]} "))
        clear_screen()
        formatteddata()
        print(f"   {sft[0]}hint: admin123{sft[2]}")
        passw = getpass.getpass(f"   {sft[2]}{sft[1]}Masukan sandi untuk menghapus data:{sft[2]} ")
        if passw == "admin123":
            clear_screen()
            for i in range(3):
                clear_screen()
                print(f"\n   {sft[2]}{sft[1]}[/] Menghapus data\n")
                time.sleep(0.1)
                clear_screen()
                print(f"\n   {sft[6]}[|]{sft[2]}{sft[1]} Menghapus data.\n")
                time.sleep(0.1)
                clear_screen()
                print(f"\n   {sft[6]}[\]{sft[2]}{sft[1]} Menghapus data..\n")
                time.sleep(0.1)
                clear_screen()
                print(f"\n   {sft[2]}{sft[1]}[-] Menghapus data......\n")
            clear_screen()
            removeline(baris)
            print(f"\n   {sft[2]}{sft[1]}Data berhasil dihapus!{sft[2]}")
            time.sleep(0.8)
        else:
            clear_screen()
            print(f"\n   {sft[2]}{sft[1]}{sft[4]}Password tidak sesuai!{sft[2]}")
            time.sleep(0.8)

    elif choice == "4":
        clear_screen()
        print(f"\n   {sft[0]}hint: admin123{sft[2]}")
        passw = getpass.getpass(f"   {sft[2]}{sft[1]}Masukan sandi untuk menghapus seluruh data:{sft[2]} ")
        if passw == "admin123":
            clear_screen()
            for i in range(3):
                clear_screen()
                print(f"\n   {sft[2]}{sft[1]}[/] Menghapus seluruh data\n")
                time.sleep(0.1)
                clear_screen()
                print(f"\n   {sft[5]}[|]{sft[2]}{sft[1]} Menghapus seluruh data.\n")
                time.sleep(0.1)
                clear_screen()
                print(f"\n   {sft[5]}[\]{sft[2]}{sft[1]} Menghapus seluruh data..\n")
                time.sleep(0.1)
                clear_screen()
                print(f"\n   {sft[7]}[-]{sft[2]}{sft[1]} Menghapus seluruh data...\n")
                time.sleep(0.1)
                clear_screen()
                print(f"\n   {sft[7]}[/]{sft[2]}{sft[1]} Menghapus seluruh data....\n")
                time.sleep(0.1)
                clear_screen()
                print(f"\n   {sft[6]}[|]{sft[2]}{sft[1]} Menghapus seluruh data.....\n")
                time.sleep(0.1)
                clear_screen()
                print(f"\n   {sft[6]}[\]{sft[2]}{sft[1]} Menghapus seluruh data.....\n")
                time.sleep(0.1)
                clear_screen()
                print(f"\n   {sft[2]}{sft[1]}[-] Menghapus seluruh data......\n")
            clear_screen()
            removealldata()
            print(f"\n   {sft[2]}{sft[1]}Data berhasil dihapus!{sft[2]}")
            time.sleep(0.8)
        else:
            clear_screen()
            print(f"\n   {sft[2]}{sft[1]}{sft[4]}Password tidak sesuai!{sft[2]}")
            time.sleep(0.8)
 """
