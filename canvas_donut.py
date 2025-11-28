import pygame
import math
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Rotating Donut")
clock = pygame.time.Clock()

# Constants
R1 = 1  # Radius of the small circle
R2 = 2  # Radius of the large circle
K1 = 150  # Scaling factor
K2 = 5  # Distance from the viewer

def render_canvas_donut():
    A, B = 0, 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Clear the screen
        screen.fill((0, 0, 0))
        # Precompute trigonometric values
        cosA, sinA = math.cos(A), math.sin(A)
        cosB, sinB = math.cos(B), math.sin(B)
        for theta in [i * 0.3 for i in range(0, int(2 * math.pi / 0.3))]:
            costheta, sintheta = math.cos(theta), math.sin(theta)
            for phi in [i * 0.1 for i in range(0, int(2 * math.pi / 0.1))]:
                cosphi, sinphi = math.cos(phi), math.sin(phi)
                h = R2 + R1 * costheta
                x = h * (cosB * cosphi + sinA * sinB * sinphi) - R1 * sintheta * cosA * sinB
                y = h * (sinB * cosphi - sinA * cosB * sinphi) + R1 * sintheta * cosA * cosB
                z = K2 + cosA * h * sinphi + sinA * R1 * sintheta
                ooz = 1 / z
                xp = int(WIDTH // 2 + K1 * ooz * x)
                yp = int(HEIGHT // 2 - K1 * ooz * y)
                L = 0.7 * (cosphi * costheta * sinB - cosA * costheta * sinphi - sinA * sintheta
                           + cosB * (cosA * sintheta - costheta * sinA * sinphi))
                if L > 0:
                    color = (int(L * 255), int(L * 255), int(L * 255))
                    pygame.draw.rect(screen, color, (xp, yp, 2, 2))
        
        pygame.display.flip()
        A += 0.07
        B += 0.03
        clock.tick(20)

# Run the graphical donut
render_canvas_donut()
