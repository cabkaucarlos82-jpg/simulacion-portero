import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------
# Simulación de efectividad de un portero
# ---------------------------------------

# Configuración
num_partidos = 1000
tiros_por_partido = np.random.poisson(lam=10, size=num_partidos)   # Distribución Poisson
altura_zonas = 5   # resolución de matriz de calor
ancho_zonas = 8
heatmap = np.zeros((altura_zonas, ancho_zonas))

atajadas_totales = 0
tiros_totales = 0

# Probabilidades base según distancia
def probabilidad_gol(distancia):
    if distancia < 10:
        return 0.65   # muy cerca → más gol
    elif distancia < 20:
        return 0.40
    else:
        return 0.20   # muy lejos → menos gol

# Simulación Monte Carlo
for partido in range(num_partidos):

    tiros = tiros_por_partido[partido]

    for _ in range(tiros):
        tiros_totales += 1

        # Posición del tirador en el campo (eje x: ancho, eje y: largo)
        x = np.random.uniform(0, ancho_zonas)
        y = np.random.uniform(0, altura_zonas)

        # Distancia al arco simulada
        distancia = np.random.uniform(5, 30)

        # Probabilidad condicional de gol
        p_gol = probabilidad_gol(distancia)

        # Experimento Bernoulli
        gol = np.random.rand() < p_gol

        if not gol:
            atajadas_totales += 1

        # Guardar en la matriz de calor
        heatmap[int(y)][int(x)] += 1

# Porcentaje de atajadas
porcentaje_atajadas = (atajadas_totales / tiros_totales) * 100

print(f"Total de tiros: {tiros_totales}")
print(f"Atajadas del portero: {atajadas_totales}")
print(f"Porcentaje de atajadas: {porcentaje_atajadas:.2f}%")

# -------- MATRIZ DE CALOR --------
plt.figure(figsize=(8, 5))
plt.title("Mapa de calor de zonas de tiro")
plt.xlabel("Posición (Eje X)")
plt.ylabel("Distancia al arco (Eje Y)")
plt.imshow(heatmap, cmap='hot', interpolation='nearest')
plt.colorbar(label="Cantidad de tiros")
plt.show()
