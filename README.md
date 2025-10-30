# 🎯 PPT Hand Gesture Controller

Control your PowerPoint presentations using hand gestures! This project uses computer vision and machine learning to detect hand gestures through your webcam and map them to PowerPoint controls.

## ✨ Features

- **Real-time Hand Tracking**: Uses MediaPipe for accurate hand detection
- **Gesture Recognition**: Recognizes multiple hand gestures for different controls
- **Smooth Operation**: Built-in gesture smoothing to avoid false triggers
- **Easy to Use**: Simple setup and intuitive controls
- **Customizable**: Configurable settings for different environments

## 🎮 Supported Gestures

| Gesture | Fingers | Action |
|---------|---------|--------|
| ✌️ Two Fingers | Index + Middle | Next Slide |
| 🤟 Three Fingers | Index + Middle + Ring | Previous Slide |
| 🖐️ Palm | All 5 Fingers | Exit Presentation |
| 👊 Fist | Closed Fist | Pause/Black Screen |
| 👆 Point | Index Only | Laser Pointer |
| 🤙 Call Sign | Thumb + Pinky | Switch Window |

## 📋 Requirements

- Python 3.8 or higher
- Webcam
- Windows/macOS/Linux
- PowerPoint installed

## 🚀 Installation

1. **Clone or download this project**

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation**:
   ```bash
   python -c "import cv2, mediapipe, pyautogui; print('All packages installed successfully!')"
   ```

## 🎯 Usage

1. **Open your PowerPoint presentation** and start the slideshow (F5)

2. **Run the controller**:
   ```bash
   python main.py
   ```

3. **Position yourself**:
   - Sit in front of your webcam
   - Ensure good lighting
   - Keep your hand visible in the frame

4. **Use gestures** to control your presentation!

5. **Press 'q'** to quit the application

## ⚙️ Configuration

Edit `config.py` to customize settings:

```python
# Camera Settings
CAMERA_INDEX = 0  # Change if you have multiple cameras
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# Detection Settings
DETECTION_CONFIDENCE = 0.7  # Increase for stricter detection
TRACKING_CONFIDENCE = 0.5

# Gesture Settings
GESTURE_COOLDOWN = 1.5  # Seconds between actions
```

## 🎓 Tips for Best Performance

1. **Lighting**: Ensure good, even lighting on your hand
2. **Background**: Use a plain background for better detection
3. **Distance**: Keep your hand 1-2 feet from the camera
4. **Clarity**: Make gestures clear and hold for 1-2 seconds
5. **Practice**: Try gestures before your presentation

## 🛠️ Troubleshooting

### Camera not detected
- Check if another application is using the webcam
- Try changing `CAMERA_INDEX` in `config.py`

### Gestures not recognized
- Improve lighting conditions
- Increase `DETECTION_CONFIDENCE` in `config.py`
- Ensure your entire hand is visible in the frame

### Actions trigger too quickly
- Increase `GESTURE_COOLDOWN` in `config.py`
- Increase `GESTURE_THRESHOLD` for stricter recognition

### PowerPoint not responding
- Make sure PowerPoint is the active window
- Try running as administrator (Windows)
- Check if keyboard shortcuts are enabled in PowerPoint

## 📝 File Structure

```
ppt-hand-presentation/
├── main.py              # Main application script
├── gesture_handler.py   # Gesture-to-action mapping
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🔧 Advanced Customization

### Adding New Gestures

1. **Define gesture detection** in `main.py`:
   ```python
   def detect_gesture(self, hand_landmarks):
       # Add your custom gesture logic
       if your_condition:
           return "custom_gesture"
   ```

2. **Map to action** in `gesture_handler.py`:
   ```python
   def custom_action(self):
       # Define what happens
       pyautogui.press('space')
   ```

3. **Register in gesture_actions dict**:
   ```python
   self.gesture_actions = {
       "custom_gesture": self.custom_action,
       # ... other gestures
   }
   ```

## 🤝 Contributing

Feel free to fork this project and add your own features! Some ideas:
- Voice commands
- Multi-hand gestures
- Gesture recording/playback
- Support for other presentation software

## 📄 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

- **MediaPipe** by Google for hand tracking
- **OpenCV** for computer vision
- **PyAutoGUI** for system control

## 📧 Support

If you encounter issues:
1. Check the troubleshooting section
2. Ensure all dependencies are installed correctly
3. Verify your webcam is working
4. Try adjusting settings in `config.py`

---

**Happy Presenting! 🎉**

Made with ❤️ for seamless presentations
