
from ursina import *


def create_menu(on_start):

    title = Text(
        text="3D BATTLE GAME",
        origin=(0, 0),
        scale=3,
        position=(0, 0.35)
    )

    subtitle = Text(
        text="ENTER THE BATTLE",
        origin=(0, 0),
        scale=1,
        position=(0, 0.23)
    )

    start_button = Button(
        text="START GAME",
        scale=(0.3, 0.08),
        position=(0, 0.05),
        color=color.azure,
        on_click=on_start
    )

    settings_button = Button(
        text="SETTINGS",
        scale=(0.3, 0.08),
        position=(0, -0.07),
        color=color.gray
    )

    exit_button = Button(
        text="EXIT",
        scale=(0.3, 0.08),
        position=(0, -0.19),
        color=color.dark_gray,
        on_click=application.quit
    )

    return [
        title,
        subtitle,
        start_button,
        settings_button,
        exit_button
    ]
  
