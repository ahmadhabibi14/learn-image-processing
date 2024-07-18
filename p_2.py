import cv2
from cv2 import typing
import numpy as np

# Membaca citra digital dari file gambar
citra: typing.MatLike = cv2.imread("img/ak-hacker-baik.jpg")

# Membaca channel warna BGR dan menyimpannya ke dalam variable terpisah
b = citra[:, :, 0]
g = citra[:, :, 1]
r = citra[:, :, 2]

# citra_gray = cv2.cvtColor(citra, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Hacker Baik - rgb", citra)
# cv2.imshow("Hacker Baik - gray", citra_gray)

# Menyimpan jumlah baris dan kolom
total_row = len(citra)
total_col = len(citra[0])

# Citra baru dengan nilai 0
citra_gray = np.zeros((total_row, total_col))

for row in range(total_row):
  for col in range(total_col):
    citra_gray[row, col] = round(0.299 * r[row, col] + 0.587 * g[row, col] + 0.114 * b[row, col])

citra_gray = citra_gray.astype(np.uint8)

cv2.imshow("Hacker Baik - gray", citra_gray)

# Menunggu sampai user menekan sembarang tombol
cv2.waitKey(0)