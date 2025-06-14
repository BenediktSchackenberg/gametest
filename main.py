import pygame
import random

# Screen size
WIDTH, HEIGHT = 800, 600

# Colors
SKY = (135, 206, 235)
BROWN = (139, 69, 19)
GREEN = (34, 139, 34)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

class Tree:
    def __init__(self, x, base_y):
        self.x = x
        self.base_y = base_y
        self.width = 10
        self.height = 30

    def draw(self, surface):
        trunk_rect = pygame.Rect(self.x, self.base_y - self.height, 4, self.height)
        pygame.draw.rect(surface, BROWN, trunk_rect)
        foliage_points = [
            (self.x - self.width, self.base_y - self.height),
            (self.x + 2, self.base_y - self.height - self.height // 2),
            (self.x + self.width + 4, self.base_y - self.height)
        ]
        pygame.draw.polygon(surface, GREEN, foliage_points)

class Helicopter:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(50, HEIGHT // 2)
        self.dx = random.choice([-2, 2])

    def update(self):
        self.x += self.dx
        if self.x < 0 or self.x > WIDTH:
            self.dx *= -1
        
    def draw(self, surface, tick):
        body_rect = pygame.Rect(self.x, self.y, 40, 10)
        pygame.draw.rect(surface, GRAY, body_rect)
        pygame.draw.line(surface, BLACK, (self.x + 20, self.y), (self.x + 20, self.y - 10), 2)
        rotor_offset = 10 if tick % 20 < 10 else -10
        pygame.draw.line(surface, BLACK, (self.x + 20 - 15, self.y - 10), (self.x + 20 + 15, self.y - 10 + rotor_offset), 2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    trees = [Tree(x, HEIGHT - 20) for x in range(20, WIDTH, 40)]
    helicopters = [Helicopter() for _ in range(3)]

    running = True
    tick = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        tick += 1
        screen.fill(SKY)

        for tree in trees:
            tree.draw(screen)

        for heli in helicopters:
            heli.update()
            heli.draw(screen, tick)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
