from __future__ import annotations

from typing import TYPE_CHECKING

from components.base_component import BaseComponent
from input_handlers import GameOverEventHandler
from render_order import RenderOrder

if TYPE_CHECKING:
    from entity import Actor


class Fighter(BaseComponent):
    entity: Actor

    def __init__(self, hp: int, defense: int, power: int):
        self.max_hp = hp
        self._hp = hp
        self.defense = defense
        self.power = power

    @property   # Getter - returns hp
    def hp(self) -> int:
        return self._hp

    @hp.setter   # Setter - ensures hp is never set below 0 or above maximum hp
    def hp(self, value: int) -> None:
        self._hp = max(0, min(value, self.max_hp))
        if self._hp == 0 and self.entity.ai:
            self.die()

    def die(self) -> None:
        if self.engine.player is self.entity:
            death_message = '\u001b[38;5;52mYou died!\u001b[0m'
            self.engine.event_handler = GameOverEventHandler(self.engine)
        else:
            death_message = f'{self.entity.name} is dead!'

        self.entity.char = '%'
        self.entity.color = (150, 0, 0)
        self.entity.blocks_movement = False
        self.entity.ai = None
        self.entity.name = f'Remains of {self.entity.name}'
        self.entity.render_order = RenderOrder.CORPSE

        print(death_message)