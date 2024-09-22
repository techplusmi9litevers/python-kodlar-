import os
import time
import random

def temizle_ekran():
    os.system('cls' if os.name == 'nt' else 'clear')

def cicek_acma(reng):
    print(f"\nRenk: {reng.upper()}")
    print("Çiçek açıyor... 🌸\n")

    for i in range(1, 11):
        time.sleep(0.3)
        temizle_ekran()
        print(" " * (10 - i) + "🌼" + "🌿" * (i - 1))
    
    print("\nÇiçek açtı! 🌼🌼🌼")
    time.sleep(1)

def ana_menu():
    print("Sanal Çiçek Açma Simülasyonu 🌸")
    renkler = ["kırmızı", "mavi", "sarı", "yeşil", "pembe", "mor"]
    
    while True:
        print("\nRenk Seçin:")
        for i, renk in enumerate(renkler, 1):
            print(f"{i}. {renk.capitalize()}")
        print("0. Çıkış")
        
        secim = input("Seçiminizi yapın: ")
        
        if secim.isdigit():
            secim = int(secim)
            if secim in range(1, len(renkler) + 1):
                cicek_acma(renkler[secim - 1])
            elif secim == 0:
                print("Çıkış yapılıyor...")
                break
            else:
                print("Geçersiz seçim. Lütfen tekrar deneyin.")
        else:
            print("Lütfen bir sayı girin.")

if __name__ == "__main__":
    ana_menu()
