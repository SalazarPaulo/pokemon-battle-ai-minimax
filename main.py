import os
import random

class Pokemon:
    def __init__(self, nombre, vida, defensa, ataque, escudo):
        self.nombre = nombre
        self.vida = vida
        self.defensa = defensa
        self.ataque = ataque
        self.escudo = escudo

    def mostrar_estado(self):
        print(f"{self.nombre}:")
        print(f"Vida: {self.vida}")
        print(f"Defensa: {self.defensa}")
        print(f"Ataque: {self.ataque}")
        print(f"Escudo: {self.escudo}")

    def ataque_normal(self, oponente):
        dano = self.ataque - oponente.defensa
        if dano <= 0:
            dano = 1
        oponente.recibir_dano(dano)

    def curar(self):
        puntos_vida = random.randint(10, 20)
        self.vida += puntos_vida
        print(f"{self.nombre} se ha curado {puntos_vida} puntos de vida.")

    def mejorar_atributos(self):
        atributo = random.choice(['ataque', 'defensa'])
        incremento = random.randint(1, 5)
        if atributo == 'ataque':
            self.ataque += incremento
            print(f"{self.nombre} ha aumentado su atributo de ataque en {incremento}.")
        else:
            self.defensa += incremento
            print(f"{self.nombre} ha aumentado su atributo de defensa en {incremento}.")

    def habilidad_defensa(self):
        puntos_escudo = random.randint(5, 10)
        self.escudo += puntos_escudo
        print(f"{self.nombre} ha ganado {puntos_escudo} puntos de escudo.")

    def recibir_dano(self, dano):
        dano_efectivo = dano - self.escudo
        if dano_efectivo < 0:
            dano_efectivo = 0
        self.vida -= dano_efectivo
        self.escudo -= dano
        if self.vida < 0:
            self.vida = 0
        if self.escudo < 0:
            self.escudo = 0
        print(f"{self.nombre} ha recibido {dano_efectivo} puntos de daño.")

    def esta_vivo(self):
        return self.vida > 0


def seleccionar_habilidad():
    print("1. Ataque")
    print("2. Curar")
    print("3. Mejorar atributos")
    print("4. Defensa")
    opcion = input("Selecciona una habilidad: ")
    return opcion


def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def evaluar_estado(jugador1, jugador2, oponente1, oponente2):
    # jugador1_score = jugador1.vida + jugador1.defensa + jugador1.ataque
    # jugador2_score = jugador2.vida + jugador2.defensa + jugador2.ataque
    # oponente1_score = oponente1.vida + oponente1.defensa + oponente1.ataque
    # oponente2_score = oponente2.vida + oponente2.defensa + oponente2.ataque

    # return (jugador1_score + jugador2_score) - (oponente1_score + oponente2_score)
    #Segunda forma
  # Evalúe la salud de los jugadores.
  salud1 = jugador1.vida + jugador1.ataque
  salud2 = jugador2.vida + jugador2.ataque
    # salud1 = jugador1.vida 
    # salud2 = jugador2.vida 

  # Devuelva una puntuación basada en la salud de los jugadores.
  if salud1 > salud2:
    return 1
  elif salud1 < salud2:
    return -1
  else:
    return 0


def minmax(jugador1, jugador2, oponente1, oponente2, profundidad, maximizing_player):
    if profundidad == 0 or not (jugador1.esta_vivo() or jugador2.esta_vivo()) or not (oponente1.esta_vivo() or oponente2.esta_vivo()):
        return evaluar_estado(jugador1, jugador2, oponente1, oponente2)

    if maximizing_player:
        max_eval = float('-inf')
        habilidades = ['1', '2', '3', '4']
        for habilidad in habilidades:
            jugador1_copia = Pokemon(jugador1.nombre, jugador1.vida, jugador1.defensa, jugador1.ataque, jugador1.escudo)
            jugador2_copia = Pokemon(jugador2.nombre, jugador2.vida, jugador2.defensa, jugador2.ataque, jugador2.escudo)
            oponente1_copia = Pokemon(oponente1.nombre, oponente1.vida, oponente1.defensa, oponente1.ataque, oponente1.escudo)
            oponente2_copia = Pokemon(oponente2.nombre, oponente2.vida, oponente2.defensa, oponente2.ataque, oponente2.escudo)

            if jugador1.esta_vivo():
                realizar_jugada(jugador1_copia, oponente1_copia, habilidad)

            if jugador2.esta_vivo():
                realizar_jugada(jugador2_copia, oponente2_copia, habilidad)

            eval = minmax(jugador1_copia, jugador2_copia, oponente1_copia, oponente2_copia, profundidad - 1, False)
            max_eval = max(max_eval, eval)

        return max_eval
    else:
        min_eval = float('inf')
        habilidades = ['1', '2', '3', '4']
        for habilidad in habilidades:
            jugador1_copia = Pokemon(jugador1.nombre, jugador1.vida, jugador1.defensa, jugador1.ataque, jugador1.escudo)
            jugador2_copia = Pokemon(jugador2.nombre, jugador2.vida, jugador2.defensa, jugador2.ataque, jugador2.escudo)
            oponente1_copia = Pokemon(oponente1.nombre, oponente1.vida, oponente1.defensa, oponente1.ataque, oponente1.escudo)
            oponente2_copia = Pokemon(oponente2.nombre, oponente2.vida, oponente2.defensa, oponente2.ataque, oponente2.escudo)

            if oponente1.esta_vivo():
                realizar_jugada(oponente1_copia, jugador1_copia, habilidad)

            if oponente2.esta_vivo():
                realizar_jugada(oponente2_copia, jugador2_copia, habilidad)

            eval = minmax(jugador1_copia, jugador2_copia, oponente1_copia, oponente2_copia, profundidad - 1, True)
            min_eval = min(min_eval, eval)

        return min_eval


