import copy

import tcod

from engine import Engine
import entity_factories
from procgen import generate_dungeon


def main() -> None:

    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    max_monsters_per_room = 2

    #Creates variable that is equal to the tileset load function for tcod.
    #Tells tcod which font to use for the tileset. 32 and 8 refers to amount of columns and rows in png file.
    tileset = tcod.tileset.load_tilesheet(
        'dejavu10x10_gs_tc.png', 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    #Can't use player.spawn method here becasue it relies on GameMap which isn't created
    #until after the player.
    player = copy.deepcopy(entity_factories.player)

    engine = Engine(player=player)

    engine.game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        engine=engine,
    )
    engine.update_fov()

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

            engine.event_handler.handle_events()


if __name__ == '__main__':
    main()