import tkinter as tk
from tkinter import ttk
import pyqrcode
from PIL import Image, ImageTk
import io
import time

class QRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time QR Code")
        self.label = ttk.Label(root)
        self.label.pack(pady=10)
        self.ts_label = ttk.Label(root, font=("Arial", 12))
        self.ts_label.pack()
        self.update_qr()

    def update_qr(self):
        timestamp = time.strftime("%m/%d/%Y %H:%M")
        self.ts_label.config(text=timestamp)
        qr_img = pyqrcode.create(timestamp, error='H')
        buffer = io.BytesIO()
        qr_img.png(buffer, scale=6)
        buffer.seek(0)
        img = Image.open(buffer)
        tk_img = ImageTk.PhotoImage(img)
        self.label.config(image=tk_img)
        self.label.image = tk_img
        self.root.after(1000, self.update_qr)

if __name__ == "__main__":
    root = tk.Tk()
    QRApp(root)
    root.mainloop()
