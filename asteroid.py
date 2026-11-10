import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self, x:float, y:float, radius:float)->None:
        super().__init__(x,y,radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        
    def split(self) -> None:
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        else:
            log_event("asteroid_split")
            ang1 = random.uniform(20,50)
            vel_ast1 = self.velocity.rotate(ang1)
            vel_ast2 = self.velocity.rotate(-ang1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = vel_ast1 * 1.2
            asteroid2.velocity = vel_ast2 * 1.2
            