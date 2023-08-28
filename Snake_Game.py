import pygame
import random

pygame.init()

# Define the screen dimensions
screen_width = 800
screen_height = 600

# Define colors
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Snake block size and speed
block_size = 20
snake_speed = 15

# Create the game screen
game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Define the snake
def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_screen, green, [x[0], x[1], block_size, block_size])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Initial position of the snake
    lead_x = screen_width / 2
    lead_y = screen_height / 2

    # Initial movement direction of the snake
    lead_x_change = 0
    lead_y_change = 0

    # Store the body of the snake as a list of coordinates
    snake_list = []
    snake_length = 1

    # Generate initial position of food
    food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size

    clock = pygame.time.Clock()

    while not game_over:

        while game_close:
            game_screen.fill(white)
            font_style = pygame.font.SysFont(None, 50)
            message = font_style.render("You Lost! Press Q-Quit or C-Play Again", True, blue)
            game_screen.blit(message, [screen_width / 6, screen_height / 3])

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        # Check for boundaries
        if lead_x >= screen_width or lead_x < 0 or lead_y >= screen_height or lead_y < 0:
            game_close = True

        lead_x += lead_x_change
        lead_y += lead_y_change
        game_screen.fill(white)
        pygame.draw.rect(game_screen, red, [food_x, food_y, block_size, block_size])
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        our_snake(block_size, snake_list)
        pygame.display.update()

        if lead_x == food_x and lead_y == food_y:
            food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
