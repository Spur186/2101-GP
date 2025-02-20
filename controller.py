"""
controller.py
--------------
This module handles reading a single PWM signal from the joystick and converting
that signal into an angle. For simulation purposes, it prompts the user to enter a PWM value.
In a real system, replace the input() calls with your hardware’s ADC/PWM reading.
"""

PWM_MIN = 1000  # Minimum expected PWM value from the joystick
PWM_MAX = 2000  # Maximum expected PWM value from the joystick

def get_pwm_input():
    """
    Retrieve the PWM signal from the joystick.
    
    Returns:
        int: The PWM value.
    """
    try:
        pwm_value = int(input(f"Enter PWM value from joystick ({PWM_MIN} to {PWM_MAX}): "))
    except ValueError:
        print("Invalid input. Using mid-range value.")
        pwm_value = (PWM_MIN + PWM_MAX) // 2
    return pwm_value

def pwm_to_angle(pwm_value, min_pwm=PWM_MIN, max_pwm=PWM_MAX, min_angle=0.0, max_angle=360.0):
    """
    Convert a PWM value to an angle using linear interpolation.
    
    Args:
        pwm_value (int): The PWM signal value.
        min_pwm (int): Minimum PWM value.
        max_pwm (int): Maximum PWM value.
        min_angle (float): Minimum angle (in degrees).
        max_angle (float): Maximum angle (in degrees).
        
    Returns:
        float: The calculated angle in degrees.
    """
    # Clamp the pwm_value to the expected range.
    if pwm_value < min_pwm:
        pwm_value = min_pwm
    elif pwm_value > max_pwm:
        pwm_value = max_pwm

    
    angle = min_angle + (pwm_value - min_pwm) * (max_angle - min_angle) / (max_pwm - min_pwm)
    return angle
