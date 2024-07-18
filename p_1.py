import cv2
from cv2 import typing

# Membaca citra digital dari file gambar
citra: typing.MatLike = cv2.imread("img/ak-hacker-baik.jpg")

# Menampilkan citra digital yang sudah dibaca
cv2.imshow("Hacker Baik - blue", citra[:, :, 0])
cv2.imshow("Hacker Baik - green", citra[:, :, 1])
cv2.imshow("Hacker Baik - red", citra[:, :, 2])

# Menampilkan matriks dari citra (BGR)
print("Matriks citra: \n", citra)
print("Matriks channel warna biru: \n", citra[:, :, 0])
print("Matriks channel warna hijau: \n", citra[:, :, 1])
print("Matriks channel warna merah: \n", citra[:, :, 2])

# Menunggu sampai user menekan sembarang tombol
cv2.waitKey(0)