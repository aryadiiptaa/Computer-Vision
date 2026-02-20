import numpy as np

kamera = np.zeros((50, 100), dtype=np.uint8)

print(f"Dimensi Kamera (Baris/Y, Kolom/X): {kamera.shape}")

# Target yang mau diwarnai: X = 80 (Kanan), Y = 20 (Atas)
target_x = 80
target_y = 20

# === CARA BENAR ===
print("\nMencoba Cara Benar: kamera[Y, X]")
kamera[target_y, target_x] = 255
print("Berhasil! Program aman dan tidak crash.")


# === CARA SALAH (JEBAKAN) ===
print("\nMencoba Cara Salah: kamera[X, Y]")
print("Menunggu program crash...")
# Hapus tanda pagar (#) di bawah ini untuk melihat error aslinya:
# kamera[target_x, target_y] = 255