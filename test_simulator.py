"""
test_simulator.py
-----------------
This module simulates a test run of the cable-driven pen control system without hardware.
Instead of moving motors, the program reads a PWM value from the keyboard,
converts it to an angle, calculates a new coordinate based on a fixed step in that direction,
clamps the coordinate to the workspace, and then displays the desired coordinate along with
the calculated displacement from the current position.

All hardware-specific actions (e.g., motor movement, servo control) are replaced with print statements.
"""

import time
import math

# Import functions from the other modules
# (Ensure these modules are in the same directory or in your PYTHONPATH)
from controller import get_pwm_input, pwm_to_angle, PWM_MIN, PWM_MAX
from displacement import clamp_coordinate
from cable_control import update_coordinate
# from servo_control import initialize_wrist, set_wrist_position  # Not used in simulation

# --- Constants for Simulation ---
# Workspace boundaries (should match displacement.py values)
COORD_X_MIN = 40.0
COORD_X_MAX = 200.0
COORD_Y_MIN = 40.0
COORD_Y_MAX = 215.0

# Fixed step distance for each update (in the same unit as coordinates, e.g., mm)
STEP_SIZE = 5.0

def simulate_move(current_position, new_position):
    """
    Simulate the move by printing the desired new coordinates and the calculated displacement.
    
    Args:
        current_position (tuple): The current (x, y) coordinate.
        new_position (tuple): The new (x, y) coordinate.
    """
    displacement = (new_position[0] - current_position[0],
                    new_position[1] - current_position[1])
    print("\nSimulated Move:")
    print(f"  Current Position: {current_position}")
    print(f"  New Position:     {new_position}")
    print(f"  Displacement:     {displacement}\n")

def main():
    # For simulation, we don't initialize motors or a wrist servo.
    # Start the pen at the center of the workspace.
    current_position = ((COORD_X_MIN + COORD_X_MAX) / 2,
                        (COORD_Y_MIN + COORD_Y_MAX) / 2)
    
    print("=== Test Simulator ===")
    print("Enter CTRL+C to terminate the simulation.\n")
    print(f"Starting position: {current_position}\n")
    
    try:
        while True:
            # 1. Read the PWM signal from the joystick (simulated by keyboard input).
            pwm_value = get_pwm_input()
            
            # 2. Convert the PWM signal to a direction angle.
            angle = pwm_to_angle(pwm_value)
            print(f"Joystick angle (from PWM {pwm_value}): {angle:.2f}°")
            
            # 3. Calculate the new pen position based on current position, angle, and step size.
            new_position = update_coordinate(current_position, angle, STEP_SIZE)
            
            # 4. Clamp the new position to ensure it stays within the workspace.
            new_position = clamp_coordinate(new_position[0], new_position[1])
            print(f"Desired coordinates after clamping: {new_position}")
            
            # 5. Simulate moving the pen by printing the displacement.
            simulate_move(current_position, new_position)
            
            # Update the current position for the next iteration.
            current_position = new_position
            
            # Wait a short period before the next update.
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\nSimulation terminated.")

if __name__ == "__main__":
    main()
