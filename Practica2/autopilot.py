import cv2
import numpy as np

cap = cv2.VideoCapture("PracticaAutopilot.mp4")

while(1):
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)

    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength=50, maxLineGap=20)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0] if len(line.shape) > 1 else line
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

    cv2.imshow('Original', frame)
    cv2.imshow('Edges', edges)

    k = cv2.waitKey(25) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()