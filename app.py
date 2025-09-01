import tkinter as tk
from tkinter import messagebox
from datetime import date

def show_message():
    messagebox.showinfo("Ucapan", f"Selamat Ulang Tahun, {name_entry.get()}! 🎉\nSemoga sehat dan bahagia selalu.")

# Membuat jendela utama
root = tk.Tk()
root.title("Birthday Greeting Card")
root.geometry("400x300")
root.configure(bg="#FFDEE9")

# Judul
title = tk.Label(root, text="🎂 Happy Birthday! 🎂", font=("Arial", 20, "bold"), bg="#FFDEE9", fg="#800080")
title.pack(pady=10)

# Input nama
label_name = tk.Label(root, text="Masukkan nama:", font=("Arial", 12), bg="#FFDEE9")
label_name.pack()

name_entry = tk.Entry(root, font=("Arial", 12), justify="center")
name_entry.pack(pady=5)

# Tombol
btn = tk.Button(root, text="Tampilkan Ucapan", font=("Arial", 12, "bold"), bg="#FFB6C1", command=show_message)
btn.pack(pady=20)

# Footer
footer = tk.Label(root, text=f"Created on {date.today()}", font=("Arial", 10, "italic"), bg="#FFDEE9")
footer.pack(side="bottom", pady=10)

# Jalankan program
root.mainloop()

    


