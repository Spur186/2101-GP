import time
from controller import get_pwm_input, pwm_to_angle, PWM_MIN, PWM_MAX
from displacement import clamp_coordinate
from cable_control import update_coordinate, initialize_motors, move_cables
from servo_control import initialize_wrist, set_wrist_position
from machine import Pin

# Define workspace coordinate ranges (should match displacement.py values) 
COORD_X_MIN = 40.0
COORD_X_MAX = 200.0
COORD_Y_MIN = 40.0
COORD_Y_MAX = 215.0

# Define the fixed step distance (e.g., in mm) for each update.
STEP_SIZE = 5.0

# Button for wrist (pen-lift) control (assumed to be on "GP22") 
button = Pin("GP22", Pin.IN)
# Button for Stoping system
button2 = Pin("GP23", Pin.IN)

def main():
    # Initialize cable motors and wrist servo.
    motor_x, motor_y = initialize_motors()
    wrist = initialize_wrist()
    wrist_down = False  # Initial state: pen is up

    # Initialize current pen position (starting at the center of the workspace).
    current_position = ((COORD_X_MIN + COORD_X_MAX) / 2, (COORD_Y_MIN + COORD_Y_MAX) / 2)
    Stop = False
    try:
        while Stop == False:
            # 1. Read the PWM signal from the joystick.
            pwm_value = get_pwm_input()
            
            # 2. Convert the PWM signal to a direction angle.
            angle = pwm_to_angle(pwm_value)
            print(f"Joystick angle: {angle:.2f}°")
            
            # 3. Calculate the new pen position from the current position, angle, and step size.
            new_position = update_coordinate(current_position, angle, STEP_SIZE)
            
            # 4. Clamp the new position to ensure it stays within the workspace.
            new_position = clamp_coordinate(new_position[0], new_position[1])
            print(f"New position: {new_position}")
            
            # 5. Command the cable motors to move the pen to the new position.
            move_cables(new_position[0], new_position[1], motor_x, motor_y)
            
            # Update the current position.
            current_position = new_position
            
            # 6. Check the button to toggle the wrist (pen up/down).
            # ***NOT IMPLEMENTED YET***
            if button.value() == 1:
                # Wait for the button to be released.
                while button.value() == 1:
                    time.sleep_ms(10)
                if wrist_down:
                    set_wrist_position(wrist, 0)  # Pen up
                    wrist_down = False
                    print("Wrist toggled: Pen UP")
                else:
                    set_wrist_position(wrist, 30)  # Pen down (example angle)
                    wrist_down = True
                    print("Wrist toggled: Pen DOWN")
            
            time.sleep(0.1)  # Delay between updates.
            #
            if button2.value() == 1:
                Stop == True
    finally:
        # Deinitialize motors and wrist to safely shut down.
        motor_x.deinit()
        motor_y.deinit()
        wrist.deinit()
        print("Motors and wrist deinitialized.")

if __name__ == "__main__":
    main()
