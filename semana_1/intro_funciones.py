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

def main():
    print('Menu de funciones')
    print('1. Funcion para convertir celsius a fahrenheit')
    print('2. Función para calcular el area de un circulo')
    print('3. Función para calcular el promedio de una lista')
    print('4. Función para calcular energia cinetica')
    print('5. Función para calcular velocidad final de objeto en caida libre')

    # funciones para manejar ingreso de datos
    def input_int(mensaje):
        while True:
            try:
                valor = int(input(mensaje))
                return valor
            except ValueError:
                print('Por favor, ingrese un numero valido')

    def input_float(mensaje):
        while True:
            try:
                valor = float(input(mensaje))
                return valor
            except ValueError:
                print('Por favor, ingrese un numero valido')

    usr = input_int('Seleccione una opción: ')

    match usr:
        case 1: 
            celsius = input_float('Ingrese los grados en celsius: ')
            fahrenheit = celsius_a_fahrenheit(celsius)
            print(f'Los grados en fahrenheit son: {fahrenheit}')
        case 2:
            radio = input_float('Ingrese el valor del radio del circulo: ')
            area = area_circulo(radio)
            print(f'El area del circulo con radio de {radio} es de {area} cm cuadrados')
        case 3:
            lista = []
            n = input_int('Ingrese el numero de valores en la lista: ')
            for i in range(0, n):
                valor = input_float('Ingrese valor en la lista: ')
                lista.append(valor)
            promedio = promedio_lista(lista)
            print(f'El promedio de la lista es: {promedio}')
        case 4:
            masa = input_float('Ingrese el valor de la masa: ')
            velocidad = input_float('Ingrese el valor de la velocidad: ')
            energia = energia_cinetica(masa, velocidad)
            print(f'La energia cinetica es: {energia}')
        case 5:
            altura = input_float('Ingrese el valor de la altura: ')
            velocidad_final = caida_libre(altura)
            print(f'La velocidad final del objeto es: {velocidad_final}')
        case _:
            print('Opción no valida')

main()





    