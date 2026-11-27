
from ursina import *

from player import create_player
from environment import create_environment
from camera import set_camera_view, toggle_camera
from menu import create_menu

app = Ursina()

window.title = "3D Battle Game"
window.borderless = False
window.fullscreen = False

# Lighting
DirectionalLight().look_at(Vec3(1, -1, -1))

# Create world
create_environment()

# Create player
player = create_player()
player.enabled = False

# Game state
game_started = False

# Start game function
def start_game():
    global game_started

    game_started = True

    for item in menu_items:
        item.enabled = False

    player.enabled = True
    mouse.locked = True

    set_camera_view(player, "first")


# Create menu
menu_items = create_menu(start_game)

# Keyboard controls
def input(key):

    if not game_started:
        return

    if key == "v":
        toggle_camera(player)

    if key == "escape":
        mouse.locked = False


# Display controls
Text(
    text="WASD: Move | SPACE: Jump | V: Change Camera",
    position=(-0.85, -0.46),
    scale=0.8
)

app.run()
