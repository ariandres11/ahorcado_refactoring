import random
from typing import Final

INTENTOS_INICIALES: Final[int] = 6

ESTADOS_AHORCADO = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,
]


def jugar():
    palabras = obtener_palabras()

    palabra_adivinar = elegir_palabra_aleatoria(palabras)

    letras_usadas = []
    intentos_restantes = INTENTOS_INICIALES

    letras_palabra = list(palabra_adivinar)

    while intentos_restantes > 0:
        mostrar_progreso(palabra_adivinar, letras_usadas, intentos_restantes)

        letra = pedir_ingreso_letra()

        if verificar_letra_usada(letra, letras_usadas):
            print(f"Ya usaste la letra '{letra}', arriesga otra.")
        else:
            letras_usadas.append(letra)

            if letra in letras_palabra:
                print(f"Muy bien! Acertaste la letra {letra}")
                verificar_ganador = all(l in letras_usadas for l in letras_palabra)
                if verificar_ganador:
                    mensaje_ganador(palabra_adivinar)
                    return
            else:
                print(f"Lo siento, la letra {letra} no está en la palabra.")
                intentos_restantes -= 1

    mensaje_perdedor(palabra_adivinar)


def mensaje_perdedor(palabra_adivinar: str):
    print(ESTADOS_AHORCADO[0])
    print("Perdiste x.x")
    print(f"La palabra era: {palabra_adivinar}")


def mensaje_ganador(palabra_adivinar: str):
    print(f"¡Felicidades! Adivinaste la palabra: {palabra_adivinar}")


def pedir_ingreso_letra() -> str:
    while True:
        letra = input("Arriesga una letra: ").lower()
        if len(letra) == 1 and letra.isalpha():
            return letra
        print("Debes ingresar una única letra válida. Intenta de nuevo.")


def verificar_letra_usada(letra: str, letras_usadas: list[str] = []) -> bool:
    return letra in letras_usadas


def mostrar_progreso(
    palabra_adivinar: str, letras_usadas: list[str], intentos_restantes: int
):
    progreso = [letra if letra in letras_usadas else "_" for letra in palabra_adivinar]

    print(ESTADOS_AHORCADO[intentos_restantes])
    print(f"Palabra: {progreso}")
    print("Intentos restantes: ", intentos_restantes)
    print("Letras usadas:", letras_usadas)


def obtener_palabras() -> list[str]:
    return [
        "cama",
        "perro",
        "gato",
        "auto",
        "casa",
        "arbol",
        "libro",
        "computadora",
        "teclado",
        "mouse",
        "pantalla",
        "cable",
        "disco",
        "memoria",
        "procesador",
        "placa",
        "fuente",
        "gabinete",
        "auricular",
        "parlante",
        "telefono",
        "celular",
        "reloj",
        "camara",
        "lampara",
        "silla",
        "mesa",
        "puerta",
        "ventana",
        "pared",
        "piso",
        "techo",
        "cocina",
        "baño",
        "dormitorio",
        "living",
        "patio",
        "garage",
        "jardin",
        "balcon",
        "calle",
        "avenida",
        "vereda",
        "plaza",
        "parque",
        "bosque",
        "selva",
        "desierto",
        "montaña",
        "playa",
        "oceano",
        "mar",
        "rio",
        "lago",
        "laguna",
        "arroyo",
        "cascada",
        "puente",
        "tunel",
        "estacion",
        "tren",
        "avion",
        "barco",
        "subte",
        "colectivo",
        "bicicleta",
        "moto",
        "camion",
        "camioneta",
        "grua",
        "cohete",
        "satelite",
        "planeta",
        "estrella",
        "galaxia",
        "universo",
        "espacio",
        "astronauta",
        "cometa",
        "asteroide",
        "sol",
        "luna",
        "tierra",
        "marte",
        "jupiter",
        "saturno",
        "urano",
        "neptuno",
        "pluton",
        "mercurio",
        "venus",
        "madera",
        "metal",
        "plastico",
        "vidrio",
        "papel",
        "carton",
        "cemento",
        "ladrillo",
        "piedra",
        "arena",
        "tierra",
        "agua",
        "fuego",
        "aire",
        "viento",
        "lluvia",
        "nieve",
        "granizo",
        "tormenta",
        "trueno",
        "relampago",
        "nube",
        "niebla",
        "humo",
        "ceniza",
        "carbon",
        "petroleo",
        "gas",
        "energia",
        "electricidad",
        "iman",
        "brujula",
        "mapa",
        "globo",
        "espejo",
        "reloj",
        "bruja",
        "mago",
        "duende",
        "fantasma",
        "monstruo",
        "dragon",
        "vampiro",
        "zombi",
        "esqueleto",
        "calavera",
        "tumba",
        "castillo",
        "palacio",
        "templo",
        "iglesia",
        "museo",
        "teatro",
        "cine",
        "estadio",
        "gimnasio",
        "escuela",
        "colegio",
        "universidad",
    ]


def elegir_palabra_aleatoria(palabras: list[str]) -> str:
    return random.choice(palabras)


print("Bienvenido, adivina la palabra secreta")
print("prueba")
jugar()
