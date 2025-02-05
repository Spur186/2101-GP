# main.py
# -------
import time
from controller import get_2d_control_input, FIELD_WIDTH, FIELD_HEIGHT
from displacement import clamp_coordinate, calculate_displacement
from cable_control import initialize_motors, move_cables
from servo_control import initialize_wrist, set_wrist_position
from machine import Pin

# --- Smoothing Parameters ---
SMOOTH_THRESHOLD = 10  # Minimum change to bypass smoothing (in mm)
SMOOTH_AMOUNT = 7      # Maximum step when smoothing is active

# --- Button for Wrist (Pen) Control ---
button = Pin("GP22", Pin.IN)

def main():
    # Initialize cable motors (for X and Y movement)
    motor_x, motor_y = initialize_motors()
    
    # Initialize the wrist servo for pen up/down
    wrist = initialize_wrist()
    wrist_down = False  # False = pen up; True = pen down
    
    # Get an initial coordinate reading (starting at center)
    x_old, y_old = clamp_coordinate(FIELD_WIDTH / 2, FIELD_HEIGHT / 2)
    
    try:
        while True:
            # 1. Get the target coordinate from the 2D control device.
            raw_x, raw_y = get_2d_control_input()
            
            # 2. Clamp/process the coordinate into the allowed working area.
            x, y = clamp_coordinate(raw_x, raw_y)
            disp = calculate_displacement(raw_x, raw_y)
            print(f"Raw Input: ({raw_x:.1f}, {raw_y:.1f}) --> Clamped: ({x:.1f}, {y:.1f})")
            print("Displacement:", disp)
            
            # 3. Smooth out any large jumps.
            if abs(x - x_old) > SMOOTH_THRESHOLD:
                x = x_old + SMOOTH_AMOUNT if x > x_old else x_old - SMOOTH_AMOUNT
                time.sleep_ms(20)
            if abs(y - y_old) > SMOOTH_THRESHOLD:
                y = y_old + SMOOTH_AMOUNT if y > y_old else y_old - SMOOTH_AMOUNT
                time.sleep_ms(20)
            x_old, y_old = x, y
            
            # 4. Command the cable motors directly with the target (x, y) coordinate.
            move_cables(x, y, motor_x, motor_y)
            time.sleep_ms(20)
            
            # 5. Check the button to toggle the wrist (pen up/down).
            if button.value() == 1:
                # Wait for the button to be released.
                while button.value() == 1:
                    time.sleep_ms(10)
                if wrist_down:
                    set_wrist_position(wrist, 0)  # Pen UP
                    wrist_down = False
                    print("Wrist toggled: Pen UP")
                else:
                    set_wrist_position(wrist, 30)  # Pen DOWN
                    wrist_down = True
                    print("Wrist toggled: Pen DOWN")
                    
    finally:
        motor_x.deinit()
        motor_y.deinit()
        wrist.deinit()
        print("Motors deinitialized.")

if __name__ == "__main__":
    main()
