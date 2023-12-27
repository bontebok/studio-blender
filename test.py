from typing import Tuple
from functools import partial
from operator import itemgetter
from typing import cast, Callable, Iterable, List, Optional, Sequence, Tuple

__all__ = ("Coordinate3D", "RGBAColor", "Rotation3D")


#: Type alias for simple 3D coordinates
Coordinate3D = Tuple[float, float, float]

#: Type alias for RGBA color tuples used by Blender
RGBAColor = Tuple[float, float, float, float]

#: Type alias for simple 3D rotations
Rotation3D = Tuple[float, float, float]


def filter_drones(positions: Sequence[Coordinate3D]):
    print(positions)


def c(v):
    return True

positions: Sequence[Coordinate3D] = [(1,2,3),(4,5,6)]

num_positions = len (positions)

def _condition(position: Coordinate3D):
    print (position)
    return False

condition = False

conditions:List[bool] = [True] * num_positions

if condition: # Create list of conditions, and count
    conditions = [ condition(position) for position in positions ]


conditons_map:List[int] = range(num_positions)

print(conditions.count(True))




OUTPUT_TYPE_TO_AXIS_SORT_KEY = {
    "GRADIENT_XYZ": (0, 1, 2),
    "GRADIENT_XZY": (0, 2, 1),
    "GRADIENT_YXZ": (1, 0, 2),
    "GRADIENT_YZX": (1, 2, 0),
    "GRADIENT_ZXY": (2, 0, 1),
    "GRADIENT_ZYX": (2, 1, 0),
    "default": (0, 0, 0),
}
"""Axis mapping for the gradient-based output types"""

OUTPUT_TYPE_TO_AXIS_SORT_KEY = {
    key: itemgetter(*value) for key, value in OUTPUT_TYPE_TO_AXIS_SORT_KEY.items()
}

output_type = "GRADIENT_ZXY"

query_axes = (
    OUTPUT_TYPE_TO_AXIS_SORT_KEY.get(output_type)
    or OUTPUT_TYPE_TO_AXIS_SORT_KEY["default"]
)

#sort_key = lambda index: query_axes(positions[index])[0]
sort_key = lambda index: query_axes(positions[index])

print(sort_key(0))