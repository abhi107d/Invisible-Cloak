# Webcam Magic Frame

This project captures a background image and then uses it to create a magic frame effect in real-time webcam feed, replacing certain colors with the captured background.

## Features

- Capture background frames.
- Replace specific colors in the webcam feed with the captured background.
- Real-time color range adjustment using trackbars.

## Requirements

- Python 3.x
- OpenCV
- NumPy

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/abhi107d/Invisible-Cloak.git
    cd Invisible-Cloak
    ```

2. Install the required libraries:
    ```sh
    pip install opencv-python numpy
    ```

## Usage

1. Run the script:
    ```sh
    python app.py
    ```

2. A window named "Trackbar" will appear with six trackbars for adjusting the HSV color range For eg green is (36,25,25) ~ (86, 255,255).

3. A window named "Magic Cam" will display the webcam feed.

4. Press 'r' to start capturing the background. Ensure the frame is clear of any foreground objects for a few seconds.

5. Adjust the trackbars to set the HSV range of colors you want to replace with the background.

6. Press 'q' to quit the application.

## Code Explanation

### Class: `WebcamCapture`

This class handles the webcam capture, background capture, and frame processing.

#### Methods:

- `__init__(self)`: Initializes the webcam, creates trackbars, and starts the main loop for capturing and processing frames.
- `captureBackground(self, frame)`: Captures background frames for a certain number of iterations.
- `getImg(self)`: Computes the average background image from captured frames.
- `magicFrame(self, frame)`: Processes each frame to replace specified colors with the background.
- `fun(self, val)`: A dummy callback function for trackbars.

### Constants

- `NOBC`: Number of background frames to capture (default: 60).

## Key Controls

- **r**: Start capturing the background.
- **q**: Quit the application.

## Notes

- Ensure your frame is clear of any foreground objects while capturing the background.
- Adjust the HSV range carefully to get the best results for the magic frame effect.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to contribute to this project by submitting issues or pull requests. Happy coding!
