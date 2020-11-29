import tcod

from engine import Engine
from entity import Entity
from input_handlers import EventHandler
from procgen import generate_dungeon


def main() -> None:

    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    #Creates variable that is equal to the tileset load function for tcod.
    #Tells tcod which font to use for the tileset. 32 and 8 refers to amount of columns and rows in png file.
    tileset = tcod.tileset.load_tilesheet(
        'dejavu10x10_gs_tc.png', 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler() #variable to hold data from EventHandler class

    player = Entity(int(screen_width / 2), int(screen_height / 2), '@', (255,255,255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), '0', (255, 255, 0))
    entities = {npc, player}

    game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        player=player
    )

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

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
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)

if __name__ == '__main__':
    main()