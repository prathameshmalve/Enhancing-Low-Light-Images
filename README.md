
# Image Enhancement Web App

This project is a web-based application built using **Streamlit** that enhances low-light images using custom image processing techniques. The app allows users to upload low-light images, process them with brightness, contrast, and sharpening adjustments, and download the enhanced image.

## Features

- **Image Upload**: Users can upload images in common formats like `.jpg`, `.jpeg`, `.png`, `.bmp`.
- **Low-Light Image Enhancement**: The app processes low-light images using bilateral filtering, brightness adjustments, contrast enhancement, and sharpening.
- **Saturation Increase**: Automatically adjusts saturation to improve image quality.
- **Denoising**: Uses non-local means denoising to reduce image noise.
- **Download Enhanced Image**: Users can download the enhanced image after processing.

## Demo

[Provide a link to a live demo if available.]

## Installation

To run this web app locally, follow the steps below.

### Prerequisites

- **Python 3.7+**
- The following Python packages:
  - `streamlit`
  - `opencv-python-headless`
  - `numpy`
  - `scikit-image`

### Installation Steps

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Install dependencies**:

    Using pip:

    ```bash
    pip install -r requirements.txt
    ```

    You can manually install the dependencies by running:

    ```bash
    pip install streamlit opencv-python-headless numpy tqdm scikit-image
    ```

3. **Run the application**:

    Start the Streamlit app by running:

    ```bash
    streamlit run app.py
    ```

4. **Access the web app**:

    After running the above command, the app will be hosted locally. You can access it in your browser at:

    ```
    http://localhost:8501
    ```

## Usage

1. Upload a low-light image using the **Upload Image** button.
2. The app will process and enhance the image using custom image processing techniques.
3. View the original and enhanced images on the web interface.
4. Download the enhanced image by clicking the **Download Enhanced Image** button.



## License

[MIT License](LICENSE)
