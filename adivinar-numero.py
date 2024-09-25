import random


def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("Bienvenido al juego de adivinanza")
    print("debes adivinar un numero entre 1 y 100")
    print("Puedes Lograrlo")
    while not adivinado:
        adivinanza = input("introduce un numero del 1 al 100 :")

        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos += 1

            if 1 <= adivinanza <= 100:
                if adivinanza < numero_secreto:
                    print(f"el numero es mas grande que {adivinanza}")
                elif adivinanza > numero_secreto:
                    print(f"el numero es mas pequeño que {adivinanza}")
                else:
                    print(
                        f"Muy bien ganaste el numero era {adivinanza} hiciste {intentos} intentos"
                    )
                    play_again()
                    adivinado = True
            else:
                print("El numero debe ser entre 1 y 100")
        else:
            print("Pon un numero Cabeza de huevo")


def play_again():
    play = input("Quieres Jugar otra vez?(Y/N):")
    play = play.upper()
    if play == "Y":
        juego_adivinanza()
    elif play == "N":
        print("Hasta Luego")
    else:
        print("introduce una opcion valida")
        play_again()


juego_adivinanza()
