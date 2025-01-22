import types
import numpy as np
import pygame as pyg


class Object:
    def __init__(self, rect:pyg.Rect,
                 use_gravity: bool,
                 velocity=np.array([0,0])):
        self.use_gravity=use_gravity
        self.rect=rect
        self.sprite=None
        self.velocity=velocity
        self.gravity=-1

    def set_collide(self):
        def wrapper(func:types.FunctionType):
            self.collide=func
        return wrapper

    def set_update(self):
        def wrapper(func:types.FunctionType):
            self.update=func
        return wrapper

    def update(self, gravity):
        self.gravity=gravity[1]
        if self.use_gravity:
            self.rect=self.rect.move(self.velocity[0],self.velocity[1])
            self.velocity[0] += gravity[0]
            self.velocity[1] += gravity[1]

    def collide(self, incoming):
        if self.use_gravity:
            self.rect.move(0, self.velocity[1])
            self.velocity[1]=0


    def set_speed(self, **kw):
        if kw.get("x"):
            self.velocity[0]=kw.get("x")
        if kw.get("y"):
            self.velocity[1]=kw.get("y")
        if kw.get("velocity"):
            self.velocity=np.array(kw.get("velocity"))

class WorldBox:
    def __init__(self, gravity):
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
