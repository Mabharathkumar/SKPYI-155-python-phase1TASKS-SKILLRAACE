import cv2
import numpy as np
import pyautogui

# Define the screen resolution
screen_size = pyautogui.size()

# Define the codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")

# Define the video writer object
out = cv2.VideoWriter("screen_record.avi", fourcc, 20.0, screen_size)

# Create a loop to capture the screen
try:
    while True:
        # Take a screenshot
        img = pyautogui.screenshot()

        # Convert the screenshot to a numpy array
        frame = np.array(img)

        # Convert it from RGB to BGR (OpenCV format)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Write the frame
        out.write(frame)

        # Show the frame
        cv2.imshow("Screen Recorder", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) == ord('q'):
            break
except KeyboardInterrupt:
    print("Recording stopped by user")

# Release the video writer object and close the windows
out.release()
cv2.destroyAllWindows()
