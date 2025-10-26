import cv2

# 1. Read the image from a file
# Note: The path in the image is unreadable. 
# You must change "your_image_path.jpg" to the actual path of your image.
image = cv2.imread("your_image_path.jpg") 

# 2. Display the original image
cv2.imshow("original image", image)
cv2.waitKey(0)

# 3. Resize the image to 300x300 pixels
resized = cv2.resize(image, (300, 300))
cv2.imshow("Resized image", resized)
cv2.waitKey(0)

# 4. Crop the image
# This takes a slice of the image from y-coordinates 100 to 200
# and x-coordinates 200 to 300.
cropped = image[100:200, 200:300]
cv2.imshow("Cropped image", cropped)
cv2.waitKey(0)

# 5. Rotate the image 90 degrees clockwise
rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Rotated image", rotated)
cv2.waitKey(0)

# 6. Close all the display windows
cv2.destroyAllWindows()
