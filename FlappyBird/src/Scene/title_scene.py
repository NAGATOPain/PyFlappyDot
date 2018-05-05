from src.Scene.scene import *
import pygame


class TitleScene(Scene):

    __FONT = "Arial"
    __TITLE = "FLAPPY DOT"
    __TUTORIAL = "Space to Play !"
    __FONT_COLOR = (255, 255, 255)

    def __init__(self, display, id, w_size):
        super().__init__(display, id, w_size)
        # Init title
        font_title = pygame.font.SysFont(self.__FONT, 50)
        font_title.set_bold(True)
        self.__title_lbl = font_title.render(self.__TITLE, True, self.__FONT_COLOR)

        # Init tutorial
        font_tut = pygame.font.SysFont(self.__FONT, 20)
        font_tut.set_bold(True)
        self.__tut_lbl = font_tut.render(self.__TUTORIAL, True, self.__FONT_COLOR)

    def update(self):
        super().update()
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Change Scene to Game Scene:
                    self._isEndScene = True
                else: pass
            else: pass

    def render(self):
        super().render()
        # Render Title
        self._display.blit(self.__title_lbl,
                        ((self._w_size[0] - self.__title_lbl.get_width()) // 2,
                         self._w_size[1] // 3 - self.__title_lbl.get_height() // 2))
        # Render tutorial
        self._display.blit(self.__tut_lbl,
                           ((self._w_size[0] - self.__tut_lbl.get_width()) // 2,
                            self._w_size[1] // 2 - self.__tut_lbl.get_height() // 2))