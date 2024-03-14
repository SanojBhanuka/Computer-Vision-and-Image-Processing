import cv2
import matplotlib.pyplot as plt


# Function to rotate an image by a specified angle
def rotate_image(image, angle):
    # Get image center and rotation matrix
    (h, w) = image.shape[:2]
    center = (w / 2, h / 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Perform rotation
    rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))
    return rotated_image


# Load image from full path
image_path = '1.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


# Rotate image by specified angles
rotated_45 = rotate_image(image, 45)
rotated_90 = rotate_image(image, 90)

# Display original and rotated images side by side
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(rotated_45, cmap='gray')
plt.title('Rotated 45°')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(rotated_90, cmap='gray')
plt.title('Rotated 90°')
plt.axis('off')

plt.show()