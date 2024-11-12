import numpy as np

# Definir la función trapezoidal_integration
def trapecio_integracion(func, a, b, n):
    if a > b:
        raise ValueError("El limite inferior (a) debe ser menor o igual al limite suprerior (b)")
    
    # calcular el tamaño del subintervalo
    h = (b - a) / n

    # suma con los extremos
    suma = (func(a) + func(b)) / 2

    # suma los resultados de los puntos intermedios
    for i in range(1, n):
        suma += func(a + i * h)

    return h * suma

# Definir algunas funciones de prueba
def f_const(x):
    return 1

def f_linear(x):
    return x

def f_quadratic(x):
    return x**2

def f_complex(x):
    return np.sin(x)

def f_step(x):
    return 0 if x < 0.5 else 1

def f_oscillatory(x):
    return np.sin(20 * x)

# Parámetros de integración
a, b = 0, 1
n = 100000

# Prueba 1: Integral de una función constante
resultado_manual = trapecio_integracion(f_const, a, b, n)
assert abs(resultado_manual - 1) < 1e-5, f"Error en prueba constante: {resultado_manual} != 1"
print("Prueba 1 (constante) superada: resultado cercano a 1.")

# Prueba 2: Integral de una función lineal
resultado_manual = trapecio_integracion(f_linear, a, b, n)
assert abs(resultado_manual - 0.5) < 1e-5, f"Error en prueba lineal: {resultado_manual} != 0.5"
print("Prueba 2 (lineal) superada: resultado cercano a 0.5.")

# Prueba 3: Integral de una función cuadrática
resultado_manual = trapecio_integracion(f_quadratic, a, b, n)
assert abs(resultado_manual - 1/3) < 1e-5, f"Error en prueba cuadrática: {resultado_manual} != {1/3}"
print("Prueba 3 (cuadrática) superada: resultado cercano a 1/3.")

# Prueba 4: Comparación con numpy.trapz
x_vals = np.linspace(a, b, n + 1)
y_vals = f_complex(x_vals)
resultado_trapz = np.trapezoid(y_vals, x_vals)
resultado_manual = trapecio_integracion(f_complex, a, b, n)
assert abs(resultado_manual - resultado_trapz) < 1e-5, f"Error en comparación con numpy.trapz: {resultado_manual} != {resultado_trapz}"
print("Prueba 4 (comparación con numpy.trapz) superada: resultados coinciden.")

# Prueba 5: Integral de una función escalón
resultado_manual = trapecio_integracion(f_step, 0, 1, n)
assert abs(resultado_manual - 0.5) < 1e-5, f"Error en prueba escalón: {resultado_manual} != 0.5"
print("Prueba 5 (escalón) superada: resultado cercano a 0.5.")

# Prueba 6: Integral de una función oscilatoria
resultado_sinusoidal = trapecio_integracion(f_oscillatory, 0, np.pi, n)
assert abs(resultado_sinusoidal) < 1e-3, f"Error en prueba oscilatoria: {resultado_sinusoidal} no es cercano a 0"
print("Prueba 6 (oscilatoria) superada: resultado cercano a 0.")

# Prueba 7: Error al no ajustar delta_x correctamente (orden de límites invertido)
try:
    resultado_invalido = trapecio_integracion(f_const, 1, 0, n)  # a > b, orden invertido
    assert False, "Prueba 7 falló: No se lanzó excepción con límites invertidos."
except ValueError as e:
    print("Prueba 7 (orden de límites invertido) superada: excepción lanzada correctamente con mensaje:", e)

print("Todas las pruebas se han pasado correctamente.")

