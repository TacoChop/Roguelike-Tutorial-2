from typing import Optional

import tcod.event

from actions import Action, EscapeAction, MovementAction

#Subclass of tcod EventDispatch class. Passes data to Action subclass based on which key is pressed.
class EventHandler(tcod.event.EventDispatch[Action]):

    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None #Holds Action subclass that is assigned by key press. invalid key returns None.

        key = event.sym #holds the actual key press

        if key == tcod.event.K_UP:
            action = MovementAction(dx=0, dy=-1) #dx & dy values determine direction and distance moved
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(dx=1, dy=0)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        #No valid key was pressed
        return action