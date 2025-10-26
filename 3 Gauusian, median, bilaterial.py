# exp3_smoothing_filters.py
import cv2

img_path = r"C:\Users\phata\OneDrive\Desktop\ChatGPT Image Oct 6, 2025, 08_19_49 PM.png"
img = cv2.imread(img_path)

gaussian = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)
bilateral = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

cv2.imshow("Original", img)
cv2.imshow("Gaussian Blur", gaussian)
cv2.imshow("Median Blur", median)
cv2.imshow("Bilateral Filter", bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
