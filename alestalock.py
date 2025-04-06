import os
import marshal, zlib, base64
from colorama import Fore, Style

def ascii_logo():
    print(Fore.LIGHTCYAN_EX)  # Mavi
    print(r"""
 █████╗ ██╗     ███████╗███████╗████████╗ █████╗
██╔══██╗██║     ██╔════╝██╔════╝╚══██╔══╝██╔══██╗
███████║██║     █████╗  ███████╗   ██║   ███████║
██╔══██║██║     ██╔══╝  ╚════██║   ██║   ██╔══██║
██║  ██║███████╗███████╗███████║   ██║   ██║  ██║
╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝
        Alesta-Şifreleme v1.0
       ----------------—------
    """)
    print(Fore.LIGHTRED_EX + "       Powered by: @Alestavia" + Style.RESET_ALL)  # Kırmızı ve resetle

def sifrele(dosya_adi):
    os.system('clear')  # Ekranı temizle
    try:
        with open(dosya_adi, "r", encoding="utf-8") as f:
            kod = f.read()

        derlenmis_kod = compile(kod, "<sifreli>", "exec")
        marshallenmis = marshal.dumps(derlenmis_kod)
        zlibli = zlib.compress(marshallenmis)
        b64li = base64.b64encode(zlibli)

        # Dosya adı değiştirilmeden aynı isimle şifreli dosya oluşturuluyor
        with open(dosya_adi, "w", encoding="utf-8") as f:
            f.write("import marshal,zlib,base64\n")
            f.write("exec(marshal.loads(zlib.decompress(base64.b64decode(")
            f.write(repr(b64li))
            f.write("))))")

        print(f"\n\033[92m[✓] Şifreleme tamamlandı! --> {dosya_adi} üzerine şifrelendi.\033[0m\n")
    except FileNotFoundError:
        print("\n\033[91m[!] Dosya bulunamadı!\033[0m\n")

def dosya_ismi_degistir():
    os.system('clear')  # Ekranı temizle
    eski = input("Eski dosya ismini gir: ")
    yeni = input("Yeni dosya ismini gir: ")
    try:
        os.rename(eski, yeni)
        print(f"\n\033[92m[✓] Dosya ismi '{eski}' → '{yeni}' olarak değiştirildi.\033[0m\n")
    except Exception as e:
        print(f"\n\033[91m[!] Hata: {e}\033[0m\n")

def ana_menu():
    while True:
        os.system('clear')  # Ekranı temizle
        ascii_logo()
        print(Fore.CYAN + "1. Tool → Şifrele" + Style.RESET_ALL +  Style.BRIGHT)
        print(Fore.LIGHTCYAN_EX + "2. Tool → Dosya İsmi Değiştir" + Style.RESET_ALL +  Style.BRIGHT)
        print(Fore.BLUE + "3. Çıkış Yap" + Style.RESET_ALL +  Style.BRIGHT)
        secim = input(Fore.GREEN +  "\nSeçim yap: " + Style.BRIGHT + Style.RESET_ALL)

        if secim == "1":
            dosya = input(Fore.LIGHTCYAN_EX + "[!]-Şifrelenecek dosya ismini girin: " + Style.RESET_ALL)
            sifrele(dosya)
            input(Fore.LIGHTCYAN_EX + "Devam etmek için ENTER..." + Style.RESET_ALL)
        elif secim == "2":
            dosya_ismi_degistir()
            input("Devam etmek için ENTER...")
        elif secim == "3":
            print(Fore.LIGHTMAGENTA_EX + "\nGüle güle Reis!\n" + Style.RESET_ALL)
            break
        else:
            print("\n\033[91mGeçersiz seçim!\033[0m\n" )
            input("Devam etmek için ENTER...")

# Başlat
ana_menu()
