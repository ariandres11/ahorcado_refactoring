import random
from constantes import MENSAJES, ESTADOS_AHORCADO, INTENTOS_INICIALES
from palabras import obtener_palabras


class JuegoAhorcado:
    def __init__(self, palabras: list[str], intentos_iniciales: int):
        self.palabra_adivinar = random.choice(palabras)
        self.letras_usadas = []
        self.intentos_restantes = intentos_iniciales

    def verificar_letra_usada(self, letra: str) -> bool:
        return letra in self.letras_usadas

    def arriesgar_letra(self, letra: str) -> bool:
        self.letras_usadas.append(letra)
        if letra in self.palabra_adivinar:
            return True
        else:
            self.intentos_restantes -= 1
            return False

    def obtener_progreso(self) -> list[str]:
        return [
            letra if letra in self.letras_usadas else "_"
            for letra in self.palabra_adivinar
        ]

    def esta_ganado(self) -> bool:
        return all(letra in self.letras_usadas for letra in self.palabra_adivinar)

    def esta_perdido(self) -> bool:
        return self.intentos_restantes <= 0


def pedir_ingreso_letra() -> str:
    while True:
        letra = input(MENSAJES["pedir_letra"]).lower()
        if len(letra) == 1 and letra.isalpha():
            return letra
        print(MENSAJES["error_letra_invalida"])


def jugar_consola(intentos_iniciales: int):
    print(MENSAJES["bienvenida"])

    palabras = obtener_palabras()
    ahorcado = JuegoAhorcado(palabras, intentos_iniciales)

    while not ahorcado.esta_perdido() and not ahorcado.esta_ganado():
        progreso = ahorcado.obtener_progreso()

        print(ESTADOS_AHORCADO[ahorcado.intentos_restantes])
        print(f"Palabra: {' '.join(progreso)}")
        print(f"Letras usadas: {', '.join(ahorcado.letras_usadas)}")
        print(f"Intentos restantes: {ahorcado.intentos_restantes}")

        letra = pedir_ingreso_letra()

        if ahorcado.verificar_letra_usada(letra):
            print(MENSAJES["letra_repetida"].format(letra=letra))
        else:
            acerto = ahorcado.arriesgar_letra(letra)
            if acerto:
                print(MENSAJES["acierto"].format(letra=letra))
            else:
                print(MENSAJES["fallo"].format(letra=letra))

    if ahorcado.esta_ganado():
        print(MENSAJES["victoria"].format(palabra=ahorcado.palabra_adivinar))
    else:
        print(ESTADOS_AHORCADO[ahorcado.intentos_restantes])
        print(MENSAJES["derrota"].format(palabra=ahorcado.palabra_adivinar))


if __name__ == "__main__":
    jugar_consola(INTENTOS_INICIALES)
