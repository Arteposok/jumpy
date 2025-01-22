from sys import displayhook

import pygame as pyg
import numpy as np
from artem_physics import *


def main():
    pyg.init()
    screen=pyg.display.set_mode((500,500))
    running=True
    clock=pyg.time.Clock()
    fps=120
    world=WorldBox(np.array((0.,2.)))
    player=Object(pyg.Rect(200,0,100,100),True,np.array([0,0]))
    floor=Object(pyg.Rect(200,200,100,100),False,np.array([0,0]))
    world.add_object(player)
    world.add_object(floor)
    while running:
        for event in pyg.event.get():
            if event.type==pyg.QUIT:
                running=False

        keys=pyg.key.get_pressed()
        if keys[pyg.K_a]:
            player.set_speed(x=-1)
        elif keys[pyg.K_d]:
            player.set_speed(x=1)
        else:
            player.set_speed(x=0)
        screen.fill((0,0,0))
        world.update()
        pyg.draw.rect(screen,(255,255,255), player.rect)
        pyg.draw.rect(screen,(255,5,5), floor.rect)
        pyg.display.flip()
        clock.tick(fps)


if __name__=="__main__":
    main()
    pyg.quit()