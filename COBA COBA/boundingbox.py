import cv2

cam =  cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    if not ret:
        print("rusak kamera lu kali")
        break

    kiri_atas = (150,100)
    kanan_bawah = (450,400)

    warna = (0,0,255)
    ketebalan = 2

    cv2.rectangle(frame, kiri_atas, kanan_bawah, warna, ketebalan)

    cv2.imshow('kamera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()