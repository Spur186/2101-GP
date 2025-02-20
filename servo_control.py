"""
servo_control.py
----------------
This module controls the wrist (pen-lift) servo.
"""

from machine import PWM, Pin

def translate(angle: float) -> int:
    """
    Convert an angle (in degrees) to a 16-bit PWM duty cycle.
    
    Args:
        angle (float): Angle in degrees.
    
    Returns:
        int: PWM duty cycle value.
    """
    if 0 <= angle <= 180:
        pwm_out = int((500 + 2000 * (angle / 180)) * 65535 / 20000)
    elif angle > 180:
        pwm_out = 8192
    else:
        pwm_out = 1638
    return pwm_out

def initialize_wrist():
    """
    Initialize the wrist (pen-lift) servo on Pin 2.
    
    Returns:
        PWM: The PWM object for the wrist servo.
    """
    wrist = PWM(Pin(2), freq=50)
    wrist.duty_u16(translate(0))  # Start with pen up (0°)
    return wrist

def set_wrist_position(wrist, position_angle):
    """
    Set the wrist servo to the desired position.
    
    Args:
        wrist: PWM object for the wrist servo.
        position_angle (float): Target angle (e.g., 0 for pen up, 30 for pen down).
    """
    wrist.duty_u16(translate(position_angle))
