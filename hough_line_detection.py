import cv2
import numpy as np

# Step 1: Read the image
img = cv2.imread("lines_sample.jpg")
if img is None:
    print("Error: Image not found! Make sure 'lines_sample.jpg' is in the same folder.")
    exit()

# Step 2: Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 3: Use Canny edge detection to find edges
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Step 4: Apply Hough Transform to detect lines
lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)

# Step 5: Draw detected lines on the original image
if lines is not None:
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)  # red line

# Step 6: Show the result
cv2.imshow("Original Image with Detected Lines", img)
cv2.imshow("Edge Detection (Canny)", edges)

# Step 7: Wait until a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
