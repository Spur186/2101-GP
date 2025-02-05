# cable_control.py
# ----------------
# This module converts a target (x, y) coordinate into motor commands
# for a cable-suspended pen system.

from machine import PWM, Pin

def translate_to_pwm(coordinate, min_coord, max_coord, min_pwm=1638, max_pwm=8192):
    """
    Convert a coordinate value into a PWM duty cycle via linear interpolation.
    
    Args:
        coordinate (float): The x or y coordinate.
        min_coord (float): The minimum possible coordinate.
        max_coord (float): The maximum possible coordinate.
        min_pwm (int): The PWM value corresponding to the minimum coordinate.
        max_pwm (int): The PWM value corresponding to the maximum coordinate.
    
    Returns:
        int: The calculated PWM duty cycle.
    """
    # Ensure coordinate is within the expected range
    coordinate = max(min_coord, min(coordinate, max_coord))
    duty_range = max_pwm - min_pwm
    coord_range = max_coord - min_coord
    pwm_val = int(min_pwm + (coordinate - min_coord) / coord_range * duty_range)
    return pwm_val

def initialize_motors():
    """
    Initialize the PWM-controlled motors for the cable system.
    
    Assumes:
      - Motor controlling horizontal movement is on Pin 0.
      - Motor controlling vertical movement is on Pin 1.
    """
    motor_x = PWM(Pin(0), freq=50)
    motor_y = PWM(Pin(1), freq=50)
    # Optionally set initial positions (here we start at the minimum coordinate)
    motor_x.duty_u16(translate_to_pwm(0, 0, 220))
    motor_y.duty_u16(translate_to_pwm(0, 0, 280))
    return motor_x, motor_y

def move_cables(x, y, motor_x, motor_y, x_min=0, x_max=220, y_min=0, y_max=280):
    """
    Convert the target (x, y) into PWM signals and command the motors.
    
    Args:
        x (float): Target x-coordinate.
        y (float): Target y-coordinate.
        motor_x: PWM object for horizontal movement.
        motor_y: PWM object for vertical movement.
    
    Returns:
        tuple: (pwm_x, pwm_y) the PWM values sent to each motor.
    """
    pwm_x = translate_to_pwm(x, x_min, x_max)
    pwm_y = translate_to_pwm(y, y_min, y_max)
    motor_x.duty_u16(pwm_x)
    motor_y.duty_u16(pwm_y)
    print(f"Moving cables: X PWM: {pwm_x}, Y PWM: {pwm_y}")
    return pwm_x, pwm_y
