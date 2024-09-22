import random

def sayi_tahmin_oyunu():
    sayi = random.randint(1, 100)
    tahmin = 0
    print("1 ile 100 arasında bir sayı tahmin et!")

    while tahmin != sayi:
        tahmin = int(input("Tahminin: "))
        if tahmin < sayi:
            print("Daha yüksek bir sayı dene.")
        elif tahmin > sayi:
            print("Daha düşük bir sayı dene.")
    
    print("Tebrikler! Doğru tahmin ettin!")

sayi_tahmin_oyunu()
