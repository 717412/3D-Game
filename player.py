
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


def create_player():
    player = FirstPersonController()

    player.position = (0, 2, 0)
    player.speed = 6
    player.jump_height = 2
    player.gravity = 1

    return player
  
