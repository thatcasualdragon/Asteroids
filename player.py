from circleshape import CircleShape
import constants
import pygame

class Player(CircleShape):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # draw the player's piece on the screen
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), constants.LINE_WIDTH)

    def rotate(self, dt):
        self.rotation = (constants.PLAYER_TURN_SPEED * dt) + self.rotation

    # move the player's piece up, down, left, and right on screen
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_j]:
                self.rotate(0 - dt)
        if keys[pygame.K_l]:
                self.rotate(dt)
        if keys[pygame.K_i]:
                self.move(dt)
        if keys[pygame.K_k]:
                self.move(0 - dt)

    #math for moving up and down on screen
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * constants.PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
