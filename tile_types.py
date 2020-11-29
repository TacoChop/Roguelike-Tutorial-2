from typing import Tuple

import numpy as np # type: ignore

#Tile graphics structured type compatible with Console.tiles_rgb.
graphic_dt = np.dtype( #Creates data type for Numpy
    [
        ('ch', np.int32), #Unicode codepoint.
        ('fg', '3B'),   #3 unsigned bytes, for RGB colors.
        ('bg', '3B'),
    ]
)

#Tile struct used for statically defined tile data.
tile_dt = np.dtype(
    [
        ('walkable', np.bool), #True if this tile can be walked over
        ('transparent', np.bool), #True if this tile doesn't block FOV
        ('dark', graphic_dt), #Graphics for when this tile is not in FOV
    ]
)

def new_tile(
        *, #Enforce the use of keywords, so that parameter order doesn't matter
        walkable: int,
        transpaernet: int,
        dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    '''Helper function for defining individual tile types'''
    return np.array((walkable, transpaernet, dark), dtype=tile_dt)

floor = new_tile(
    walkable=True, transpaernet=True, dark=(ord('.'), (48, 48, 48), (107, 108, 110)), #ord is character representing tile, then foreground color, then background color
)
wall = new_tile(
    walkable=False, transpaernet=False, dark=(ord(' '), (138, 138, 145), (10, 12, 36)),
)