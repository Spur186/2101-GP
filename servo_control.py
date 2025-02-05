# servo_control.py
# ----------------
# This module handles servo initialization, PWM duty-cycle conversion,
# moving the servos, and controlling the wrist (pen up/down).

from machine import PWM, Pin

# --- Servo-to-PWM conversion ---
def translate(angle: float) -> int:
    """
    Convert an angle (in degrees) to the 16-bit PWM duty cycle.
    
    Uses a linear interpolation between minimum and maximum duty cycles.
    """
    if 0 <= angle <= 180:
        pwm_out = int((500 + 2000 * (angle / 180)) * 65535 / 20000)
    elif angle > 180:
        pwm_out = 8192  # default to near maximum if too big
    else:
        pwm_out = 1638  # default to near minimum if negative
    return pwm_out

# --- Servo Initialization ---
def initialize_servos():
    """
    Initialize the PWM channels for shoulder, elbow, and wrist servos.
    
    The pin assignments match your original code:
      - Shoulder: Pin 0
      - Elbow: Pin 1
      - Wrist: Pin 2
    """
    shoulder = PWM(Pin(0), freq=50)
    elbow = PWM(Pin(1), freq=50)
    wrist = PWM(Pin(2), freq=50)
    # Set initial angles (0 degrees for shoulder/elbow; wrist up = 0°)
    shoulder.duty_u16(translate(0))
    elbow.duty_u16(translate(0))
    wrist.duty_u16(translate(0))
    return shoulder, elbow, wrist

# --- Moving the Servos ---
def move_servos(shoulder_angle, elbow_angle, shoulder, elbow):
    """
    Convert the given angles to PWM duty cycles and send them to the servos.
    
    Returns:
        tuple: (shoulder_duty_cycle, elbow_duty_cycle)
    """
    shoulder_dc = translate(shoulder_angle)
    elbow_dc = translate(elbow_angle)
    shoulder.duty_u16(shoulder_dc)
    elbow.duty_u16(elbow_dc)
    return shoulder_dc, elbow_dc

# --- Wrist (Pen) Control ---
def set_wrist_position(wrist, position_angle):
    """
    Move the wrist servo to the given angle.
    (For example, 0 degrees = pen up; 30 degrees = pen down.)
    """
    wrist.duty_u16(translate(position_angle))

# Optionally, you could add a helper function to toggle the wrist state.
def toggle_wrist(wrist, current_state, up_angle=0, down_angle=30):
    """
    Toggle the wrist position.
    
    Args:
        wrist: The wrist servo PWM object.
        current_state (bool): True if currently down, False if up.
        up_angle (float): Angle for pen-up.
        down_angle (float): Angle for pen-down.
        
    Returns:
        bool: The new state (True if down, False if up).
    """
    if current_state:
        set_wrist_position(wrist, up_angle)
        return False
    else:
        set_wrist_position(wrist, down_angle)
        return True
