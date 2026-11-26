
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

window.title = "3D Game"

# Sky
Sky()

# Ground
ground = Entity(
    model="plane",
    scale=(100, 1, 100),
    color=color.rgb(75, 130, 75),
    collider="box"
)

# Player
player = FirstPersonController()
player.position = (0, 2, 0)
player.speed = 6

# Buildings
for x in range(-20, 21, 10):
    Entity(
        model="cube",
        position=(x, 2, 15),
        scale=(5, 4, 5),
        color=color.gray,
        collider="box"
    )

# Lighting
DirectionalLight().look_at(Vec3(1, -1, -1))

# Game title
Text(
    text="3D BATTLE GAME",
    position=(-0.85, 0.45),
    scale=2
)

app.run()
