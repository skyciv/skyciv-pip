from typing import List

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class AreaLoad:
    def __init__(self,
                 type: Literal["one_way", "two_way",
                               "column_wind_load", "open_structure"] = None,
                 nodes: List[int] = None,
                 mag: float = None,
                 direction: Literal["X", "Y", "Z"] = None,
                 elevations: str = None,
                 mags: str = None,
                 column_direction: str = None,
                 loaded_members_axis: Literal["all", "major"] = None,
                 LG: str = None
                 ) -> None:
        """Creates an instance of the SkyCiv AreaLoad class.

        Args:
            type (str): How the area load should distribute the load. {"one_way" | "two_way" | "column_wind_load" | "open_structure"}.
            nodes (list[int]): The IDs of the nodes which define the area for loading. Specify 3 or 4 values, in sequential order(clockwise or counterclockwise direction).
            mag (float): The magnitude of the load, in the units of pressure.
            direction (str): The direction of the load in the global axes. {"X" | "Y" | "Z"}.
            elevations (str, optional): Relevant only if "type": "column_wind_load". The elevations between which the corresponding pressure magnitudes (see next row in this table) should be applied. This property should have 1 more value than the corresponding pressure magnitudes property. Defaults to None.
            mags (str, optional): Relevant only if "type": "column_wind_load". The magnitudes of pressures which should be applied between the corresponding elevations (see above row in this table). This property should have 1 less value than the corresponding elevations property. Defaults to None.
            column_direction (str, optional): Relevant only if "type": "one_way" or "type": "column_wind_load". The span direction of the applied area load. The values must be the IDs of 2 nodes which are in the nodes property. Defaults to None.
            loaded_members_axis (str, optional): Relevant only if "type": "open_structure".Whether to apply the open structure load to all members attaching to the nodes (indicated by all), or to only those members which lie along the global XYZ axes(indicated by major). Defaults to None. {"all" | "major"}
            LG (str, optional): The load group to which this area load belongs. Defaults to None.
        """

        self.type = type
        self.nodes = nodes
        self.mag = mag
        self.direction = direction
        self.elevations = elevations
        self.mags = mags
        self.column_direction = column_direction
        self.loaded_members_axis = loaded_members_axis
        self.LG = LG
