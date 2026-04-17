import numpy as np
import math

def pad_to_quantum_image(image_2d):
    height, width = image_2d.shape
    
    # Find next power of 2 for dimensions
    next_power_h = 2**math.ceil(math.log2(height))
    next_power_w = 2**math.ceil(math.log2(width))
    
    pad_bottom = next_power_h - height
    pad_right = next_power_w - width
    
    padded_image = np.pad(
        image_2d, 
        ((0, pad_bottom), (0, pad_right)), 
        mode='constant', 
        constant_values=0
    )
    return padded_image

def initialize_state_vector(total_pixels):
    # Every state starts with an amplitude of 1 / sqrt(total_pixels)
    amplitude = 1.0 / np.sqrt(total_pixels)
    
    # Create an 1D array
    state_vector = np.full(total_pixels, amplitude, dtype=complex)
    return state_vector