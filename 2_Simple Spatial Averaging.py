import cv2
import matplotlib.pyplot as plt

# Function to perform simple spatial averaging
def spatial_average(image, kernel_size):
    # Apply blur with specified kernel size
    blurred_image = cv2.blur(image, (kernel_size, kernel_size))
    return blurred_image

# Load image from full path
image_path = '1.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


# Perform spatial averaging for different kernel sizes
average_3x3 = spatial_average(image, 3)
average_10x10 = spatial_average(image, 10)
average_20x20 = spatial_average(image, 20)

# Display original and spatially averaged images side by side
plt.figure(figsize=(15, 5))

plt.subplot(1, 4, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 4, 2)
plt.imshow(average_3x3, cmap='gray')
plt.title('3x3 Average')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.imshow(average_10x10, cmap='gray')
plt.title('10x10 Average')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.imshow(average_20x20, cmap='gray')
plt.title('20x20 Average')
plt.axis('off')

plt.show()