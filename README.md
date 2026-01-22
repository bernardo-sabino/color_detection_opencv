# Real-Time Color Detector using OpenCV

A Python application for real-time color detection and object tracking using computer vision techniques. This project demonstrates fundamental concepts of image segmentation, morphological operations, and contour detection applied to video streams.

## 📋 Context

This repository is part of my portfolio in **Robotics and Computer Vision**. The goal of this script is to provide an implementation of color-based segmentation, which is a foundational technique for vision-based control in robotics (e.g., following a colored line or tracking a specific object).

## 🛠️ Techniques & Concepts

The core pipeline processes the video feed through the following stages:

1.  **Color Space Conversion (BGR to HSV):**
    The frames are converted to the HSV (Hue, Saturation, Value) color space. HSV is preferred over RGB for color detection because it separates color information (Hue) from intensity (Value), making the detection more robust to lighting changes.

2.  **Thresholding & Segmentation:**
    A binary mask is created using `cv2.inRange`. This isolates pixels that fall within the specific HSV range defined for the target color.

3.  **Morphological Operations:**
    To reduce noise and improve the mask quality, two morphological transformations are applied:
    * **Opening (`cv2.MORPH_OPEN`):** Erosions followed by dilations. Used to remove small background noise (salt noise).
    * **Closing (`cv2.MORPH_CLOSE`):** Dilations followed by erosions. Used to close small holes inside the foreground object.

4.  **Contour Detection & Bounding Box:**
    The algorithm finds contours in the binary mask (`cv2.findContours`) and filters them by area to ignore artifacts. Finally, a bounding box (`cv2.boundingRect`) is drawn around the largest detected objects.

## ⚙️ Configuration & Tuning

The script includes a **Tuning Mode** to help find the correct HSV values for a specific object in your environment.

To enable it, change the constant in the script:

```python
TUNING = True
```
When enabled, a window with 6 trackbars will appear, allowing you to adjust the Lower and Upper bounds for Hue, Saturation, and Value in real-time.

## 🚀 How to Run

### Prerequisites
* Python 3.x installed
* A functional webcam connected

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/bernardo-sabino/color_detection_opencv.git 
    cd color_detection_opencv
    ```

2.  **Install the dependencies:**
    Ensure you are in the project directory and run:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the script:**
    ```bash
    python color_detector.py
    ```

Press **`q`** on your keyboard to quit the application.

## 👤 Author

**Bernardo Sabino**

* **Education:** Control and Automation Engineering Student at UFMG | Industrial Automation Technician (SENAI-MG)
* **Interests:** Robotics, Computer Vision, ROS/ROS 2, and Embedded Systems.
* **Connect with me:** [LinkedIn](https://www.linkedin.com/in/bernardosab/) | [GitHub](https://github.com/bernardo-sabino)

---
*Developed as part of my studies in Computer Vision algorithms.*