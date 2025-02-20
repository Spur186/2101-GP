"""
displacement.py
---------------
This module provides functions to keep coordinates within the defined workspace.
"""

# Define workspace boundaries (example values; adjust as needed)
X_MIN = 40.0
X_MAX = 200.0
Y_MIN = 40.0
Y_MAX = 215.0

def clamp_coordinate(x, y):
    """
    Clamp the coordinate (x, y) to the workspace boundaries.
    
    Args:
        x (float): The x-coordinate.
        y (float): The y-coordinate.
        
    Returns:
        tuple: (x, y) clamped within the workspace.
    """
    x_clamped = max(X_MIN, min(x, X_MAX))
    y_clamped = max(Y_MIN, min(y, Y_MAX))
    return x_clamped, y_clamped
