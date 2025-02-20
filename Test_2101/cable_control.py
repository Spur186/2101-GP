"""
cable_control.py
----------------
This module calculates a new pen position based on the current position, a direction (angle), 
and a fixed step size.
"""

import math

def update_coordinate(current, angle, step):
    """
    Calculate a new (x, y) coordinate given the current coordinate, direction (angle), and step size.
    
    Args:
        current (tuple): Current (x, y) coordinate.
        angle (float): Direction angle in degrees.
        step (float): Step size (distance to move).
        
    Returns:
        tuple: New (x, y) coordinate.
    """
    radians = math.radians(angle)
    new_x = current[0] + step * math.cos(radians)
    new_y = current[1] + step * math.sin(radians)
    return new_x, new_y
