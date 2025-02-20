"""
displacement.py
---------------
This module provides functions to ensure that coordinates remain within a defined workspace.
"""

# Workspace boundaries
X_MIN = 40.0
X_MAX = 200.0
Y_MIN = 40.0
Y_MAX = 215.0

def clamp_coordinate(x, y):
    """
    Clamp the coordinate (x, y) within the workspace boundaries.
    
    Args:
        x (float): The x-coordinate.
        y (float): The y-coordinate.
        
    Returns:
        tuple: (x, y) clamped within [X_MIN, X_MAX] and [Y_MIN, Y_MAX].
    """
    x_clamped = max(X_MIN, min(x, X_MAX))
    y_clamped = max(Y_MIN, min(y, Y_MAX))
    return x_clamped, y_clamped
