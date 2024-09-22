class Kitap:
    def __init__(self, ad, yazar, yayin_yili):
        self.ad = ad
        self.yazar = yazar
        self.yayin_yili = yayin_yili

class Kutuphane:
    def __init__(self):
        self.kitaplar = []

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)
        print(f"{kitap.ad} kitabı kütüphaneye eklendi.")

    def kitap_listele(self):
        if not self.kitaplar:
            print("Kütüphanede hiç kitap yok.")
            return
        print("Kütüphanedeki Kitaplar:")
        for i, kitap in enumerate(self.kitaplar, start=1):
            print(f"{i}. {kitap.ad} - {kitap.yazar} ({kitap.yayin_yili})")

    def kitap_arama(self, arama):
        bulunan_kitaplar = [kitap for kitap in self.kitaplar if arama.lower() in kitap.ad.lower() or arama.lower() in kitap.yazar.lower()]
        if not bulunan_kitaplar:
            print("Aradığınız kitap bulunamadı.")
            return
        print("Bulunan Kitaplar:")
        for kitap in bulunan_kitaplar:
            print(f"{kitap.ad} - {kitap.yazar} ({kitap.yayin_yili})")

def menu():
    kutuphane = Kutuphane()
    while True:
        print("\nKütüphane Yönetim Sistemi")
        print("1. Kitap Ekle")
        print("2. Kitap Listele")
        print("3. Kitap Ara")
        print("4. Çıkış")
        
        secim = input("Bir seçenek girin: ")

        if secim == "1":
            ad = input("Kitap adı: ")
            yazar = input("Yazar adı: ")
            yayin_yili = input("Yayın yılı: ")
            kitap = Kitap(ad, yazar, yayin_yili)
            kutuphane.kitap_ekle(kitap)

        elif secim == "2":
            kutuphane.kitap_listele()

        elif secim == "3":
            arama = input("Aramak istediğiniz kitap veya yazar: ")
            kutuphane.kitap_arama(arama)

        elif secim == "4":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

menu()
