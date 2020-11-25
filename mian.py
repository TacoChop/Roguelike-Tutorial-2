import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

def main() -> None:
    screen_width = 80
    screen_height = 50

    #Variables used to place player in center of screen
    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    #Creates variable that is equal to the tileset load function for tcod.
    #Tells tcod which font to use for the tileset. 32 and 8 refers to amount of columns and rows in png file.
    tileset = tcod.tileset.load_tilesheet(
        'dejavu10x10_gs_tc.png', 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler() #variable to hold data from EventHandler class

    #Creates the game screen
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title='Demo Game',
        vsync=True,
    ) as context: #Creates the console for the game screen. order='F' sets x,y order for numpy to draw 2D arrays
        root_console = tcod.Console(screen_width, screen_height, order='F')

        # Start of game loop
        while True:
            root_console.print(x=player_x, y=player_y, string='@') #draws player @

            context.present(root_console) #Function that updates screen and draws what is contained in root_console.

            root_console.clear()

            for event in tcod.event.wait(): #Waits for input (event) from player

                #Sends event to proper input_handlers method and assigns the returned Action class to the variable.
                action = event_handler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    #Returns whether object (action) is instance of given class (MovementAction).
                    # #If action is MovementAction it changes player x and y.
                    player_x += action.dx
                    player_y += action.dy

                elif isinstance(action, EscapeAction):
                    raise SystemExit()


if __name__ == '__main__':
    main()