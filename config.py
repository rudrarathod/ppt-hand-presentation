"""
Configuration Settings
Customize these settings for your setup
"""

# Camera Settings
CAMERA_INDEX = 0  # Default camera (0 for built-in webcam)
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# Hand Detection Settings
DETECTION_CONFIDENCE = 0.7  # Confidence threshold for hand detection (0.0 - 1.0)
TRACKING_CONFIDENCE = 0.5   # Confidence threshold for hand tracking (0.0 - 1.0)

# Gesture Recognition Settings
GESTURE_BUFFER_SIZE = 10    # Number of frames to buffer for gesture smoothing
GESTURE_THRESHOLD = 7       # Minimum count in buffer to recognize gesture
GESTURE_COOLDOWN = 1.5      # Seconds between gesture actions

# Display Settings
SHOW_FPS = True
WINDOW_NAME = "Hand Gesture Controller"

# Debug Mode
DEBUG = False  # Set to True for verbose logging
