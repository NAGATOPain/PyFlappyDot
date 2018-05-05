import pygame, os

class Bird:

    # Bird attributes:
    __RATIO = 15
    __COLOR = (255, 255, 0)

    # Other attributes:
    __GRAVITY = 3
    __JUMP_HEIGHT = 50

    def __init__(self, display, w_size):
        self.__display = display
        self.__w_size = w_size
        self.__pos = [self.__w_size[0] // 2, self.__w_size[1] // 2]
        self.__clock = 0.5
        self.__die = False

        # Audio of bird
        flap_path = os.path.abspath("sounds/sfx_wing.ogg")
        self.__flap_effect = pygame.mixer.Sound(flap_path)

    def move(self):
        self.__flap_effect.play()
        self.__clock = 0.5
        self.__pos[1] -= self.__JUMP_HEIGHT

    def update(self):
        if not self.__pos[1] >= self.__w_size[1]: # Prevent bird not to fall over the screen
            # Fall:
            self.__clock += 1 / 60
            self.__pos[1] += round(self.__GRAVITY * self.__clock ** 2) 
        else:
            # If bird fall to ground:
            self.__die = True

    def render(self):
        pygame.draw.circle(self.__display, self.__COLOR, tuple(self.__pos), self.__RATIO, 5)

    def get_pos(self):
        return self.__pos

    def get_ratio(self):
        return self.__RATIO

    def is_die(self): return self.__die

    def die(self):
        self.__die = True