class Gorev:
    def __init__(self, ad):
        self.ad = ad
        self.tamamlandi = False

    def tamamla(self):
        self.tamamlandi = True

    def __str__(self):
        durum = "✓" if self.tamamlandi else "✗"
        return f"{durum} {self.ad}"

class GorevYonetimi:
    def __init__(self):
        self.gorevler = []

    def gorev_ekle(self, gorev):
        self.gorevler.append(gorev)
        print(f"Görev eklendi: {gorev.ad}")

    def gorev_listele(self):
        if not self.gorevler:
            print("Görev listesi boş.")
            return
        print("Görev Listesi:")
        for i, gorev in enumerate(self.gorevler, start=1):
            print(f"{i}. {gorev}")

    def gorev_tamamla(self, index):
        try:
            self.gorevler[index - 1].tamamla()
            print(f"Görev tamamlandı: {self.gorevler[index - 1].ad}")
        except IndexError:
            print("Geçersiz görev numarası.")

    def gorev_sil(self, index):
        try:
            silinen_gorev = self.gorevler.pop(index - 1)
            print(f"Görev silindi: {silinen_gorev.ad}")
        except IndexError:
            print("Geçersiz görev numarası.")

def menu():
    yonetim = GorevYonetimi()
    while True:
        print("\nGörev Yönetim Sistemi")
        print("1. Görev Ekle")
        print("2. Görev Listele")
        print("3. Görev Tamamla")
        print("4. Görev Sil")
        print("5. Çıkış")
        
        secim = input("Bir seçenek girin: ")

        if secim == "1":
            ad = input("Görev adı: ")
            gorev = Gorev(ad)
            yonetim.gorev_ekle(gorev)

        elif secim == "2":
            yonetim.gorev_listele()

        elif secim == "3":
            yonetim.gorev_listele()
            index = int(input("Tamamlamak istediğiniz görev numarasını girin: "))
            yonetim.gorev_tamamla(index)

        elif secim == "4":
            yonetim.gorev_listele()
            index = int(input("Silmek istediğiniz görev numarasını girin: "))
            yonetim.gorev_sil(index)

        elif secim == "5":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

menu()
