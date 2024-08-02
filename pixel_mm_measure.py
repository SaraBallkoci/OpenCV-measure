import cv2
import numpy as np

PPM = 160.86 / 22
print(f"Pixels per millimeter (PPM): {PPM:.4f}")

points = []
img = None

def click_event(event, x, y, flags, param):
    global points, img, PPM
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
        if len(points) == 2:
            distance_px = np.sqrt((points[0][0] - points[1][0]) ** 2 + (points[0][1] - points[1][1]) ** 2)
            print(f"Distance between points: {distance_px:.2f} pixels")

            cv2.line(img, points[0], points[1], (255, 0, 0), 2)

            distance_mm = distance_px / PPM
            midpoint = ((points[0][0] + points[1][0]) // 2, (points[0][1] + points[1][1]) // 2)
            cv2.putText(img, f"{distance_px:.2f} px", midpoint, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            cv2.putText(img, f"{distance_mm:.2f} mm", (midpoint[0], midpoint[1] + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
            points = []

        cv2.imshow('Image', img)

img = cv2.imread('tooth.jpeg')
points = []

if img is None:
    print("Error: Image not found. Please check the file path.")
else:
    cv2.imshow('Image', img)
    cv2.setMouseCallback('Image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()