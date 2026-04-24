import numpy as np
import matplotlib.pyplot as plt




def cargar_experimentos():
    
    return {

        #Tabla 6 Ruta Simple
        "exp1": {
            "politica": "PPO", "ambiente": "real", "ruta": "simple",
            "ISE": 434.99, "IAE": 135.93, "ITSE": 6932.79, "ITAE": 2601.61,
            "tiempo_s": None, "pasos": None, "reward_medio": None
        },
        "exp2": {
            "politica": "PPO-Mask", "ambiente": "real", "ruta": "simple",
            "ISE": 362.85, "IAE": 128.92, "ITSE": 5869.30, "ITAE": 2669.86,
            "tiempo_s": None, "pasos": None, "reward_medio": None
        },

        "exp3": {
            "politica": "PPO", "ambiente": "simulado", "ruta": "simple",
            "ISE": 73.35, "IAE": 24.51, "ITSE": 203.90 , "ITAE": 89.73,
            "tiempo_s": None, "pasos": None, "reward_medio": None
        },
        "exp4": {
            "politica": "PPO-Mask", "ambiente": "simulado", "ruta": "simple",
            "ISE": 73.79, "IAE": 22.91, "ITSE": 200.16, "ITAE": 73.77,
            "tiempo_s": None, "pasos": None, "reward_medio": None
        },



        #Tabla 7 Ruta Cuadrada
        "exp5": {
            "politica": "PPO", "ambiente": "simulado", "ruta": "cuadrada",
            "ISE": None, "IAE": None, "ITSE": None, "ITAE": None,
            "tiempo_s": 27.89, "pasos": 270, "reward_medio": 7.12
        },
        "exp6": {
            "politica": "PPO", "ambiente": "real", "ruta": "cuadrada",
            "ISE": None, "IAE": None, "ITSE": None, "ITAE": None,
            "tiempo_s": 112.48, "pasos": 594, "reward_medio": 3.75
        },
        "exp7": {
            "politica": "PPO-Mask", "ambiente": "simulado", "ruta": "cuadrada",
            "ISE": None, "IAE": None, "ITSE": None, "ITAE": None,
            "tiempo_s": 24.42, "pasos": 235, "reward_medio": 7.94
        },
        "exp8": {
            "politica": "PPO-Mask", "ambiente": "real", "ruta": "cuadrada",
            "ISE": None, "IAE": None, "ITSE": None, "ITAE": None,
            "tiempo_s": 103.46, "pasos": 569, "reward_medio": 4.13
        },


        #Tabla 8 Ruta Triangular
        "exp9": {
            "politica": "PPO", "ambiente": "simulado", "ruta": "triangular",
            "ISE": None, "IAE": None, "ITSE": None, "ITAE": None,
            "tiempo_s": 26.20, "pasos": 254, "reward_medio": 7.38
        },
        "exp10": {
            "politica": "PPO", "ambiente": "real", "ruta": "triangular",
            "ISE": None, "IAE": None, "ITSE": None, "ITAE": None,
            "tiempo_s": 104.37, "pasos": 581, "reward_medio": 3.92
        },
        "exp11": {
            "politica": "PPO-Mask", "ambiente": "simulado", "ruta": "triangular",
            "ISE": None, "IAE": None, "ITSE": None, "ITAE": None,
            "tiempo_s": 22.75, "pasos": 219, "reward_medio": 8.25
        },
        "exp12": {
            "politica": "PPO-Mask", "ambiente": "real", "ruta": "triangular",
            "ISE": None, "IAE": None, "ITSE": None, "ITAE": None,
            "tiempo_s": 116.71, "pasos": 638, "reward_medio": 4.45
        }
    }




def generar_trayectoria_ideal(waypoints, puntos_por_segmento=100):
    #Generar los vectores vacios
    x_ideal=[]
    y_ideal=[]


    #Iterar
    for i in range( len(waypoints) - 1):
        punto_actual = waypoints[i]
        punto_siguiente = waypoints[i+1]


        #Guardar eje X e Y
        ejex = np.linspace(punto_actual[0],punto_siguiente[0], puntos_por_segmento)
        ejey = np.linspace(punto_actual[1],punto_siguiente[1], puntos_por_segmento)

        x_ideal.extend(ejex)
        y_ideal.extend(ejey)

    return np.array(x_ideal), np.array(y_ideal)





def simular_lidar(n_sectores=36, d_min=0.5, d_max=30.0):

    #Crear angulos
    angulos_deg= np.linspace(0,360,n_sectores)
    
    #Generar distancia random
    distancias = np.random.uniform(d_min,d_max,n_sectores)

    #modificar indices
    distancias[5:9] = np.random.uniform(0.5, 2.0, size=4)

    #Normalizar 
    distancias_norm= (distancias-d_min)/(d_max-d_min)

    return angulos_deg, distancias, distancias_norm