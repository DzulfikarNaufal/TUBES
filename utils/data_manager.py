#kode ansi kabur 0-dim, 1-bold, 2-reset, 3-italic, 4-Red, 5-Cyan, 6-Magenta, 7-Yellow
sft = ["\033[90m", "\033[1m", "\033[0m", "\033[3m", "\033[91m", "\033[96m", "\033[95m", "\033[93m"]


def formatteddata():
    clear_screen()
    isi = baca_mahasiswa()
    test = 0
    print(f"\n   {sft[2]}{sft[1]}======] Daftar Mahasiwa [======{sft[2]}\n")
    for index, baris in enumerate(isi):
        index += 1
        print(f"   {sft[2]}{sft[1]} Data-{index}\n     Nama : {sft[5]}{isi[test][1]}\n{sft[2]}{sft[1]}     NIM  : {sft[5]}{isi[test][0]}\n{sft[2]}{sft[1]}     IPK  : {sft[5]}{isi[test][2]}\n{sft[1]}")
        test += 1 