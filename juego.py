import random #El módulo random proporciona funciones para la generación de números aleatorios
#y operaciones con ellos



def elige_usuario():
    """
    Pide al usuario que elija una opción para el juego de piedra, papel, tijera.

    Returns:
    - eleccion_usuario (str): una cadena de texto que representa la elección del usuario.
    """
    posibles_opciones = ['piedra', 'papel', 'tijera']
    eleccion_usuario = input('Selecciona tu arma: [Piedra, Papel o Tijera]').lower()
    if eleccion_usuario in posibles_opciones:
        pass
    else:
        print('Elección no válida, introduce piedra, papel o tijera')
        elige_usuario()
    return eleccion_usuario

def elige_cpu():
    '''
    Esta función devuelve una opción aleatoria para la CPU.

    Returns:
    - eleccion_CPU (str) : una cadena de texto que representa la elección de la CPU
    '''
    numero_aleatorio = random.randint(1,3)
    if numero_aleatorio == 1:
        eleccion_cpu = 'piedra'
    elif numero_aleatorio == 2:
        eleccion_cpu = 'papel'
    else:
        eleccion_cpu = 'tijera'
    return eleccion_cpu

def combate(eleccion_usuario, eleccion_cpu):
    