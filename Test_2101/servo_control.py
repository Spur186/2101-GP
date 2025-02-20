"""
servo_control.py
----------------
This module simulates the pen-lift (wrist) servo control.
Since this is a test simulation, it only prints the intended action.
"""

def translate(angle):
    """
    Simulate the conversion of an angle to a PWM value.
    
    Args:
        angle (float): Angle in degrees.
        
    Returns:
        int: Simulated PWM value.
    """
    if 0 <= angle <= 180:
        pwm_value = int((500 + 2000 * (angle / 180)) * 65535 / 20000)
    elif angle > 180:
        pwm_value = 8192
    else:
        pwm_value = 1638
    return pwm_value

def simulate_servo_action(position_angle):
    """
    Simulate the servo action by displaying the target angle and its corresponding PWM value.
    
    Args:
        position_angle (float): The target servo angle.
    """
    pwm_value = translate(position_angle)
    print(f"Simulated servo: Setting pen-lift to {position_angle}° (PWM: {pwm_value})")
