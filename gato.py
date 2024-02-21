#Descripcion: Juego del gato añadiendo un oponente con IA
#Autor: Dr. Aldo Gonzalez Vazquez
#Version: 1.0
#Fecha: 20/0272024
#Completar las siguientes funciones en el juego:
#Dibujar las líneas del tablero: Implementar la función draw_lines para dibujar las líneas del juego en la pantalla.
#Comprobar si un jugador ha ganado: Completar la función check_win para determinar si un jugador ha ganado el juego.
#Comprobar si el juego termina en empate: Implementar la función check_draw para verificar si todos los cuadros están marcados y no hay ganador, lo que resulta en un empate.
#Actualizar el estado del juego después de cada turno: Dibujar las marcas de los jugadores en el tablero y actualizar la interfaz gráfica para reflejar el estado actual del juego.
#Finalizar el juego y determinar el ganador o empate: Mostrar un mensaje cuando el juego termine, ya sea por un ganador o por un empate.

import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Constantes para el tamaño de la pantalla
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colores
BG_COLOR = (0, 255, 255)
LINE_COLOR = (0, 0, 0)
CIRCLE_COLOR = (255, 255, 0)
CROSS_COLOR = (255, 0, 0)

# Pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Juego del gato by Profe Aldo')
screen.fill(BG_COLOR)

# Tablero (3x3)
board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Dibujar las líneas del tablero
def draw_lines():
    # Horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Vertical
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def check_win(player):
    # Comprueba si el jugador ha ganado
    # Horizontal, vertical y diagonal
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def check_draw():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

def check_empty_squares():
    squares = []
    for y in range(BOARD_ROWS):
        for x in range(BOARD_COLS):
            if board[y][x] == 0:
                squares.append((y, x))
    return squares

def ai_move():
    empty_squares = check_empty_squares()
    if empty_squares:  # Si hay cuadrados vacíos
        row, col = random.choice(empty_squares)
        mark_square(row, col, 2)  # Asumiendo que la IA es el jugador 2
        if check_win(2):
            return True
        if check_draw():
            return True
    return False

# Función principal del juego
def main():
    running = True
    player_turn = 1 #Inicia el jugador humano
    draw_lines()
    pygame.display.update()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and player_turn == 1:
                mouseX = event.pos[0]  # Coordenada X del clic
                mouseY = event.pos[1]  # Coordenada Y del clic
                
                clicked_row = int(mouseY // SQUARE_SIZE)
                clicked_col = int(mouseX // SQUARE_SIZE)

                if board[clicked_row][clicked_col] == 0:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(1):
                        running = False
                    elif check_draw():
                        running = False
                    else:
                        player_turn = 2  # Cambia al turno de la IA
                    draw_figures()
                    pygame.display.update()
                        
        if player_turn == 2 and not running == False:
            if ai_move():
                running = False
            player_turn = 1
            draw_figures()
            pygame.display.update()

        
    pygame.quit()

if __name__ == '__main__':
    main()
