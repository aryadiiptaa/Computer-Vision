import numpy as np
import matplotlib.pyplot as plt

# Membuat matriks 10 baris x 10 kolom berisi angka 0 (Hitam)
citra = np.zeros((10, 10), dtype=np.uint8)

# Ubah pixel di Baris ke-1, Kolom ke-1 menjadi Putih (255)
citra[1, 1] = 255

# Membuat garis vertikal Abu-abu (nilai 150)
# Dari Baris 3 s.d 8, di Kolom ke-5
citra[3:9, 5] = 150 

# Membuat kotak Putih (nilai 255)
# Rentang Baris 7 s.d 8, dan Kolom 7 s.d 8
citra[7:9, 7:9] = 255

# Menampilkan matriks sebagai gambar skala keabuan (grayscale)
plt.imshow(citra, cmap='gray', vmin=0, vmax=255)
plt.title("Hasil Visualisasi Matriks 10x10")

# Menambahkan grid merah untuk memperjelas batas tiap pixel
plt.grid(True, color='red', linestyle='-', linewidth=0.5) 
plt.show()

print(citra)