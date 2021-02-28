class Scene(object):
    def enter(self):
        pass

class Engine:
    def __init__(self,scene_map):
        pass
    def play(self):
        print('I am playing')
class Death:
    def enter(self):
        pass


class CentralCorridor:
    def enter(self):
        pass

class LaserWeaponArmoy(Scene):
    def enter(self):
        pass
class TheBridge(Scene):
    def enter(self):
        pass
class EscapePod:
    def enter(self):
        pass
class Map(object):
    def __init__(self,scene_start):
        pass
    def next_scene(self,scene_name):
        pass
    def opening_scene(self):
        pass
if __name__ == '__main__':
    a_map=Map('central_corridor')
    a_game=Engine(a_map)
    a_game.play()