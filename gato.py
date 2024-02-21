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

# Función principal del juego
def main():
    running = True
    draw_lines()
    pygame.display.update()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Aquí iría la lógica para manejar los clics y dibujar las marcas de los jugadores
        # También la comprobación para determinar el fin del juego

    pygame.quit()

if __name__ == '__main__':
    main()
