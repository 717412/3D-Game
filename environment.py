
from ursina import *


def create_environment():

    # Ground
    ground = Entity(
        model="plane",
        scale=(100, 1, 100),
        color=color.rgb(75, 135, 75),
        collider="box"
    )

    # Roads
    Entity(
        model="cube",
        position=(0, 0.02, 15),
        scale=(100, 0.05, 8),
        color=color.dark_gray
    )

    # Buildings
    building_positions = [
        (-15, 10),
        (15, 10),
        (-15, 25),
        (15, 25),
        (0, 40)
    ]

    for x, z in building_positions:
        Entity(
            model="cube",
            position=(x, 3, z),
            scale=(8, 6, 8),
            color=color.rgb(125, 130, 140),
            collider="box"
        )

    # Trees
    for x, z in [(-25, 5), (25, 5), (-25, 30), (25, 30)]:
        Entity(
            model="cylinder",
            position=(x, 1, z),
            scale=(0.7, 2, 0.7),
            color=color.brown
        )

        Entity(
            model="sphere",
            position=(x, 3, z),
            scale=3,
            color=color.green
        )

    Sky()

    return ground
  
