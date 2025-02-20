"""
cable_control.py
----------------
This module calculates a new pen position based on the current position,
a given direction (angle), and a fixed step size. It also handles sending commands
to the cable motors (using PWM) to move the pen.
"""

import math
from machine import PWM, Pin

def update_coordinate(current, angle, step):
    """
    Calculate a new (x, y) coordinate given the current position, a direction (angle),
    and a step distance.
    
    Args:
        current (tuple): Current (x, y) coordinate.
        angle (float): Direction angle in degrees.
        step (float): Distance to move in that direction.
        
    Returns:
        tuple: New (x, y) coordinate.
    """
    # Convert angle from degrees to radians for math.cos and math.sin.
    radians = math.radians(angle)
    new_x = current[0] + step * math.cos(radians)
    new_y = current[1] + step * math.sin(radians)
    return new_x, new_y

def initialize_motors():
    """
    Initialize the motors that control the cables.
    
    Assumes:
      - X-axis motor is on Pin 0.
      - Y-axis motor is on Pin 1.
    
    Returns:
        tuple: (motor_x, motor_y) as PWM objects.
    """
    motor_x = PWM(Pin(0), freq=50)
    motor_y = PWM(Pin(1), freq=50)
    # TODO: Optionally set initial positions or duty cycles for your motors.
    return motor_x, motor_y

def move_cables(x, y, motor_x, motor_y):
    """
    Command the cable motors to move the pen to the specified (x, y) coordinate.
    
    In a cable-driven system, you may need to convert the coordinate into the appropriate
    PWM commands for your motor drivers.
    
    Args:
        x (float): Target x-coordinate.
        y (float): Target y-coordinate.
        motor_x: PWM object for the X-axis motor.
        motor_y: PWM object for the Y-axis motor.
        
    Returns:
        tuple: (pwm_x, pwm_y) placeholder values sent to the motors.
    """
    # For now, we use a simple conversion (this is a placeholder).
    pwm_x = int(x)
    pwm_y = int(y)
    motor_x.duty_u16(pwm_x)
    motor_y.duty_u16(pwm_y)
    return pwm_x, pwm_y
