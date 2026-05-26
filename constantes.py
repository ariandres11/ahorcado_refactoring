from typing import Final

INTENTOS_INICIALES: Final[int] = 6

MENSAJES = {
    "bienvenida": "🎮 Bienvenido, adivina la palabra secreta 🎮",
    "pedir_letra": "Arriesga una letra: ",
    "error_letra_invalida": "⚠️ Debes ingresar una única letra válida. Intenta de nuevo.",
    "letra_repetida": "Ya usaste la letra '{letra}', arriesga otra.",
    "acierto": "¡Muy bien! Acertaste la letra '{letra}'",
    "fallo": "Lo siento, la letra '{letra}' no está en la palabra.",
    "victoria": "🏆 ¡Felicidades! Adivinaste la palabra: {palabra}",
    "derrota": "💀 Perdiste x.x La palabra era: {palabra}"
}

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
