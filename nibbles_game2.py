import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (500, 500)

# Set up the game window
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Nibbles Game")

# Set up the clock
clock = pygame.time.Clock()

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Set up the game variables
snake_pos = [250, 250]
snake_body = [[250, 250], [240, 250], [230, 250]]
direction = "RIGHT"
food_pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
food_spawned = True
new_segment = False
score = 0

# Set up the font for displaying score
font = pygame.font.Font(None, 30)

# Define the function for drawing the snake and the food
def draw_snake(snake_body):
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))

def draw_food(food_pos):
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

# Game loop
game_over = False
while not game_over:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"
            elif event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"

    # Move the snake
    if direction == "RIGHT":
        snake_pos[0] += 10
    elif direction == "LEFT":
        snake_pos[0] -= 10
    elif direction == "UP":
        snake_pos[1] -= 10
    elif direction == "DOWN":
        snake_pos[1] += 10

    # Check if the snake has hit the wall or itself
    if snake_pos[0] < 0 or snake_pos[0] > window_size[0]-10 or snake_pos[1] < 0 or snake_pos[1] > window_size[1]-10:
        game_over = True
    for body_part in snake_body[1:]:
        if snake_pos == body_part:
            game_over = True

    # Check if the snake has eaten the food
    if snake_pos == food_pos:
        food_spawned = False
        new_segment = True
        score += 1
        snake_pos = list(snake_pos) # create a new instance of the position to make the body longer
        if new_segment:
            snake_body.append(list(snake_body[-1]))

    # Spawn a new food if needed
    if not food_spawned:
        food_pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
        food_spawned = True

    # Update the snake body
    snake_body.insert(0, list(snake_pos))
    if snake_pos != food_pos:
        snake_body.pop()
    else:
        food_spawned = False

    # Clear the screen
    screen.fill(black)

    # Draw the snake and the food
    draw_snake(snake_body)
    draw_food(food_pos)

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(10)
