# ImageManipulation - numpy-based Image Processing Mini Project

## Overview
This project demonstrates fundamental image processing techniques using **only numpy**, giving a hands-on understanding of how digital images work at the pixel level. It is designed as a mini project for learning **computer vision basics**, with a focus on numpy operations commonly used in AI and ML workflows.

---

## Tech Stack
- **Python 3**
- **numpy** - for array manipulation and vectorized operations
- **Pillow (PIL)** - for loading images
- **matplotlib** - for displaying images

---

## Features Implemented

1. **Load and visualize images**  
   - Images are converted to numpy arrays and displayed using matplotlib.

2. **Convert RGB to Grayscale**  
   - Implemented using weighted sum: `Gray = 0.299*R + 0.587*G + 0.114*B`.

3. **Normalize Pixel Values**  
   - Pixel values converted from `[0, 255]` to `[0, 1]` for ML-ready data.

4. **Adjust Brightness and Contrast**  
   - Brightness: add or subtract a constant value to pixels.  
   - Contrast: scale pixel differences from the mean.

5. **Flip Images Horizontally and Vertically**  
   - Implemented using numpy slicing.

6. **Apply Blur Filter**  
   - Implemented a 3x3 mean filter both with loops and fully vectorized numpy.

7. **Edge Detection**  
   - Implemented a Sobel-like filter (X-direction) using loops and fully vectorized operations.

---

## Learning Outcomes

- Strong understanding of **numpy arrays, slicing, and broadcasting**.  
- Applied **vectorized operations** for efficient image manipulation.  
- Gained experience with **convolution basics**, the foundation of CNNs.  
- Learned how to process **grayscale and RGB images**.  
- Developed a mini CV workflow from scratch, fully in Python.

---


---

## How to Run

1. Install dependencies:  
```bash
pip install numpy pillow matplotlib
```
2. Place your image in the `images/` folder
3. Run the main script
```bash
python main.py
```
4. Observe grayscale conversion, brightness/contrast adjustment, flipping, blurring, and edge detection.

### Notes

> All image processing is implemented from scratch using numpy, no OpenCV or other CV libraries.

> Vectorized implementations demonstrate performance optimization for large images.

> Ideal for learning image processing fundamentals and preparing for AI/ML projects.

---