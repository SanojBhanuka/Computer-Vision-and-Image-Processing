import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to perform block averaging
def block_average(image, block_size):
    # Calculate dimensions of blocks
    h, w = image.shape[:2]
    bh, bw = h // block_size, w // block_size

    # Iterate over blocks
    for i in range(bh):
        for j in range(bw):
            # Extract current block
            block = image[i * block_size:(i + 1) * block_size, j * block_size:(j + 1) * block_size]

            # Calculate average intensity
            avg_intensity = np.mean(block)

            # Replace current block with average intensity
            image[i * block_size:(i + 1) * block_size, j * block_size:(j + 1) * block_size] = avg_intensity

    return image

# Load image from full path
image_path = '1.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Perform block averaging for different block sizes
block_3x3 = block_average(image.copy(), 3)
block_5x5 = block_average(image.copy(), 5)
block_7x7 = block_average(image.copy(), 7)

# Display original and block-averaged images side by side
plt.figure(figsize=(15, 5))

plt.subplot(1, 4, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 4, 2)
plt.imshow(block_3x3, cmap='gray')
plt.title('3x3 Block Average')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.imshow(block_5x5, cmap='gray')
plt.title('5x5 Block Average')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.imshow(block_7x7, cmap='gray')
plt.title('7x7 Block Average')
plt.axis('off')

plt.show()