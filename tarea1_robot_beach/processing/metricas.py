import numpy as np

def calcular_IAE(errores, dt):
    return np.sum(np.abs(errores)) * dt 

def calcular_ISE(errores, dt):
    return np.sum(errores**2) * dt 

def calcular_ITAE(errores, dt):
    t = np.arange(len(errores)) * dt 
    return np.sum(t * np.abs(errores)) * dt 

def calcular_ITSE(errores, dt):
    t = np.arange(len(errores)) * dt 
    return np.sum(t * (errores**2)) * dt 

def calcular_todas_las_metricas(errores, dt):
    res = {
        "ISE": round(calcular_ISE(errores, dt), 2),
        "IAE": round(calcular_IAE(errores, dt), 2),
        "ITSE": round(calcular_ITSE(errores, dt), 2),
        "ITAE": round(calcular_ITAE(errores, dt), 2)
    }
    return res 

def calcular_mejora(valor_ppo, valor_mask):
    return ((valor_ppo - valor_mask) / valor_ppo) * 100 