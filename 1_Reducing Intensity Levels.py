import cv2
import numpy as np
import matplotlib.pyplot as plt


# Function to reduce the number of intensity levels in an image
def reduce_intensity_levels(image, levels):
    # Calculate the scaling factor
    factor = 256 / levels

    # Perform intensity level reduction
    reduced_image = np.floor(image / factor) * factor

    return reduced_image.astype(np.uint8)


# Load image from full path
image_path = '1.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Perform intensity level reduction
levels = 4  # Variable input for intensity levels
reduced_image = reduce_intensity_levels(image, levels)

# Display original and reduced images side by side
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(reduced_image, cmap='gray')
plt.title('Reduced Image')
plt.axis('off')

plt.show()
