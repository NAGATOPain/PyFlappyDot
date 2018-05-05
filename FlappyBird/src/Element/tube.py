import pygame, random


class Tube:

    __TUBE_COLOR = (255, 255, 255)
    __TUBE_SIZE = 50
    __SPEED = 1
    __SPACE_BETWEEN_TUBE = 200

    def __init__(self, display, w_size):
        self.__w_size = w_size
        self.__display = display
        self.__tube = []
        self.__tube.append([w_size[0], w_size[1] // 2, 100, False]) # Pos w,h; space between 2 tubes up down ; whether be passed

    def __create(self):
        x = self.__w_size[0]
        y = random.randint(self.__TUBE_SIZE, self.__w_size[1] - self.__TUBE_SIZE * 2)
        space = random.randint(90, 120)
        passed = False
        self.__tube.append([x, y, space, passed])

    def get_tube(self):
        return self.__tube

    def get_size(self):
        return self.__TUBE_SIZE

    def update(self):
        for i in self.__tube:
            i[0] -= self.__SPEED
        # Create new tube if last tube goes long enough
        if self.__tube[len(self.__tube) - 1][0] <= self.__w_size[0] - self.__SPACE_BETWEEN_TUBE:
            self.__create()
        # Delete the first tube if it goes over the screen:
        if self.__tube[0][0] <= -self.__TUBE_SIZE:
            self.__tube.pop(0)

    def render(self):
        for i in self.__tube:
            pygame.draw.rect(self.__display, self.__TUBE_COLOR, (i[0], 0, self.__TUBE_SIZE, i[1]), 5)
            pygame.draw.rect(self.__display, self.__TUBE_COLOR,
                             (i[0], i[1] + i[2], self.__TUBE_SIZE, self.__w_size[1] - (i[1] + i[2])), 5)
