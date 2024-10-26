
def choose_options():
    jugador_1 = str(input('''Jugador 1 Escoge que quieres sacar:
        - Piedra
        - Papel
        - Tijera:
                    ''')).lower()
    jugador_2 = str(input('''Jugador 2 Escoge que quieres sacar:
        - Piedra
        - Papel
        - Tijera:
                    ''')).lower()
    return jugador_1, jugador_2


def check_rules(jugador_1, jugador_2, posibles_valores):
    if jugador_1.lower() in posibles_valores:
        if jugador_2.lower() in posibles_valores:
            if jugador_1 == posibles_valores[0] and jugador_2 == posibles_valores[2]:
                result = "Piedra aplasta tijera. ¡¡¡El ganador es el jugador 1!!!"
            elif jugador_1 == posibles_valores[0] and jugador_2 == posibles_valores[1]:
                result = "Papel envuelve a Piedra. ¡¡¡El ganador es el jugador 2!!!"
            elif jugador_1 == posibles_valores[1] and jugador_2 == posibles_valores[2]:
                result = "Tijera corta papel. ¡¡¡El ganador es jugador 2!!!"
            elif jugador_1 == posibles_valores[2] and jugador_2 == posibles_valores[2]:
                result = "Ambos sacaron Tijera. ¡¡¡Es un empate vuelvan a jugar!!!"
            elif jugador_1 == posibles_valores[1] and jugador_2 == posibles_valores[1]:
                result = "Ambos sacaron Papel. ¡¡¡Es un empate vuelvan a jugar!!!"
            elif jugador_1 == posibles_valores[0] and jugador_2 == posibles_valores[0]:
                result = "Ambos sacaron Piedra. ¡¡¡Es un empate vuelvan a jugar!!!"
            elif jugador_2 == posibles_valores[0] and jugador_1 == posibles_valores[2]:
                result = "Piedra aplasta tijera. ¡¡¡El ganador es el jugador 2!!!"
            elif jugador_2 == posibles_valores[0] and jugador_1 == posibles_valores[1]:
                result = "Papel envuelve a Piedra. ¡¡¡El ganador es el jugador 1!!!"
            elif jugador_2 == posibles_valores[1] and jugador_1 == posibles_valores[2]:
                result = "Tijera corta papel. ¡¡¡El ganador es jugador 1!!!"
        else:
            result = "Jugador 2 selecciona una de las opciones mostradas o escribela correctamente"
    else:
            result = "Jugador 1 selecciona una de las opciones mostradas o escribela correctamente"
    
    return result



if __name__ == '__main__':
    posibles_valores = ["piedra", "papel", "tijera"]
    print("Bienvenido al peidra papel y tijera")
    jugador_1, jugador_2 = choose_options()
    result = check_rules(jugador_1, jugador_2, posibles_valores)
    print(result)

    