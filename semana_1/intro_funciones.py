import math as m

# introduccion a funciones

def celsius_a_fahrenheit(grados):
    # funcion que convierte un valor de grados celsius a fahrenheit
    return (grados * 9 / 5) + 32

def area_circulo(radio):
    # funcion que calcula el area de un circulo teniendo el valor de su radio
    return m.pi*radio**2

def promedio_lista(lista):
    # funcion que calcula el promedio de una lista, y devuelve un error en caso de que la lista este vacia
    if not lista:                                       # verifica que la lista no este vacia
        raise ValueError("La lista esta vacia") 
    return sum(lista) / len(lista)

def energia_cinetica(masa, velocidad):
    # funcion que calcula la energia cinetica teniendo los valores de su masa y velocidad
    return (masa / 2) * (velocidad**2)
                         
def caida_libre(altura):
    """
    funcion que calcula la velocidad final de un objeto que cae desde una 
    altura, teniendo la altura desde la cual se lanza
    """
    gravedad = 9.81
    return m.sqrt(2*gravedad*altura)
