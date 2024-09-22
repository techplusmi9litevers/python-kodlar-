import os
import sys

def onay_mesaji():
    vbs_kodu = '''
    Dim msg
    msg = MsgBox("⚠️ Dikkat! Bu uygulama, cihazınızda kalıcı değişiklikler yapabilir." & vbCrLf & _
                  "Cihazınızda işlem yapmadan önce tüm verilerinizi yedekleyin." & vbCrLf & _
                  "Bu uygulamayı kullanarak herhangi bir sorumluluk kabul etmiyorsunuz." & vbCrLf & _
                  "Devam etmek istiyor musunuz?", vbYesNo + vbCritical, "Uyarı")
    If msg = vbNo Then
        WScript.Quit
    End If
    '''
    with open("onay.vbs", "w") as f:
        f.write(vbs_kodu)
    
    os.system("cscript //nologo onay.vbs")
    os.remove("onay.vbs")  # VBS dosyasını sildik

def fastboot_komutlari():
    print("Fastboot Komutları Uygulaması 🚀")
    print("1: Sistemi sil")
    print("2: Cache'i sil")
    print("3: Data'yı sil")
    print("4: Boot'u sil")
    print("5: NV'i sil")
    print("6: Vendor'ı sil")
    print("7: Cust'ı sil")
    print("8: Internal Storage sil")
    print("9: EFS sil")
    print("10: Logoyu sil")
    print("11: Sistemi yeniden başlat")
    print("12: Recovery'yi yeniden başlat")
    print("0: Çıkış")

    while True:
        secim = input("Bir seçim yapın (0-12): ")
        
        if secim == '1':
            os.system('fastboot erase system')
            print("Sistem siliniyor...")
        elif secim == '2':
            os.system('fastboot erase cache')
            print("Cache siliniyor...")
        elif secim == '3':
            os.system('fastboot erase data')
            print("Data siliniyor...")
        elif secim == '4':
            os.system('fastboot erase boot')
            print("Boot siliniyor...")
        elif secim == '5':
            os.system('fastboot erase nv')
            print("NV siliniyor...")
        elif secim == '6':
            os.system('fastboot erase vendor')
            print("Vendor siliniyor...")
        elif secim == '7':
            os.system('fastboot erase cust')
            print("Cust siliniyor...")
        elif secim == '8':
            os.system('fastboot erase userdata')
            print("Internal Storage siliniyor...")
        elif secim == '9':
            os.system('fastboot erase efs')
            print("EFS siliniyor...")
        elif secim == '10':
            os.system('fastboot erase logo')
            print("Logo siliniyor...")
        elif secim == '11':
            os.system('fastboot reboot')
            print("Sistem yeniden başlatılıyor...")
        elif secim == '12':
            os.system('fastboot reboot recovery')
            print("Recovery yeniden başlatılıyor...")
        elif secim == '0':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    onay_mesaji()  # Onay mesajını göster
    fastboot_komutlari()
