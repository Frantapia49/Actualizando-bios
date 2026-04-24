import numpy as np

def calcular_movimiento(x, y, theta, v, omega, dt=0.1):
    # Saturación de velocidades según Tabla 1 [cite: 592]
    v = np.clip(v, 0, 0.8)
    omega = np.clip(omega, -0.6, 0.6)
    
    # Modelo cinemático diferencial [cite: 589]
    x_nuevo = x + v * np.cos(theta) * dt
    y_nuevo = y + v * np.sin(theta) * dt
    theta_nuevo = theta + omega * dt
    return x_nuevo, y_nuevo, theta_nuevo 

def distancia_al_objetivo(x, y, x_meta, y_meta):
    return np.sqrt((x_meta - x)**2 + (y_meta - y)**2) 

def calcular_error_seguimiento(x_real, y_real, x_ideal, y_ideal):
    # Ajustar tamaño si difieren [cite: 599]
    n = min(len(x_real), len(x_ideal))
    return np.sqrt((x_real[:n] - x_ideal[:n])**2 + (y_real[:n] - y_ideal[:n])**2) 