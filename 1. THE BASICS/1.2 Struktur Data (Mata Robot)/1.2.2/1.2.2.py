import numpy as np
import matplotlib.pyplot as plt

# 1. Buat arena hitam (Tinggi 100, Lebar 100)
citra = np.zeros((100, 100), dtype=np.uint8)

# 2. Kita buat dua titik di sumbu X yang sama (Tengah, X = 50)
x_tengah = 50

# Titik A: Y kecil (Nilai 10) -> Kita beri warna Putih Terang (255)
# Ingat: Aksesnya [Y, X]
citra[10, x_tengah] = 255 

# Titik B: Y besar (Nilai 90) -> Kita beri warna Abu-abu (100)
citra[90, x_tengah] = 100 

# 3. Tampilkan Visualisasinya
plt.imshow(citra, cmap='gray', vmin=0, vmax=255)
plt.title("Pembuktian Sistem Koordinat Y")
plt.xlabel("Sumbu X (Semakin ke kanan makin besar)")
plt.ylabel("Sumbu Y (Semakin ke BAWAH makin besar)")
plt.grid(True, color='red', linestyle=':', linewidth=0.5)

# Matplotlib secara default mengikuti OpenCV (Y ke bawah), 
# jadi kita tidak perlu membalik sumbunya lagi.
plt.show()