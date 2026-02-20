import cv2
import numpy as np

# 1. Bikin gambar berwarna (Perhatikan angka '3' di belakang)
citra_warna = np.zeros((100, 100, 3), dtype=np.uint8)

# 2. Konversi ke Grayscale
citra_abu = cv2.cvtColor(citra_warna, cv2.COLOR_BGR2GRAY)

# 3. Cek jumlah data yang harus dihitung CPU robot
print(f"Bentuk Citra Warna    : {citra_warna.shape} , Total: {citra_warna.size} titik angka")
print(f"Bentuk Citra Grayscale: {citra_abu.shape}    , Total: {citra_abu.size} titik angka")

# Kesimpulan: Grayscale menghilangkan 2 channel ekstra, memotong beban CPU hingga 66%!