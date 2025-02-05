# controller.py
# -------------
# This module simulates a 2D control input.
# Replace the input() calls with your actual hardware interface as needed.

# Define the overall dimensions of the control field (e.g., in mm)
FIELD_WIDTH = 220   # Maximum X value
FIELD_HEIGHT = 280  # Maximum Y value

def get_2d_control_input():
    """
    Retrieve a 2D coordinate from the control device.
    
    Returns:
        tuple: (x, y) coordinate.
    """
    try:
        x = float(input(f"Enter target X (0 to {FIELD_WIDTH}): "))
        y = float(input(f"Enter target Y (0 to {FIELD_HEIGHT}): "))
    except ValueError:
        print("Invalid input. Using center coordinates.")
        x = FIELD_WIDTH / 2
        y = FIELD_HEIGHT / 2
    return x, y
