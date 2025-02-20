"""
controller.py
--------------
This module reads a single PWM value from user input and converts that PWM value into an angle.
"""

PWM_MIN = 1000  # Minimum PWM value expected from the joystick
PWM_MAX = 2000  # Maximum PWM value expected from the joystick

def get_pwm_input():
    """
    Prompt the user for a PWM value.
    
    Returns:
        int: The PWM value entered.
    """
    try:
        pwm_value = int(input(f"Enter PWM value from joystick ({PWM_MIN} to {PWM_MAX}): "))
    except ValueError:
        print("Invalid input. Using mid-range value.")
        pwm_value = (PWM_MIN + PWM_MAX) // 2
    return pwm_value

def pwm_to_angle(pwm_value, min_pwm=PWM_MIN, max_pwm=PWM_MAX, min_angle=0.0, max_angle=360.0):
    """
    Convert a PWM value to an angle (in degrees) using linear interpolation.
    
    Args:
        pwm_value (int): The PWM signal value.
        min_pwm (int): Minimum PWM value.
        max_pwm (int): Maximum PWM value.
        min_angle (float): Minimum angle.
        max_angle (float): Maximum angle.
        
    Returns:
        float: The calculated angle in degrees.
    """
    # Clamp pwm_value to the range
    pwm_value = max(min_pwm, min(pwm_value, max_pwm))
    angle = min_angle + (pwm_value - min_pwm) * (max_angle - min_angle) / (max_pwm - min_pwm)
    return angle
