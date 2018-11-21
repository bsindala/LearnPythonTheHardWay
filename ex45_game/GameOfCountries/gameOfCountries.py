from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class GameEngine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n********** Game On **********"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
    quips = [
        "You failed!!! You knowledge of countries is appalling.",
        "It seems to me you wasted your time in grade school,",
        "or rather you wasted your parents money.",
        "Either way, pick up some atlas and know something about each country.",
        "My fifth grade niece can do a whole lot better than this."
    ]

    def enter(self):
        print Death.equips[randint(0, len(self.equips) - 1)]
        exit(1)

class RandomCountry(Scene):
    def enter(self):
        print "TODO: Select random country"

class CapitalCity(Scene):
    def enter(self):
        print "TODO: Enter capital city"

class IndependenceDay(Scene):
    def enter(self):
        print "TODO: Enter Independence Day format (Day Month e.g. 01 January)"

class IndependenceYear(Scene):
    def enter(self):
        print "TODO: Enter Independence Year"

class TypeOfLeadership(Scene):
    def enter(self):
        print "TODO: Enter the type of leadership"

class Map(object):
    scenes = {
        'random_country' : RandomCountry(),
        'capital_city' : CapitalCity(),
        'independence_day' : IndependenceDay(),
        'independence_year' : IndependenceYear(),
        'type_of_leadership' : TypeOfLeadership()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('random_country')
a_game = Engine(a_map)
a_game.play()
