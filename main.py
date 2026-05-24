import random

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
    """
]

def jugar():
    palabras = [
        "cama", "perro", "gato", "auto", "casa", "arbol", "libro", "computadora", "teclado", "mouse",
        "pantalla", "cable", "disco", "memoria", "procesador", "placa", "fuente", "gabinete", "auricular", "parlante",
        "telefono", "celular", "reloj", "camara", "lampara", "silla", "mesa", "puerta", "ventana", "pared",
        "piso", "techo", "cocina", "baño", "dormitorio", "living", "patio", "garage", "jardin", "balcon",
        "calle", "avenida", "vereda", "plaza", "parque", "bosque", "selva", "desierto", "montaña", "playa",
        "oceano", "mar", "rio", "lago", "laguna", "arroyo", "cascada", "puente", "tunel", "estacion",
        "tren", "avion", "barco", "subte", "colectivo", "bicicleta", "moto", "camion", "camioneta", "grua",
        "cohete", "satelite", "planeta", "estrella", "galaxia", "universo", "espacio", "astronauta", "cometa", "asteroide",
        "sol", "luna", "tierra", "marte", "jupiter", "saturno", "urano", "neptuno", "pluton", "mercurio",
        "venus", "madera", "metal", "plastico", "vidrio", "papel", "carton", "cemento", "ladrillo", "piedra",
        "arena", "tierra", "agua", "fuego", "aire", "viento", "lluvia", "nieve", "granizo", "tormenta",
        "trueno", "relampago", "nube", "niebla", "humo", "ceniza", "carbon", "petroleo", "gas", "energia",
        "electricidad", "iman", "brujula", "mapa", "globo", "espejo", "reloj", "bruja", "mago", "duende",
        "fantasma", "monstruo", "dragon", "vampiro", "zombi", "esqueleto", "calavera", "tumba", "castillo", "palacio",
        "templo", "iglesia", "museo", "teatro", "cine", "estadio", "gimnasio", "escuela", "colegio", "universidad"
    ]

    #INICIALIZACION
    #elegir random
    palabra_adivinar = random.choice(palabras)

    letras_usadas = []
    
    intentos_iniciales= 6

    intentos_restantes = intentos_iniciales
    
    letras_palabra = list(palabra_adivinar)

    while intentos_restantes > 0:
        progreso = [letra if letra in letras_usadas else "_" for letra in palabra_adivinar]
    
        print(ESTADOS_AHORCADO[intentos_restantes])
        print(f"Palabra: {progreso}")
        print("Intentos restantes: ", intentos_restantes)
        print("Letras usadas:", letras_usadas)
        letra = input ("Arriesga una letra:")
        letra_usada = letra in letras_usadas
        if letra_usada:
            print("Ya usaste esa letra, arriesga otra")
        else:
            letra_pertenece = letra in letras_palabra
            if letra_pertenece:
                letras_usadas.append(letra)
                print(f"Muy bien! Acertaste la letra {letra}")
                verificar_ganador = all(letra in letras_usadas for letra in letras_palabra)
                if verificar_ganador:
                    print(f"Acertaste todas las letras! Ganaste :)")
                    final = [letra if letra in letras_usadas else "_" for letra in palabra_adivinar]
                    print(f"La palabra era: {final}")
                    exit()

            else:
                letras_usadas.append(letra)
                print(f"Fallaste, la letra {letra} no pertenece a la palabra")
                intentos_restantes = intentos_restantes - 1
            
    print("Perdiste x.x")
    print(f"La palabra era: {palabra_adivinar}")
    

print("Bienvenido, adivina la palabra secreta")
jugar()



