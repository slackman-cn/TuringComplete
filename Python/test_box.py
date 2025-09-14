import pygame
import enum

def init_box():
    box = [ [pygame.Rect(i*50,j*50,50,50) for j in range(4)] for i in range(4) ]
    box_flat = [element for row in box for element in row]
    print(box_flat)
    print(box[0])
    print(box[1])
    print(box[2])
    print(box[3])


class StateEnum(enum.Enum):
    H = '1'
    L = '0'
    DISMISS = 'x'


state = StateEnum.H
print(type(state))
print(state.name)
print(state.value)

state_init = [ [(i,j) for j in range(4)] for i in range(4) ]
print(state_init)