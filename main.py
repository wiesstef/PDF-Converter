import pygame
from pygame.locals import *
import time
import random


def draw_snake(surface, snake):
    # Draw the snake on the game surface
    render_background(surface)
    block = pygame.image.load("resources/block.png").convert()
    for segment in snake:
        x, y = segment
        surface.blit(block, (x, y))
    pygame.display.flip()


def draw_apple(surface, apple):
    # Draw the apple on the game surface
    apple_image = pygame.image.load("resources/apple.png").convert()
    x, y = apple
    surface.blit(apple_image, (x, y))
    pygame.display.flip()


def is_collision(x1, y1, x2, y2):
    # Check if two objects collide based on their coordinates
    if x1 >= x2 and x1 < x2 + 40:
        if y1 >= y2 and y1 < y2 + 40:
            return True
    return False


def move():
    # Generate random coordinates for the apple
    x = random.randint(0, (800 - 40) // 40) * 40
    y = random.randint(1, (600 - 40) // 40) * 40
    return [x, y]


def display_score(surface, score):
    # Display the current score on the game surface
    font = pygame.font.SysFont('calibri', 30)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    surface.blit(score_text, (600, 10))
    pygame.display.flip()


def show_game_over(surface, score):
    # Display the game over screen with the final score
    render_background(surface)
    font = pygame.font.SysFont('calibri', 30)
    line1 = font.render("GAME OVER", True, (255, 255, 255))
    surface.blit(line1, (200, 250))
    line2 = font.render(f"Your Score: {score}", True, (255, 255, 255))
    surface.blit(line2, (200, 300))
    line3 = font.render("To play again press Enter!", True, (255, 255, 255))
    surface.blit(line3, (200, 350))
    pygame.display.flip()
    pygame.mixer.music.pause()


def reset(surface, snake):
    # Reset the game state
    render_background(surface)
    block = pygame.image.load("resources/block.png").convert()
    for segment in snake:
        x, y = segment
        surface.blit(block, (x, y))
    pygame.display.flip()


def move_left():
    # Set the direction to left
    return 'left'


def move_right():
    # Set the direction to right
    return 'right'


def move_up():
    # Set the direction to up
    return 'up'


def move_down():
    # Set the direction to down
    return 'down'


def walk(snake, direction):
    # Move the snake in the specified direction
    length = len(snake)
    x, y = snake[0][0], snake[0][1]
    if direction == 'left':
        x -= 40
        if x < 0:
            x = 800 - 40
    if direction == 'right':
        x += 40
        if x >= 800:
            x = 0
    if direction == 'up':
        y -= 40
        if y < 0:
            y = 600 - 40
    if direction == 'down':
        y += 40
        if y >= 600:
            y = 0
    snake.insert(0, (x, y))
    snake = snake[:length]
    return snake


def play_background_music():
    # Play the background music
    pygame.mixer.music.load("resources/background.mp3")
    pygame.mixer.music.play()


def render_background(surface):
    # Render the background image on the game surface
    bg = pygame.image.load("resources/background.jpg")
    surface.blit(bg, (0, 0))


def run_game():
    # Initialize pygame and set up the game window
    pygame.init()
    pygame.mixer.init()
    surface = pygame.display.set_mode((800, 600))
    snake = [(120, 120)]
    direction = 'down'
    apple = move()
    draw_snake(surface, snake)
    play_background_music()

    running = True
    pause = False
    score = 0

    while running:
        # Main game loop, continues until the game is no longer running
        for event in pygame.event.get():
            # Iterate over the events in the event queue
            if event.type == KEYDOWN:
                # Check if a key is pressed
                if event.key == K_ESCAPE:
                    # If the Escape key is pressed, stop the game loop
                    running = False
                elif event.key == K_LEFT:
                    # If the left arrow key is pressed, change the direction to left
                    direction = move_left()
                elif event.key == K_RIGHT:
                    # If the right arrow key is pressed, change the direction to right
                    direction = move_right()
                elif event.key == K_UP:
                    # If the up arrow key is pressed, change the direction to up
                    direction = move_up()
                elif event.key == K_DOWN:
                    # If the down arrow key is pressed, change the direction to down
                    direction = move_down()
                elif event.key == K_RETURN:
                    # If the Enter key is pressed
                    if pause:
                        # If the game is paused, reset the game state
                        snake = [(120, 120)]
                        direction = 'down'
                        apple = move()
                        score = 0
                        reset(surface, snake)
                        pygame.mixer.music.unpause()
                        pause = False
            elif event.type == QUIT:
                # If the window close button is clicked, stop the game loop
                running = False

        if not pause:
            # If the game is not paused, perform game logic and update the game surface
            snake = walk(snake, direction)
            draw_snake(surface, snake)
            draw_apple(surface, apple)
            display_score(surface, score)
            pygame.display.flip()

            if is_collision(snake[0][0], snake[0][1], apple[0], apple[1]):
                # If the snake's head collides with the apple, handle apple collision
                sound = pygame.mixer.Sound("resources/eating_apple.mp3")
                pygame.mixer.Sound.play(sound)
                snake.append(snake[-1])
                apple = move()
                score += 1

            for i in range(2, len(snake)):
                # Check for collision between the snake's head and its body segments
                if is_collision(snake[0][0], snake[0][1], snake[i][0], snake[i][1]):
                    # If there is a collision, pause the game and display game over screen
                    sound = pygame.mixer.Sound("resources/snake_collision.mp3")
                    pygame.mixer.Sound.play(sound)
                    pause = True
                    show_game_over(surface, score)
                    break

        time.sleep(0.2)


if __name__ == '__main__':
    run_game()
