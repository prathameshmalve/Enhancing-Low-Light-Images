import streamlit as st
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import tempfile

# Function to enhance and process image
def enhance_image(image):
    img1 = cv2.resize(image, (812, 612))

    # Apply bilateral filter
    img = cv2.bilateralFilter(img1, 2, 10, 10)

    # Sharpening
    gaussian_blur = cv2.GaussianBlur(img, (5, 5), 2)
    img = cv2.addWeighted(img, 1, gaussian_blur, -0.5, 0)

    # Calculate the average pixel value
    avg_pixel_value = np.mean(img1)

    # Apply brightness and contrast based on pixel values
    if avg_pixel_value < 10:  # Very dark image
        matrix = np.ones(img.shape, dtype="uint8") * 5
        matrix1 = np.ones(img.shape) * 3
    elif avg_pixel_value > 10 and avg_pixel_value < 20:  # Medium dark image
        matrix = np.ones(img.shape, dtype="uint8") * 3
        matrix1 = np.ones(img.shape) * 2
    else:  # Bright images
        matrix = np.ones(img.shape, dtype="uint8") * 2
        matrix1 = np.ones(img.shape) * 2

    # Change brightness and contrast
    bright = cv2.add(img, matrix)
    contrast_bright = np.uint8(np.clip(cv2.multiply(np.float64(bright), matrix1), 0, 255))

    # Sharpening operation
    diff_img = cv2.absdiff(contrast_bright, img1)
    sharp_img = cv2.add(3 * diff_img, img1)

    # Increase saturation
    hsv_img = cv2.cvtColor(sharp_img, cv2.COLOR_BGR2HSV)
    hsv_img[..., 1] = np.uint8(np.clip(hsv_img[..., 1] * 1.3, 20, 150))
    sat_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)

    # Denoising
    denoised_img = cv2.fastNlMeansDenoisingColored(sat_img, None, 3, 3, 20, 15)

    return denoised_img


# Streamlit App
st.title("Enhance Low-Light Images")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png', 'bmp'])

if uploaded_file is not None:
    # Read the image file as an OpenCV image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    # Display the original image
    st.subheader("Original Image")
    st.image(image, channels="BGR")

    # Process the image using the enhancement function
    st.subheader("Processing...")
    enhanced_image = enhance_image(image)

    # Display the enhanced image
    st.subheader("Enhanced Image")
    st.image(enhanced_image, channels="BGR")

    # Allow users to download the enhanced image
    st.subheader("Download Enhanced Image")
    result = cv2.imencode('.jpg', enhanced_image)[1].tobytes()
    st.download_button(label="Download Enhanced Image", data=result, file_name="enhanced_image.jpg", mime="image/jpeg")
