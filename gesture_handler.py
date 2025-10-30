"""
Gesture Handler Module
Maps hand gestures to PowerPoint control actions
"""

import pyautogui
import time

class GestureHandler:
    def __init__(self):
        # Disable pyautogui failsafe for smooth operation
        pyautogui.FAILSAFE = False
        pyautogui.PAUSE = 0.1
        
        self.gesture_actions = {
            "next": self.next_slide,
            "previous": self.previous_slide,
            "palm": self.exit_presentation,
            "fist": self.pause_resume,
            "point": self.laser_pointer,
            "call": self.show_all_slides
        }
        
        print("Gesture Handler Initialized")
    
    def handle_gesture(self, gesture):
        """Execute action based on gesture"""
        if gesture in self.gesture_actions:
            action = self.gesture_actions[gesture]
            action()
            print(f"Executed: {gesture}")
        else:
            print(f"Unknown gesture: {gesture}")
    
    def next_slide(self):
        """Navigate to next slide"""
        pyautogui.press('right')
        print("➡️  Next Slide")
    
    def previous_slide(self):
        """Navigate to previous slide"""
        pyautogui.press('left')
        print("⬅️  Previous Slide")
    
    def exit_presentation(self):
        """Exit presentation mode"""
        pyautogui.press('esc')
        print("🚪 Exit Presentation")
    
    def pause_resume(self):
        """Pause/resume presentation"""
        pyautogui.press('b')  # 'B' key toggles black screen in PowerPoint
        print("⏸️  Pause/Resume")
    
    def laser_pointer(self):
        """Activate laser pointer (Ctrl+L in PowerPoint)"""
        pyautogui.hotkey('ctrl', 'l')
        print("🔴 Laser Pointer")
    
    def show_all_slides(self):
        """Show all slides view"""
        pyautogui.hotkey('alt', 'tab')
        print("📊 Switch Window")
    
    def start_presentation(self):
        """Start presentation from beginning"""
        pyautogui.press('f5')
        print("▶️  Start Presentation")
    
    def start_from_current(self):
        """Start presentation from current slide"""
        pyautogui.hotkey('shift', 'f5')
        print("▶️  Start from Current Slide")
