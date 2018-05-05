import pygame
from src.Scene.scene_manager import SceneManager
from src.Scene.title_scene import TitleScene
from src.Scene.game_scene import GameScene
from src.Scene.end_scene import EndScene

pygame.init()
pygame.font.init()

# Game constants:

WORLD_SIZE = WIDTH, HEIGHT = 400, 600
WORLD_COLOR = (0, 0, 0)

# Set windows basic attributes:

pygame.display.set_caption("Flappy Dot - V1")
game_display = pygame.display.set_mode(WORLD_SIZE)

# Game variables:
scene_manager = SceneManager()
scene_manager.set_scene(TitleScene(game_display, 1, WORLD_SIZE))

# Main loop

while True:
    # Set FPS = 60
    pygame.time.delay(1000//60)

    # Set background color
    game_display.fill(WORLD_COLOR)

    # Transition of scenes:
    if scene_manager.get_scene().end():
        if scene_manager.get_scene().get_id() == 1:
            # Change to Game Scene
            scene_manager.set_scene(GameScene(game_display, 2, WORLD_SIZE))
        elif scene_manager.get_scene().get_id() == 2:
            scene_manager.set_scene(EndScene(game_display, 3, WORLD_SIZE))
        elif scene_manager.get_scene().get_id() == 3:
            scene_manager.set_scene(TitleScene(game_display, 1, WORLD_SIZE))
        else:
            pass
    scene_manager.get_scene().update()
    scene_manager.get_scene().render()

    pygame.display.update()