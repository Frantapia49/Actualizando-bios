import matplotlib.pyplot as plt
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_FOLDER = os.path.join(BASE_DIR, "resultados_graficos")

# Parte a)
def plot_metricas(dic, ambiente, ruta):
    ise, iae, itse, itae, politicas = [], [], [], [], []

    for llave, datos in dic.items():
        if datos['ambiente'] == ambiente and datos['ruta'] == ruta:
            politicas.append(datos['politica'])
            ise.append(datos['ISE'])
            iae.append(datos['IAE'])
            itse.append(datos['ITSE'])
            itae.append(datos['ITAE'])
            print(f"Encontrado: {datos['politica']} para {ambiente} {ruta}")

    plt.figure(figsize=(18, 5))

    plt.subplot(1, 4, 1)
    plt.bar(politicas, ise)
    plt.title("ISE")
    plt.bar(politicas, ise, color=['blue', 'red'])

    plt.subplot(1, 4, 2)
    plt.bar(politicas, iae)
    plt.title("IAE")
    plt.bar(politicas, iae, color=['blue', 'red'])
    
    plt.subplot(1, 4, 3)
    plt.bar(politicas, itse)
    plt.title("ITSE")
    plt.bar(politicas, itse, color=['blue', 'red'])
    
    plt.subplot(1, 4, 4)
    plt.bar(politicas, itae)
    plt.title("ITAE")
    plt.bar(politicas, itae, color=['blue', 'red'])

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    save_path = os.path.join(OUTPUT_FOLDER, "mapa_metricas.png")

    plt.tight_layout()
    plt.savefig(save_path, dpi=300) 
    print(f"Archivo guardado en: {save_path}")
    plt.show()

# Parte b)
def plot_lidar(ang, dist, dist_norm):
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.scatter(ang, dist)
    plt.title("Vista Real")
    plt.grid()

    plt.subplot(1, 2, 2)
    plt.plot(ang, dist_norm)
    plt.title("Vista IA")
    plt.grid()

    plt.tight_layout()
    
    
    output_folder = "resultados_graficos"
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    save_path = os.path.join(OUTPUT_FOLDER, "mapa_lidar.png")

    
    plt.savefig(save_path, dpi=300) 
    print(f"Archivo guardado en: {save_path}")
    
    plt.show() 
    plt.close()
# Parte c)
def plot_trayectorias(x1, y1, x2, y2, waypoints, nombre):
    wp_x, wp_y = zip(*waypoints)
    #Profesor, use el waypoints para transponer matrices, al ejecutar el codigo me dio error. Busque una solucion con la IA y me dijo
    #que lo más eficiente era poner un waypoints para ahorrar espacio.
    
    
    plt.figure(figsize=(8, 8))
    plt.plot(x1, y1, label='PPO')
    plt.plot(x2, y2, label='PPO-Mask')
    plt.scatter(wp_x, wp_y, marker='s', label='Waypoints')
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    save_path = os.path.join(OUTPUT_FOLDER, f"trayectoria_{nombre}.png")
    plt.axis('equal')
    plt.title(nombre)
    plt.legend()
    plt.grid()
    plt.savefig(save_path, dpi=300)
    plt.show()
    plt.close()