import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV con delimitador punto y coma
file_path = '/home/karla/pruebas-img/pruebas-sin-qos/prueba04/datos-grafico-pqts-perdidos-5s.csv'  # Ajusta la ruta según tu ubicación de archivo
data = pd.read_csv(file_path, delimiter=';')

# Extraer las columnas de datos para el gráfico
tiempo = data['tiempo ']
voip = data['voip']
vod = data['vod']
ftp = data['ftp']

# Configuración de estilo del gráfico
plt.style.use('ggplot')

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(10, 6), dpi=100, facecolor='white')

# Graficar los datos de cantidad de paquetes perdidos en función del tiempo para cada servicio
ax.plot(tiempo, voip, linestyle='-', color='#006400', markersize=5, linewidth=2, label='VoIP')  # Verde oscuro
ax.plot(tiempo, ftp, linestyle='-', color='#0a2351', markersize=5, linewidth=2, label='FTP')  # Azul oscuro
ax.plot(tiempo, vod, linestyle='-', color='#8B0000', markersize=5, linewidth=2, label='VOD')  # Rojo oscuro

# Título y etiquetas de los ejes
ax.set_title('Escenario 4: Cantidad de Paquetes Perdidos en Función del Tiempo', fontsize=14, weight='bold', color='black', pad=20, loc='center')
ax.set_xlabel('Tiempo [s]', fontsize=12, weight='bold', color='black', labelpad=15)
ax.set_ylabel('Paquetes Perdidos', fontsize=12, weight='bold', color='black', labelpad=15)

# Configuración de límites de los ejes
ax.set_xlim(min(tiempo), max(tiempo))
ax.set_ylim(0, max(max(voip), max(ftp), max(vod)) + 1)  # Un poco más alto que el valor máximo de paquetes perdidos

# Cuadrícula y personalización de los ejes
ax.grid(True, which='both', color='black', linestyle='--', linewidth=0.7)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#4d4d4d')
ax.spines['bottom'].set_color('#4d4d4d')
ax.tick_params(axis='both', which='major', labelsize=10, color='black')

# Marcas en el eje X
ax.set_xticks(range(0, max(tiempo) + 1, 20))  # Marcas en el eje X cada 60 segundos
ax.set_yticks(range(0, 8, 1))

# Añadir la leyenda
ax.legend(title='Servicios', fontsize=10, title_fontsize='12', loc='upper right')

# Ajustar el layout y mostrar el gráfico
plt.tight_layout()
plt.show()
