import os
import time
#kode ansi kabur 0-dim, 1-bold, 2-reset, 3-italic, 4-Red, 5-Cyan, 6-Magenta, 7-Yellow
sft = ["\033[90m", "\033[1m", "\033[0m", "\033[3m", "\033[91m", "\033[96m", "\033[95m", "\033[93m"]


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def loading(display):
    for i in range(3):
            clear_screen()
            print(f"\n   {sft[2]}{sft[1]}[/] {display}\n")
            time.sleep(0.1)
            clear_screen()
            print(f"\n   {sft[5]}[|]{sft[2]}{sft[1]} {display}.\n")
            time.sleep(0.1)
            clear_screen()
            print(f"\n   {sft[5]}[\]{sft[2]}{sft[1]} {display}..\n")
            time.sleep(0.1)
            clear_screen()
            print(f"\n   {sft[7]}[-]{sft[2]}{sft[1]} {display}...\n")
            time.sleep(0.1)
            clear_screen()
            print(f"\n   {sft[7]}[/]{sft[2]}{sft[1]} {display}....\n")
            time.sleep(0.1)
            clear_screen()
            print(f"\n   {sft[6]}[|]{sft[2]}{sft[1]} {display}.....\n")
            time.sleep(0.1)
            clear_screen()
            print(f"\n   {sft[6]}[\]{sft[2]}{sft[1]} {display}.....\n")
            time.sleep(0.1)
            clear_screen()
            print(f"\n   {sft[2]}{sft[1]}[-] {display}......\n")