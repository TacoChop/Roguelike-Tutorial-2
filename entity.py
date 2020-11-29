from typing import Tuple


class Entity:
    '''
    A generic object to represent players, enemies, items, etc.
    '''
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        #Initializer - holds x,y coordinates, char is symbol for entity, color is tuple  representing RGB values
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx: int, dy: int) -> None:
        #Moves entity given amount.
        self.x += dx
        self.y += dy