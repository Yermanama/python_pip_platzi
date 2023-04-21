import random #El módulo random proporciona funciones para la generación de números aleatorios
#y operaciones con ellos

def iniciar_juego():
    contador_usuario = 0
    contador_cpu = 0
    while contador_usuario <3 and contador_cpu <3:
        eleccion_usuario = elige_usuario()
        eleccion_cpu = elige_cpu()
        resultado = combate(eleccion_usuario, eleccion_cpu)
        contador_usuario, contador_cpu = actualizacion_marcador(contador_usuario, contador_cpu, resultado)

def elige_usuario():
    """
    Pide al usuario que elija una opción para el juego de piedra, papel, tijera.

    Returns:
    - eleccion_usuario (str): una cadena de texto que representa la elección del usuario.
    """
    posibles_opciones = ['piedra', 'papel', 'tijera']
    eleccion_usuario = input('Selecciona tu arma: [Piedra, Papel o Tijera]').lower()
    if eleccion_usuario in posibles_opciones:
        print('\n Elegiste: ' + eleccion_usuario)
        return eleccion_usuario
    else:
        print('Elección no válida, introduce piedra, papel o tijera')
        return elige_usuario()

def elige_cpu():
    '''
    Esta función devuelve una opción aleatoria para la CPU.

    Returns:
    - eleccion_CPU (str) : una cadena de texto que representa la elección de la CPU
    '''
    posibles_opciones = ['piedra', 'papel', 'tijera']
    eleccion_cpu = random.choice(posibles_opciones)
    print('La cpu elige: ' + eleccion_cpu)
    return eleccion_cpu

def combate(eleccion_usuario, eleccion_cpu):
    resultados = {
        ('piedra', 'tijera'): 'Victoria para el usuario',
        ('papel', 'piedra'): 'Victoria para el usuario',
        ('tijera', 'papel'): 'Victoria para el usuario',
        ('tijera', 'piedra'): 'Victoria para la cpu',
        ('piedra', 'papel'): 'Victoria para la cpu',
        ('papel', 'tijera'): 'Victoria para la cpu',
        ('papel', 'papel'): 'Empate',
        ('tijera', 'tijera'): 'Empate',
        ('piedra', 'piedra'): 'Empate',
    }
    resultado = resultados.get((eleccion_usuario, eleccion_cpu))
    print(resultado)
    return resultado

def actualizacion_marcador(contador_usuario, contador_cpu, resultado):
    if resultado == 'Victoria para el usuario':
        contador_usuario += 1
    elif resultado == 'Victoria para la cpu':
        contador_cpu += 1
    print('Marcador: Usuario: ' + str(contador_usuario) + ' CPU: ' + str(contador_cpu))
    return contador_usuario, contador_cpu

if __name__ == '__main__':
    iniciar_juego()