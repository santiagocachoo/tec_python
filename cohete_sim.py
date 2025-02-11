import numpy as np
import matplotlib.pyplot as plt

# Parámetros iniciales
m_c = 0.175  # Masa del cohete vacío (kg)
m_a_t0 = 0.5  # Masa inicial de agua (kg)
g = 9.81  # Aceleración gravitacional (m/s²)
h = 0.0  # Altura inicial (m)
v = 0.0  # Velocidad inicial (m/s)
t = 0.0  # Tiempo inicial (s)
k = 0.9  # Coeficiente de resistencia (N·s/m)
dt = 0.1  # Paso de tiempo (s)

T = [t]
H = [h]
V = [v]
M = [m_c + m_a_t0]

def calcular_empuje(t):
    empuje = 10 - t**2
    return empuje if empuje > 0 else 0

def calcular_tasa_perdida(t):
    return 0.1

m_a = m_a_t0
while h >= 0:
    if m_a > 0:
        dot_m = calcular_tasa_perdida(t)
        m_a = max(m_a - dot_m * dt, 0)
    else:
        dot_m = 0

    m = m_c + m_a
    F_empuje = calcular_empuje(t)
    delta_v = (-g + F_empuje / m - k * v / m) * dt
    v += delta_v
    delta_h = v * dt
    h += delta_h
    t += dt

    T.append(t)
    H.append(h)
    V.append(v)
    M.append(m)

plt.figure(figsize=(18, 6))

plt.subplot(1, 3, 1)
plt.plot(T, V, label="Velocidad (m/s)", color="b")
plt.axhline(0, color="black", linestyle="--", linewidth=0.8)
plt.title("Velocidad vs Tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Velocidad (m/s)")
plt.legend()
plt.grid()

plt.subplot(1, 3, 2)
plt.plot(T, H, label="Altura (m)", color="g")
plt.axhline(0, color="black", linestyle="--", linewidth=0.8)
plt.title("Altura vs Tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Altura (m)")
plt.legend()
plt.grid()

plt.subplot(1, 3, 3)
plt.plot(T, M, label="Masa total (kg)", color="r")
plt.axhline(m_c, color="black", linestyle="--", linewidth=0.8, label="Masa del cohete vacío")
plt.title("Masa vs Tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Masa total (kg)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

print("hola")
