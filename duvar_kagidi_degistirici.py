import tkinter as tk
from tkinter import filedialog, messagebox
import ctypes

def duvar_kagidi_yap():
    resim_yolu = filedialog.askopenfilename(title="Resim Dosyasını Seçin", filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
    if resim_yolu:
        try:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, resim_yolu, 0)
            messagebox.showinfo("Başarılı", "Duvar kağıdı başarıyla değiştirildi!")
        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Duvar Kağıdı Değiştirici")

# Duvar kağıdını değiştiren buton
button = tk.Button(root, text="Duvar Kağıdını Değiştir", command=duvar_kagidi_yap)
button.pack(pady=20)

# Uygulamayı çalıştır
root.mainloop()

# Terminalin kapanmasını engellemek için bir bekleme ekle
input("Çıkmak için bir tuşa basın...")
