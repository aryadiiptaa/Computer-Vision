import cv2

# Tambahkan cv2.CAP_DSHOW (DirectShow) khusus untuk pengguna Windows
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

cap.set(cv2.CAP_PROP_SETTINGS, 1) 

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    cv2.imshow('Cek Lagging Kamera', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
