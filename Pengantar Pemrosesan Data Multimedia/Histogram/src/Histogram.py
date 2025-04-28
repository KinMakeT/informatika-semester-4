import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# 1. Pilih gambar lewat dialog
Tk().withdraw()  # Menyembunyikan jendela utama
filename = askopenfilename(
    title="Pilih gambar",
    filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
)

if not filename:
    print("Tidak ada file dipilih.")
    exit()

# 2. Baca gambar
img = cv2.imread(filename)

if img is None:
    print("Gagal membaca gambar!")
    exit()

# 3. Konversi ke grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 4. Membuat histogram
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# 5. Hitung statistik
mean = np.mean(gray)
variance = np.var(gray)
std_dev = np.std(gray)

# 6. Analisa gambar
def analyze_image(mean, std_dev):
    if mean < 85:
        brightness = "Gelap"
    elif mean > 170:
        brightness = "Terang"
    else:
        brightness = "Normal"
    
    if std_dev < 30:
        contrast = "Kontras Rendah"
    elif std_dev > 70:
        contrast = "Kontras Tinggi"
    else:
        contrast = "Kontras Sedang"
    
    return brightness, contrast

brightness, contrast = analyze_image(mean, std_dev)

# 7. Tampilkan hasil
print(f"Rata-rata pixel: {mean:.2f}")
print(f"Variansi: {variance:.2f}")
print(f"Standar deviasi: {std_dev:.2f}")
print(f"Kondisi gambar: {brightness}, {contrast}")

# 8. Tampilkan gambar dan histogram
plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.imshow(gray, cmap='gray')
plt.title(f'Gambar Grayscale ({brightness}, {contrast})')
plt.axis('off')

plt.subplot(1,2,2)
plt.plot(hist, color='black')
plt.title('Histogram Intensitas Grayscale')
plt.xlabel('Intensitas Pixel (0-255)')
plt.ylabel('Jumlah Pixel')
plt.grid()

plt.tight_layout()
plt.show()
