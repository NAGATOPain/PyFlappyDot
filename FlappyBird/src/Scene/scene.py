class Scene:

    def __init__(self, display, id, w_size):
        self._isEndScene = False
        self._display = display
        # id = 1 means title_scene, id = 2 means game_scene, id = 3 means end_scene
        self._id = id
        self._w_size = w_size

    def update(self):
        pass

    def render(self):
        pass

    def get_id(self):
        return self._id

    def end(self):
        return self._isEndScene
