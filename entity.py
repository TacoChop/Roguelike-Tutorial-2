from __future__ import annotations

import copy
from typing import Optional, Tuple, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from game_map import GameMap

T = TypeVar('T', bound='Entity') #Binds T to whatever type Entity is? I guess?


class Entity:
    '''
    A generic object to represent players, enemies, items, etc.
    '''

    gamemap: GameMap

    def __init__(
        self,
        gamemap: Optional[GameMap] = None,
        x: int = 0,
        y: int = 0,
        char: str = '?',
        color: Tuple[int, int, int] = (255, 255, 255),
        name: str = '<Unnamed>',
        blocks_movement: bool = False,
    ):
        #Initializer - holds x,y coordinates, char is symbol for entity,
        #color is tuple representing RGB values. Also provides defaults for all variables.
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks_movement = blocks_movement
        if gamemap:
            #If gamemap isn't provided now then it will be set later.
            self.gamemap = gamemap
            gamemap.entities.add(self)

    def spawn(self: T, gamemap: GameMap, x: int, y: int) -> T:
        '''Spawn a copy of this instance at the given location.'''
        #Creates a clone of the entity instance contained in entity_factories
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        clone.gamemap = gamemap
        #Adds the clone to the entities method for gamemap so it can be placed
        gamemap.entities.add(clone)
        return clone

    def place(self, x: int, y: int, gamemap: Optional[GameMap] = None) -> None:
        '''Place this entity at a new location. Handles moving across GameMaps.'''
        self.x = x
        self.y = y
        if gamemap:
            if  hasattr(self, 'gamemap'): #Possibly uninitialized.
                self.gamemap.entities.remove(self)
            self.gamemap = gamemap
            gamemap.entities.add(self)

    def move(self, dx: int, dy: int) -> None:
        #Moves entity given amount.
        self.x += dx
        self.y += dy