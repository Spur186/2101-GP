# displacement.py
# -----------------
# This module processes raw (x, y) coordinates.

# Define your working area boundaries (adjust these to your system)
X_MIN = 40
X_MAX = 200
Y_MIN = 40
Y_MAX = 215

def clamp_coordinate(x, y):
    """
    Clamp the input coordinates to the allowed working area.
    
    Args:
        x (float): Raw x-coordinate.
        y (float): Raw y-coordinate.
        
    Returns:
        tuple: (x, y) clamped within [X_MIN, X_MAX] and [Y_MIN, Y_MAX].
    """
    x_clamped = max(X_MIN, min(x, X_MAX))
    y_clamped = max(Y_MIN, min(y, Y_MAX))
    return x_clamped, y_clamped

def calculate_displacement(x, y):
    """
    Compute the displacement (distance from each edge) of the coordinate.
    
    Args:
        x (float): Raw x-coordinate.
        y (float): Raw y-coordinate.
        
    Returns:
        dict: Displacements from each edge.
    """
    x_clamped, y_clamped = clamp_coordinate(x, y)
    displacement = {
        'left': x_clamped,
        'top': y_clamped,
        'right': X_MAX - x_clamped,
        'bottom': Y_MAX - y_clamped
    }
    return displacement
