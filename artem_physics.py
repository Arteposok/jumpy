import types
import numpy as np
import pygame as pyg


class Object:
    def __init__(self, rect:pyg.Rect, velocity=np.array([0,0])):
        self.rect=rect
        self.sprite=None
        self.velocity=velocity

    def set_collide(self):
        def wrapper(func:types.FunctionType):
            self.collide=func
        return wrapper

    def set_update(self):
        def wrapper(func:types.FunctionType):
            self.update=func
        return wrapper

    def update(self, gravity):
        self.velocity+=np.array([0,9])
        print(self.velocity)

    def collide(self, incoming):
        pass

class WorldBox:
    def __init__(self, gravity:tuple[int, int]):
        self.gravity=gravity
        self.objects_to_simulate:list[Object]=[]

    def update(self):
        for object in self.objects_to_simulate:
            for incoming in self.objects_to_simulate:
                if object!=incoming and object.rect.colliderect(incoming.rect):
                    object.collide(incoming)
            object.update(self.gravity)


    def add_object(self, object:Object):
        self.objects_to_simulate.append(object)


def test_stuff():
    world=WorldBox((0,9))
    example=Object(pyg.Rect(0,0,32,32), np.array([0,0]))
    world.add_object(example)
    for i in range(100):
        world.update()

if __name__=="__main__":
    test_stuff()