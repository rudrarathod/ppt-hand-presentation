"""
PPT Hand Gesture Controller
Main script for controlling PowerPoint presentations using hand gestures
"""

import cv2
import mediapipe as mp
import pyautogui
import time
from collections import deque
from gesture_handler import GestureHandler
from config import *

class HandGestureController:
    def __init__(self):
        # Initialize MediaPipe Hand tracking
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=DETECTION_CONFIDENCE,
            min_tracking_confidence=TRACKING_CONFIDENCE
        )
        self.mp_draw = mp.solutions.drawing_utils
        
        # Initialize gesture handler
        self.gesture_handler = GestureHandler()
        
        # Initialize video capture
        self.cap = cv2.VideoCapture(CAMERA_INDEX)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)
        
        # Gesture smoothing
        self.gesture_buffer = deque(maxlen=GESTURE_BUFFER_SIZE)
        self.last_gesture_time = time.time()
        
        print("Hand Gesture Controller Initialized!")
        print("Press 'q' to quit")
        
    def count_fingers(self, hand_landmarks):
        """Count the number of extended fingers"""
        fingers = []
        
        # Thumb (special case - check horizontal distance)
        if hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].x < \
           hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_IP].x:
            fingers.append(1)
        else:
            fingers.append(0)
        
        # Other fingers
        finger_tips = [
            self.mp_hands.HandLandmark.INDEX_FINGER_TIP,
            self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
            self.mp_hands.HandLandmark.RING_FINGER_TIP,
            self.mp_hands.HandLandmark.PINKY_TIP
        ]
        
        finger_pips = [
            self.mp_hands.HandLandmark.INDEX_FINGER_PIP,
            self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP,
            self.mp_hands.HandLandmark.RING_FINGER_PIP,
            self.mp_hands.HandLandmark.PINKY_PIP
        ]
        
        for tip, pip in zip(finger_tips, finger_pips):
            if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
                fingers.append(1)
            else:
                fingers.append(0)
        
        return fingers
    
    def detect_gesture(self, hand_landmarks):
        """Detect specific hand gestures"""
        fingers = self.count_fingers(hand_landmarks)
        finger_count = sum(fingers)
        
        # Define gestures based on finger patterns
        if finger_count == 0:  # Fist
            return "fist"
        elif finger_count == 1 and fingers[1] == 1:  # Only index finger
            return "point"
        elif finger_count == 2 and fingers[1] == 1 and fingers[2] == 1:  # Index and middle
            return "next"
        elif finger_count == 3 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1:
            return "previous"
        elif finger_count == 5:  # All fingers extended
            return "palm"
        elif fingers[0] == 1 and fingers[4] == 1 and sum(fingers[1:4]) == 0:  # Thumb and pinky
            return "call"
        else:
            return "unknown"
    
    def smooth_gesture(self, gesture):
        """Smooth gestures to avoid false positives"""
        self.gesture_buffer.append(gesture)
        
        # Get most common gesture in buffer
        if len(self.gesture_buffer) >= GESTURE_BUFFER_SIZE:
            most_common = max(set(self.gesture_buffer), key=self.gesture_buffer.count)
            if self.gesture_buffer.count(most_common) >= GESTURE_THRESHOLD:
                return most_common
        
        return None
    
    def run(self):
        """Main loop"""
        print("\n=== Gesture Controls ===")
        print("✌️  Two Fingers (Index + Middle) - Next Slide")
        print("🤟 Three Fingers (Index + Middle + Ring) - Previous Slide")
        print("🖐️  Palm (All 5 Fingers) - Exit Presentation")
        print("👊 Fist - Pause/Resume")
        print("========================\n")
        
        current_gesture = None
        
        while True:
            success, frame = self.cap.read()
            if not success:
                print("Failed to capture frame")
                break
            
            # Flip frame horizontally for mirror effect
            frame = cv2.flip(frame, 1)
            
            # Convert to RGB for MediaPipe
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(rgb_frame)
            
            # Process hand landmarks
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Draw hand landmarks
                    self.mp_draw.draw_landmarks(
                        frame, 
                        hand_landmarks, 
                        self.mp_hands.HAND_CONNECTIONS
                    )
                    
                    # Detect gesture
                    gesture = self.detect_gesture(hand_landmarks)
                    smoothed_gesture = self.smooth_gesture(gesture)
                    
                    # Execute action if gesture is stable and cooldown passed
                    if smoothed_gesture and smoothed_gesture != current_gesture:
                        current_time = time.time()
                        if current_time - self.last_gesture_time >= GESTURE_COOLDOWN:
                            self.gesture_handler.handle_gesture(smoothed_gesture)
                            current_gesture = smoothed_gesture
                            self.last_gesture_time = current_time
                    
                    # Display current gesture
                    cv2.putText(
                        frame, 
                        f"Gesture: {gesture}", 
                        (10, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 
                        1, 
                        (0, 255, 0), 
                        2
                    )
            else:
                current_gesture = None
                cv2.putText(
                    frame, 
                    "No hand detected", 
                    (10, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    1, 
                    (0, 0, 255), 
                    2
                )
            
            # Display instructions
            cv2.putText(frame, "Press 'q' to quit", (10, frame.shape[0] - 10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            
            # Show frame
            cv2.imshow("Hand Gesture Controller", frame)
            
            # Check for quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        self.cleanup()
    
    def cleanup(self):
        """Clean up resources"""
        self.cap.release()
        cv2.destroyAllWindows()
        print("Controller stopped")

if __name__ == "__main__":
    try:
        controller = HandGestureController()
        controller.run()
    except KeyboardInterrupt:
        print("\nInterrupted by user")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
