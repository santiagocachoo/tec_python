import numpy as np
from scipy.optimize import curve_fit

# datos de la tabla
edad_siembra = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                         11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                         21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
volumen_total = np.array([0, 0.3, 2.3, 10.1, 24.6, 44.4, 67.7, 92.9, 
                          118.8, 145.6, 170, 194.3, 217.2, 240, 
                          260.1, 280, 299.9, 318.7, 334.8, 350.7, 
                          365.7, 380.1, 393.7, 406.6, 418.7, 430.4, 
                          441.6, 451.8, 461.7, 471.3])

# FORMULA 1 
# funcion
def funcion(t, a, b):
    return np.exp(a + (b / t))

# calcular valores de a y b
params, covariance = curve_fit(funcion, edad_siembra[1:], volumen_total[1:], p0=(1, 1))
a, b = params

print(f'Valor de a: {a}')
print(f'Valor de b: {b}')


# FORMULA 2 (polinomial de grado 4)
# calcular coeficientes de un polinomio de grado 4
coeficientes_polinomio = np.polyfit(edad_siembra, volumen_total, 4)
print ('Coeficientes del polinomio de grado 4:', coeficientes_polinomio)