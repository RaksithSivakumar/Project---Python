import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Virtual Pet Game")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PET_COLOR = (200, 100, 100)


font = pygame.font.SysFont(None, 55)
small_font = pygame.font.SysFont(None, 35)


pet = {
    "happiness": 100,
    "health": 100,
    "level": 1,
    "experience": 0,
    "x": WIDTH // 2,
    "y": HEIGHT // 2,
    "size": 50
}


def feed_pet():
    pet["health"] += 10
    if pet["health"] > 100:
        pet["health"] = 100
    pet["experience"] += 10

def play_with_pet():
    pet["happiness"] += 10
    if pet["happiness"] > 100:
        pet["happiness"] = 100
    pet["experience"] += 10

def check_level_up():
    if pet["experience"] >= 100:
        pet["level"] += 1
        pet["experience"] = 0
        return True
    return False

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def draw_pet(surface, pet):
    pygame.draw.circle(surface, PET_COLOR, (pet["x"], pet["y"]), pet["size"])
    
    eye_size = pet["size"] // 5
    pygame.draw.circle(surface, BLACK, (pet["x"] - eye_size, pet["y"] - eye_size), eye_size)
    pygame.draw.circle(surface, BLACK, (pet["x"] + eye_size, pet["y"] - eye_size), eye_size)
    
    pygame.draw.arc(surface, BLACK, [pet["x"] - eye_size, pet["y"], 2 * eye_size, eye_size], 3.14, 0, 2)


running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                feed_pet()
            elif event.key == pygame.K_p:
                play_with_pet()

    
    if check_level_up():
        print("Level up! Your pet is now level", pet["level"])

    
    draw_pet(screen, pet)

    
    draw_text(f"Happiness: {pet['happiness']}", small_font, BLACK, screen, 10, 10)
    draw_text(f"Health: {pet['health']}", small_font, BLACK, screen, 10, 40)
    draw_text(f"Level: {pet['level']}", small_font, BLACK, screen, 10, 70)
    draw_text(f"Experience: {pet['experience']}", small_font, BLACK, screen, 10, 100)

    
    draw_text("Press 'F' to Feed", small_font, BLUE, screen, 10, HEIGHT - 70)
    draw_text("Press 'P' to Play", small_font, BLUE, screen, 10, HEIGHT - 40)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
