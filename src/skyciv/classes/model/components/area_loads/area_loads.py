from skyciv.classes.model.components._base_class.model_collection_component import ModelCollectionComponent
from skyciv.classes.model.components.area_loads.area_load import AreaLoad
from skyciv.utils.helpers import keyvals, next_object_key
from typing import List

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

class AreaLoads(ModelCollectionComponent):
    """Creates an instance of the SkyCiv AreaLoads class.
    """

    def add(self,
            type: Literal["one_way", "two_way", "column_wind_load", "open_structure"],
            nodes: List[int],
            mag: float,
            direction: Literal["X", "Y", "Z"],
            elevations: str = 0,
            mags: str = 0,
            column_direction: str = None,
            loaded_members_axis: Literal["all", "major"] = None,
            LG: str = None
            ) -> int:
        """Create an area load with the next available ID.

        Args:
            type (str): How the area load should distribute the load. {"one_way" | "two_way" | "column_wind_load" | "open_structure"}.
            nodes (list[int]): The IDs of the nodes which define the area for loading. Specify 3 or 4 values, in sequential order(clockwise or counterclockwise direction).
            mag (float): The magnitude of the load, in the units of pressure.
            direction (str): The direction of the load in the global axes. {"X" | "Y" | "Z"}.
            elevations (str, optional): Relevant only if "type": "column_wind_load". The elevations between which the corresponding pressure magnitudes (see next row in this table) should be applied. This property should have 1 more value than the corresponding pressure magnitudes property. Defaults to 0.
            mags (str, optional): Relevant only if "type": "column_wind_load". The magnitudes of pressures which should be applied between the corresponding elevations(see above row in this table). This property should have 1 less value than the corresponding elevations property. Defaults to 0.
            column_direction (str, optional): Relevant only if "type": "one_way" or "type": "column_wind_load". The span direction of the applied area load. The values must be the IDs of 2 nodes which are in the nodes property. Defaults to None.
            loaded_members_axis (str, optional): Relevant only if "type": "open_structure".Whether to apply the open structure load to all members attaching to the nodes(indicated by all), or to only those members which lie along the global XYZ axes(indicated by major). Defaults to None. {"all" | "major"}.
            LG (str, optional): The load group to which this area load belongs. Defaults to None.

        Returns:
            int: The ID of the new load.
        """

        next_index = next_object_key(self)
        element_ids = self.get_area_load_ids_from_node_ids(nodes)

        if (element_ids != None):
            print('There is more than one area load with the same nodes.')

        al = AreaLoad(
            type,
            nodes,
            mag,
            direction,
            elevations,
            mags,
            column_direction,
            loaded_members_axis,
            LG
        )
        setattr(self, str(next_index), al)

        return next_index

    def get_area_load_ids_from_node_ids(self, nodes: List[int]) -> List[int]:
        """Get the IDs of all area loads that match the provided nodes array. Node order IS considered.

        Args:
            nodes (list[int]): An array of node IDs that define the area load. At least 3 IDs are required.

        Returns:
            list[int]: An array of member IDs or None if none exist.
        """
        ids = []

        for k, v in keyvals(self):
            if v.nodes == nodes:
                ids.append(k)

        if len(ids) == 0:
            ids = None

        return ids
