
class Scene(object):
    def enter(self):
        pass

    def play(self):
        pass

class Engine(object):
    def __init__(self, scene_map):
        print('Game started')
        self.scene_map = scene_map
        scene_map.opening_scene()
    def play(self):
        pass

class Death(Scene):

    def enter(self):
        pass

class CentralCorridor(Scene):

    def enter(self):
        pass

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self, start_scene):
        if start_scene == 'central corridor':
            self.scene = CentralCorridor()
    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central corridor')
a_game = Engine(a_map)
a_game.play()
