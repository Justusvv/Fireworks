import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fireworks Screensaver")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = random.randint(2, 4)
        self.x_velocity = random.uniform(-2, 2)
        self.y_velocity = random.uniform(-2, 2)
        self.lifetime = random.randint(20, 50)

    def update(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
        self.lifetime -= 1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

class Firework:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT // 2)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.particles = [Particle(self.x, self.y, self.color) for _ in range(100)]

    def update(self):
        for particle in self.particles:
            particle.update()
        self.particles = [particle for particle in self.particles if particle.lifetime > 0]

    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)

def main():
    clock = pygame.time.Clock()
    fireworks = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        if random.randint(0, 10) == 0:
            fireworks.append(Firework())

        for firework in fireworks:
            firework.update()
            firework.draw(screen)

        fireworks = [firework for firework in fireworks if len(firework.particles) > 0]

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
