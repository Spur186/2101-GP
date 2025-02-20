

import time
from controller import get_pwm_input, pwm_to_angle, PWM_MIN, PWM_MAX
from displacement import clamp_coordinate
from cable_control import update_coordinate
from servo_control import simulate_servo_action

# Workspace coordinate boundaries (should match displacement.py)
COORD_X_MIN = 40.0
COORD_X_MAX = 200.0
COORD_Y_MIN = 40.0
COORD_Y_MAX = 215.0


# Fixed step size for each update (for example, in millimeters)
STEP_SIZE = 5.0

def main():
    End = 1

    # Set starting position at the center of the workspace.
    current_position = ((COORD_X_MIN + COORD_X_MAX) / 2, (COORD_Y_MIN + COORD_Y_MAX) / 2)
    
    print("=== Simulation for Switch Adapted Art ===")
    print(f"Starting Position: {current_position}\n")
    #Main while loop keeps running unless user enters "n" at the end of the loop
    while End == 1:
        # 1. Read the PWM value from the user.
        pwm_value = get_pwm_input()
        
        # 2. Convert the PWM value to a direction angle.
        angle = pwm_to_angle(pwm_value)
        print(f"Converted PWM {pwm_value} to angle: {angle:.2f}°")
        
        # 3. Calculate the new coordinate based on current position, angle, and step size.
        new_position = update_coordinate(current_position, angle, STEP_SIZE)
        
        # 4. Clamp the new position to the workspace boundaries.
        new_position = clamp_coordinate(new_position[0], new_position[1])
        
        # 5. Calculate and display the displacement.
        displacement_x = new_position[0] - current_position[0]
        displacement_y = new_position[1] - current_position[1]
        print(f"New desired coordinate: {new_position}")
        print(f"Calculated displacement: (dx: {displacement_x:.2f}, dy: {displacement_y:.2f})")
        
        # 6. Simulate a servo (pen-lift) action (this is optional).
        simulate_servo_action(30)  # Example: simulate lowering the pen (30°)
        
        # 7. Update the current position.
        current_position = new_position
        Question = print ("Test Again?(y/n)")
        if Question =="n":
            End = 0
        else: End = 1

        
        print("\n--- Next Update ---\n")
        time.sleep(0.1)


if __name__ == "__main__":
    main()
