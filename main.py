# -*- coding: utf-8 -*-
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


class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 50
        self.width = 20
        self.height = 30
        self.speed = 5
        try:
            img = pygame.image.load("Pixel-Art Geschäftsmann im Anzug.png").convert_alpha()
            self.image = pygame.transform.scale(img, (self.width, self.height))
        except (pygame.error, FileNotFoundError):
            self.image = None

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        self.x = max(0, min(WIDTH - self.width, self.x))

    def draw(self, surface):
        if self.image:
            surface.blit(self.image, (self.x, self.y - self.height))
        else:
            rect = pygame.Rect(self.x, self.y - self.height, self.width, self.height)
            pygame.draw.rect(surface, BLACK, rect)

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
    font = pygame.font.SysFont(None, 24)
    clock = pygame.time.Clock()

    trees = [Tree(x, HEIGHT - 20) for x in range(20, WIDTH, 40)]
    helicopters = [Helicopter() for _ in range(3)]
    player = Player()

    sayings = [
        "Das ist Wachstum, meine Freunde!",
        "Vertrag? Gern, das ist mein Job.",
        "Alles eine Frage der Effizienz!",
        "Verträge stapeln? Ich nenne das Skalierung!",
        "Reden wir später über Geld – ich habe zu tun!",
        "Liquidität ist Einstellungssache.",
        "Wem gehört hier eigentlich was?",
        "Ich sehe nur Lösungen!",
        "Mit Kaffee geht alles besser.",
        "Kurze Pause? Gibt’s bei mir nicht.",
        "Das steckt man weg.",
        "Risiko gehört dazu!",
        "Da lacht doch das Unternehmerherz.",
        "Sie wollen Zahlen? Ich zeig Ihnen, wie’s geht!",
        "Journalisten stellen viele Fragen, Unternehmer liefern Antworten.",
        "Am Ende zählt das Ergebnis!",
        "Erfolg ist, wenn man trotzdem lacht.",
        "Nächstes Projekt, nächster Erfolg."
    ]
    current_saying = ""
    say_timer = 0

    running = True
    tick = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.update(keys)

        if (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]) and say_timer == 0:
            current_saying = random.choice(sayings)
            say_timer = 120

        tick += 1
        screen.fill(SKY)

        for tree in trees:
            tree.draw(screen)

        for heli in helicopters:
            heli.update()
            heli.draw(screen, tick)

        player.draw(screen)

        if say_timer > 0:
            text = font.render(current_saying, True, BLACK)
            screen.blit(text, (10, HEIGHT - 30))
            say_timer -= 1

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
