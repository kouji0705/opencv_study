import cv2

image = cv2.imread("sample.jpg")

print("画像サイズ:", image.shape)

pixel = image[100, 200]

print("100行目、200列目のピクセル:", pixel)