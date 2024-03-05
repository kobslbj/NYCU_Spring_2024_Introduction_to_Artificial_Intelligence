import cv2
import numpy as np

# 讀取原始圖片
image = cv2.imread('image.png')

# 平移
def translate(image, x, y):
    rows, cols = image.shape[:2]
    M = np.float32([[1, 0, x], [0, 1, y]])
    translated = cv2.warpAffine(image, M, (cols, rows))
    return translated

# 旋轉
def rotate(image, angle):
    rows, cols = image.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    rotated = cv2.warpAffine(image, M, (cols, rows))
    return rotated

# 翻轉
def flip(image, flip_code):
    flipped = cv2.flip(image, flip_code)
    return flipped

# 縮放
def scale(image, scale_factor):
    scaled = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)
    return scaled

# 裁剪
def crop(image, x, y, width, height):
    cropped = image[y:y+height, x:x+width]
    return cropped

translated_image = translate(image, 50, 50)
rotated_image = rotate(image, 45)
flipped_image = flip(image, 1)  
scaled_image = scale(image, 1.5)
cropped_image = crop(image, 100, 100, 300, 300)

cv2.imwrite('translated_image.png', translated_image)
cv2.imwrite('rotated_image.png', rotated_image)
cv2.imwrite('flipped_image.png', flipped_image)
cv2.imwrite('scaled_image.png', scaled_image)
cv2.imwrite('cropped_image.png', cropped_image)
