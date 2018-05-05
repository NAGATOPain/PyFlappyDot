from src.Scene.scene import *
from src.Element.bird import *
from src.Element.tube import *
import pygame, os


class GameScene(Scene):

    __FONT_COLOR = (136, 0, 100)
    __FONT = "Arial"

    def __init__(self, display, id, w_size):
        super().__init__(display, id, w_size)
        # Init bird and tubes
        self.__bird = Bird(display, w_size)
        self.__tube = Tube(display, w_size)

        #Init score label
        self.__font = pygame.font.SysFont(self.__FONT, 50)
        self.__font.set_bold(True)
        self.__score = 0
        self.__score_lbl = str(self.__score)

        # Audio
        point_path = os.path.abspath("sounds/sfx_point.ogg")
        self.__point_effect = pygame.mixer.Sound(point_path)

        hit_path = os.path.abspath("sounds/sfx_hit.ogg")
        self.__hit_effect = pygame.mixer.Sound(hit_path)

    def update(self):
        super().update()
        # Events handling:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.__bird.move()
        # If bird die, tubes will stop moving
        if not self.__bird.is_die():
            self.__tube.update()
        self.__bird.update()
        # Update score
        self.__score_lbl = str(self.__score)
        # Check if bird interacts with tubes
        for i in self.__tube.get_tube():
            if i[0] - self.__bird.get_ratio() <= self.__bird.get_pos()[0] \
                    < i[0] + self.__tube.get_size() + self.__bird.get_ratio() and not i[3]: 
                #i[3] means whether tube  not passed by bird
                if self.__bird.get_pos()[1] < i[1] + self.__bird.get_ratio() \
                        or self.__bird.get_pos()[1] > i[1] + i[2] - self.__bird.get_ratio():
                    # Bird dies
                    if not self.__bird.is_die(): #Play sound effect of die 1 time
                        self.__hit_effect.play()
                    self.__bird.die()
            # Bird've passed a tube and plus 1 point
            if self.__bird.get_pos()[0] >= i[0] + self.__tube.get_size() and not i[3]:
                self.__point_effect.play()
                self.__score += 1
                i[3] = True

        # If bird died and fall to the ground
        if self.__bird.get_pos()[1] >= self._w_size[1]:
            self._isEndScene = True

    def render(self):
        super().render()
        self.__tube.render()
        self.__bird.render()
        score_lbl = self.__font.render(self.__score_lbl, True, self.__FONT_COLOR)
        self._display.blit(score_lbl,
                           ((self._w_size[0] - score_lbl.get_width()) // 2,
                            self._w_size[1] // 6 - score_lbl.get_height() // 2))