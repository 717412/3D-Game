
from ursina import *


def create_character_select(on_confirm):

    selected = {"name": "Explorer"}

    title = Text(
        text="SELECT YOUR CHARACTER",
        origin=(0, 0),
        position=(0, 0.35),
        scale=2
    )

    description = Text(
        text="Choose your player",
        origin=(0, 0),
        position=(0, 0.23)
    )

    explorer = Button(
        text="EXPLORER",
        position=(-0.25, 0.05),
        scale=(0.3, 0.1),
        color=color.azure,
        on_click=lambda: select("Explorer")
    )

    scout = Button(
        text="SCOUT",
        position=(0.25, 0.05),
        scale=(0.3, 0.1),
        color=color.green,
        on_click=lambda: select("Scout")
    )

    selected_text = Text(
        text="Selected: Explorer",
        origin=(0, 0),
        position=(0, -0.08)
    )

    start_button = Button(
        text="CONFIRM",
        position=(0, -0.22),
        scale=(0.3, 0.1),
        color=color.orange,
        on_click=lambda: on_confirm(selected["name"])
    )

    def select(name):
        selected["name"] = name
        selected_text.text = "Selected: " + name

    return [
        title,
        description,
        explorer,
        scout,
        selected_text,
        start_button
    ]
  
