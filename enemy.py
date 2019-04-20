from force_field import ForceField
from game_object import GameObject
from fellow import Fellow
from heroes import Hero
import pygame
from geometry import *
from bullet import Bullet


class Enemy(Hero):
    def __init__(self, x, y, game):
        super().__init__(x, y, 45, game, 'images/enemy.png')
        self.x = x
        self.y = y

    def update(self):
        if not self.game.player.is_alive:
            return
        self.orientate_to(self.game.player.x, self.game.player.y)
        #self.rotation_vector = get_vector(
        #    (self.x, self.y), (self.game.player.x, self.game.player.y))
        self.choose_direction()
        dx = self.move_direction[0] * self.speed
        dy = self.move_direction[1] * self.speed
        dx, dy = self.check_collision_with_other_enemies(dx, dy)
        self.move(dx, dy)

    def choose_direction(self):
        if math.fabs(self.x - self.game.player.x) > math.fabs(self.y - self.game.player.y):
            if self.x < self.game.player.x:
                self.move_direction = (1, 0)
            else:
                self.move_direction = (-1, 0)
        else:
            if self.y < self.game.player.y:
                self.move_direction = (0, 1)
            else:
                self.move_direction = (0, -1)

    def handle_collisions(self, coll_objects):
        for object in coll_objects:
            if isinstance(object, Fellow) or isinstance(object, Bullet):
                self.is_alive = False
            elif isinstance(object, ForceField):
                self.move_direction = (0, 0)

    def check_collision_with_other_enemies(self, dx, dy):
        for enemy in self.game.enemies:
            if enemy != self:
                if calculate_distance((self.x + dx, self.y + dy), (enemy.x, enemy.y)) < enemy.radius * 2:
                    return 0, 0
        return dx, dy
