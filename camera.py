
from ursina import *


third_person = False


def set_camera_view(player, view):
    global third_person

    if view == "third":
        third_person = True
        camera.position = (0, 2, -7)
        camera.rotation = (12, 0, 0)

    else:
        third_person = False
        camera.position = (0, 0, 0)
        camera.rotation = (0, 0, 0)


def toggle_camera(player):
    if third_person:
        set_camera_view(player, "first")
    else:
        set_camera_view(player, "third")
      
