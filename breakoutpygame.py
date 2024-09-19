import pygame

pygame.init()

# Define colors
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_ORANGE = (255, 165, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_PADDLE = (30, 100, 200)

# screen size
WIDTH_SCREEN = 600
HEIGHT_SCREEN = 700

size = (WIDTH_SCREEN, HEIGHT_SCREEN)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout - PyGame Edition - 2024-09-17")

# level text
text_font = pygame.font.Font('assets/pong-score.ttf', 45)
level_text = text_font.render("1" , True, COLOR_WHITE)
level_text_rect = level_text.get_rect()
level_text_rect.center = (40, 50)

# try text
try_text = text_font.render("1" , True, COLOR_WHITE)
try_text_rect = try_text.get_rect()
try_text_rect.center = (350, 50)

# score text
score_font = pygame.font.Font('assets/pong-score.ttf', 50)
score_text = score_font.render('005', True, COLOR_WHITE)
score_text_rect = score_text.get_rect()
score_text_rect.center = (120,100)

# score 2 text
score_2_text = score_font.render('000', True, COLOR_WHITE)
score_2_text_rect = score_2_text.get_rect()
score_2_text_rect.center = (430,100)

# Text to start the game
start_font = pygame.font.Font('assets/PressStart2P.ttf', 15)
start_text = start_font.render("Press ANY KEY to start the game" , True, COLOR_WHITE)
start_text_rect = start_text.get_rect()
start_text_rect.center = (290, 550)

# player 1
player_1 = pygame.image.load("assets/player.png")
player_1_width = 50   # Width of the player
player_1_height = 15  # Height of the player
player_1_x = (WIDTH_SCREEN/2) - 25        # Initial x position
player_1_y = HEIGHT_SCREEN - 60   # y position near the bottom of the screen
player_1_move_right = False
player_1_move_left = False

# Create ball
ball = pygame.image.load("assets/ball.png")
ball_x = WIDTH_SCREEN/2 - 5
ball_y = HEIGHT_SCREEN - 70
ball_width = 10
ball_height = 10

# block variables
BLOCK_WALL_COLUMN = 14
BLOCK_WALL_ROWS = 8

# Create the wall of blocks
class BLOCKS:
    def __init__(self):
        self.width = (WIDTH_SCREEN - 12)//BLOCK_WALL_COLUMN
        self.height = 13

    def create_walls(self):
        self.block_wall = []

        for row in range(BLOCK_WALL_ROWS):
            # New block row list
            row_block = []
            for column in range(BLOCK_WALL_COLUMN):
                # x and y positions for each block
                block_x = column * self.width + 8
                block_y = row * self.height + 128
                # create a block
                rect = pygame.Rect(block_x, block_y, self.width, self.height)
                # append that rect to the block row
                row_block.append(rect)
            # append the row to the full list of blocks
            self.block_wall.append(row_block)

    def draw_walls(self):
        for i_row in range(BLOCK_WALL_ROWS):
            for block in self.block_wall[i_row]:
                # assign block color based on row
                if i_row == 0 or i_row == 1:
                    color_block = COLOR_RED
                elif i_row == 2 or i_row == 3:
                    color_block = COLOR_ORANGE
                elif i_row == 4 or i_row == 5:
                    color_block = COLOR_GREEN
                elif i_row == 6 or i_row == 7:
                    color_block = COLOR_YELLOW
                pygame.draw.rect(screen, color_block, block)
                pygame.draw.rect(screen, COLOR_BLACK, block, 2)

wall_block = BLOCKS()
wall_block.create_walls()

# game loop
game_loop = True
game_clock = pygame.time.Clock()
interval = True

while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        elif event.type == pygame.KEYDOWN:
            interval = False
            if event.key == pygame.K_LEFT:
                player_1_move_left = False
            if event.key == pygame.K_RIGHT:
                player_1_move_right = False
        elif event.type == pygame.KEYUP:
            interval = False
            if event.key == pygame.K_LEFT:
                player_1_move_left = True
            if event.key == pygame.K_RIGHT:
                player_1_move_right = True

    # player 1 right movement
    if player_1_move_right:
        player_1_x -= 5
    else:
        player_1_x += 0

    # player 1 left movement
    if player_1_move_left:
        player_1_x += 5
    else:
        player_1_x += 0

    # player 1 collides with wall
    if player_1_x <= 0:
        player_1_x = 0
    elif player_1_x >= WIDTH_SCREEN - player_1_width:
        player_1_x = WIDTH_SCREEN - player_1_width

    # Drawing objects
    screen.fill(COLOR_BLACK)


    def wall_colors(width):
        pygame.draw.rect(screen, COLOR_RED, (width, 130, 10, 25))
        pygame.draw.rect(screen, COLOR_ORANGE, (width, 155, 10, 25))
        pygame.draw.rect(screen, COLOR_GREEN, (width, 180, 10, 25))
        pygame.draw.rect(screen, COLOR_YELLOW, (width, 205, 10, 25))
        pygame.draw.rect(screen, COLOR_PADDLE, (width, HEIGHT_SCREEN - 67, 10, 30))

    # Draw block wall
    wall_block.draw_walls()
    # Draw white borders: top, left, and right
    pygame.draw.rect(screen, COLOR_WHITE, (0, 0, WIDTH_SCREEN, 25))  # Top border
    pygame.draw.rect(screen, COLOR_WHITE, (0, 0, 10, HEIGHT_SCREEN))  # Left border
    wall_colors(0) # Left border color
    pygame.draw.rect(screen, COLOR_WHITE, (WIDTH_SCREEN - 10, 0, 10, HEIGHT_SCREEN))  # Right border
    wall_colors(WIDTH_SCREEN - 10) # Left border color
    # Drawing texts
    screen.blit(level_text, level_text_rect)
    screen.blit(try_text, try_text_rect)
    screen.blit(score_text, score_text_rect)
    screen.blit(score_2_text, score_2_text_rect)
    # Draw ball
    pygame.draw.rect(screen, COLOR_WHITE, (ball_x, ball_y, ball_width, ball_height))

    if interval:
        # Draw start line
        start_line = pygame.draw.rect(screen, COLOR_PADDLE, (0, HEIGHT_SCREEN - 60, WIDTH_SCREEN, 15))  # Top border
        screen.blit(start_text, start_text_rect)
    else:
        pygame.draw.rect(screen, COLOR_PADDLE, (player_1_x, player_1_y, player_1_width, player_1_height))

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()