def minimax_alphabeta(jugador1, jugador2, oponente1, oponente2, profundidad, alpha, beta, maximizing_player):
    if profundidad == 0 or not (jugador1.esta_vivo() or jugador2.esta_vivo()) or not (oponente1.esta_vivo() or oponente2.esta_vivo()):
        return evaluar_estado(jugador1, jugador2, oponente1, oponente2)

    if maximizing_player:
        max_eval = float('-inf')
        habilidades = ['1', '2', '3', '4']
        for habilidad in habilidades:
            jugador1_copia = Pokemon(jugador1.nombre, jugador1.vida, jugador1.defensa, jugador1.ataque, jugador1.escudo)
            jugador2_copia = Pokemon(jugador2.nombre, jugador2.vida, jugador2.defensa, jugador2.ataque, jugador2.escudo)
            oponente1_copia = Pokemon(oponente1.nombre, oponente1.vida, oponente1.defensa, oponente1.ataque, oponente1.escudo)
            oponente2_copia = Pokemon(oponente2.nombre, oponente2.vida, oponente2.defensa, oponente2.ataque, oponente2.escudo)

            if jugador1.esta_vivo():
                realizar_jugada(jugador1_copia, oponente1_copia, habilidad)

            if jugador2.esta_vivo():
                realizar_jugada(jugador2_copia, oponente2_copia, habilidad)

            eval = minimax_alphabeta(jugador1_copia, jugador2_copia, oponente1_copia, oponente2_copia, profundidad - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break

        return max_eval
    else:
        min_eval = float('inf')
        habilidades = ['1', '2', '3', '4']
        for habilidad in habilidades:
            jugador1_copia = Pokemon(jugador1.nombre, jugador1.vida, jugador1.defensa, jugador1.ataque, jugador1.escudo)
            jugador2_copia = Pokemon(jugador2.nombre, jugador2.vida, jugador2.defensa, jugador2.ataque, jugador2.escudo)
            oponente1_copia = Pokemon(oponente1.nombre, oponente1.vida, oponente1.defensa, oponente1.ataque, oponente1.escudo)
            oponente2_copia = Pokemon(oponente2.nombre, oponente2.vida, oponente2.defensa, oponente2.ataque, oponente2.escudo)

            if oponente1.esta_vivo():
                realizar_jugada(oponente1_copia, jugador1_copia, habilidad)

            if oponente2.esta_vivo():
                realizar_jugada(oponente2_copia, jugador2_copia, habilidad)

            eval = minimax_alphabeta(jugador1_copia, jugador2_copia, oponente1_copia, oponente2_copia, profundidad - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break

        return min_eval


def realizar_jugada(jugador, oponente, habilidad):
    if habilidad == "1":  # Ataque
        jugador.ataque_normal(oponente)
    elif habilidad == "2":  # Curar
        jugador.curar()
    elif habilidad == "3":  # Mejorar atributos
        jugador.mejorar_atributos()
    elif habilidad == "4":  # Defensa
        jugador.habilidad_defensa()


def jugar():
    pikachu1 = Pokemon("Pikachu 1", 100, 5, 30, 0)
    pikachu2 = Pokemon("Pikachu 2", 100, 5, 30, 0)
    charmander1 = Pokemon("Charmander 1", 100, 5, 30, 0)
    charmander2 = Pokemon("Charmander 2", 100, 5, 30, 0)

    jugador1 = pikachu1
    jugador2 = pikachu2
    oponente1 = charmander1
    oponente2 = charmander2

    while jugador1.esta_vivo() and jugador2.esta_vivo() and oponente1.esta_vivo() and oponente2.esta_vivo():
        print("--- Turno del jugador ---")
        jugador1.mostrar_estado()
        jugador2.mostrar_estado()
        oponente1.mostrar_estado()
        oponente2.mostrar_estado()

        print("Jugador 1:")
        habilidad1 = seleccionar_habilidad()
        realizar_jugada(jugador1, oponente1, habilidad1)

        print("Jugador 2:")
        habilidad2 = seleccionar_habilidad()
        realizar_jugada(jugador2, oponente2, habilidad2)

        if not (oponente1.esta_vivo() or oponente2.esta_vivo()):
            break

        print("\n--- Turno del oponente ---")
        profundidad = 3
        alpha = float('-inf')
        beta = float('inf')
        mejor_puntuacion = float('-inf')
        mejor_habilidad_oponente = None

        habilidades_oponente = ['1', '2', '3', '4']
        for habilidad_oponente in habilidades_oponente:
            jugador1_copia = Pokemon(jugador1.nombre, jugador1.vida, jugador1.defensa, jugador1.ataque, jugador1.escudo)
            jugador2_copia = Pokemon(jugador2.nombre, jugador2.vida, jugador2.defensa, jugador2.ataque, jugador2.escudo)
            oponente1_copia = Pokemon(oponente1.nombre, oponente1.vida, oponente1.defensa, oponente1.ataque, oponente1.escudo)
            oponente2_copia = Pokemon(oponente2.nombre, oponente2.vida, oponente2.defensa, oponente2.ataque, oponente2.escudo)

            if oponente1.esta_vivo():
                realizar_jugada(oponente1_copia, jugador1_copia, habilidad_oponente)

            if oponente2.esta_vivo():
                realizar_jugada(oponente2_copia, jugador2_copia, habilidad_oponente)

            puntuacion = minmax(jugador1_copia, jugador2_copia, oponente1_copia, oponente2_copia, profundidad - 1, True)

            if puntuacion > mejor_puntuacion:
                mejor_puntuacion = puntuacion
                mejor_habilidad_oponente = habilidad_oponente

            if puntuacion >= beta:
                break

            if puntuacion > alpha:
                alpha = puntuacion
        print("Movimiento Pokemon 1:")
        realizar_jugada(oponente1, jugador1, mejor_habilidad_oponente)
        print("Movimiento Pokemon 2:")
        realizar_jugada(oponente2, jugador2, mejor_habilidad_oponente)

    if jugador1.esta_vivo() or jugador2.esta_vivo():
        print("¡El equipo del jugador ha ganado!")
    else:
        print("¡El equipo del oponente ha ganado!")


def jugar_Min():
    pikachu1 = Pokemon("Pikachu 1", 100, 5, 50, 0)
    pikachu2 = Pokemon("Pikachu 2", 100, 5, 50, 0)
    charmander1 = Pokemon("Charmander 1", 100, 5, 50, 0)
    charmander2 = Pokemon("Charmander 2", 100, 5, 50, 0)

    jugador1 = pikachu1
    jugador2 = pikachu2
    oponente1 = charmander1
    oponente2 = charmander2

    while jugador1.esta_vivo() and jugador2.esta_vivo() and oponente1.esta_vivo() and oponente2.esta_vivo():
        print("--- Turno del jugador ---")
        jugador1.mostrar_estado()
        jugador2.mostrar_estado()
        oponente1.mostrar_estado()
        oponente2.mostrar_estado()

        print("Jugador 1:")
        habilidad1 = seleccionar_habilidad()
        realizar_jugada(jugador1, oponente1, habilidad1)

        print("Jugador 2:")
        habilidad2 = seleccionar_habilidad()
        realizar_jugada(jugador2, oponente2, habilidad2)

        if not (oponente1.esta_vivo() or oponente2.esta_vivo()):
            break

        print("\n--- Turno del oponente ---")
        profundidad = 3
        alpha = float('-inf')
        beta = float('inf')
        mejor_puntuacion = float('-inf')
        mejor_habilidad_oponente = None

        habilidades_oponente = ['1', '2', '3', '4']
        for habilidad_oponente in habilidades_oponente:
            jugador1_copia = Pokemon(jugador1.nombre, jugador1.vida, jugador1.defensa, jugador1.ataque, jugador1.escudo)
            jugador2_copia = Pokemon(jugador2.nombre, jugador2.vida, jugador2.defensa, jugador2.ataque, jugador2.escudo)
            oponente1_copia = Pokemon(oponente1.nombre, oponente1.vida, oponente1.defensa, oponente1.ataque, oponente1.escudo)
            oponente2_copia = Pokemon(oponente2.nombre, oponente2.vida, oponente2.defensa, oponente2.ataque, oponente2.escudo)

            if oponente1.esta_vivo():
                realizar_jugada(oponente1_copia, jugador1_copia, habilidad_oponente)

            if oponente2.esta_vivo():
                realizar_jugada(oponente2_copia, jugador2_copia, habilidad_oponente)

            puntuacion = minimax_alphabeta(jugador1_copia, jugador2_copia, oponente1_copia, oponente2_copia, profundidad - 1, alpha, beta, True)

            if puntuacion > mejor_puntuacion:
                mejor_puntuacion = puntuacion
                mejor_habilidad_oponente = habilidad_oponente
        print("Movimiento Pokemon 1:")
        realizar_jugada(oponente1, jugador1, mejor_habilidad_oponente)
        print("Movimiento Pokemon 2:")
        realizar_jugada(oponente2, jugador2, mejor_habilidad_oponente)

    if jugador1.esta_vivo() or jugador2.esta_vivo():
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")


def Menu():
    print("1. Minimax")
    print("2. Minimax con poda alfa-beta")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        jugar_Min()
    elif opcion == "2":
        jugar()

Menu()
