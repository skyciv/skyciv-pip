from skyciv.classes.model.components.point_loads.point_load import PointLoad
from skyciv.utils.helpers import next_object_key
from skyciv.classes.model.components._base_class.model_collection_component import ModelCollectionComponent
from typing import List
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

class PointLoads(ModelCollectionComponent):
    """Creates an instance of the SkyCiv PointLoads class.
    """

    def add(self,
            type: Literal["n", "m"],
            node: int = None,
            member: int = None,
            position: float = None,
            x_mag: float = 0,
            y_mag: float = 0,
            z_mag: float = 0,
            load_group: str = 'LG1'
            ) -> int:
        """Create a point load with the next available ID.

        Args:
            type (str): The type of object to which the load is applied. node, member. {"n" | "m"}.
            node (int, optional): The node ID which the point load is located. If type is "m", provide value None. Defaults to None.
            member (int, optional): The member ID which the point load is located. If type is "n", provide value None. Defaults to None.
            position (float, optional): The percentage from node_A to node_B of the member which the point load is located. E.g. 10 for 10 %. If type is "n", provide value None. Defaults to None.
            x_mag (float, optional): The magnitude of the point load force along the x-axis. Defaults to 0.
            y_mag (float, optional): The magnitude of the point load force along the y-axis. Defaults to 0.
            z_mag (float, optional): The magnitude of the point load force along the z-axis. Defaults to 0.
            load_group (str, optional): The load group to which the point load will be grouped. Defaults to 'LG1'.

        Returns:
            int: The ID of the created point load.
        """
        next_index = next_object_key(self)

        self.verify(next_index, type, node, member)

        pl = PointLoad(
            type,
            node,
            member,
            position,
            x_mag,
            y_mag,
            z_mag,
            load_group
        )
        setattr(self, str(next_index), pl)
        return next_index

    def id_from_element_id(self, type: Literal["n", "m"], element_id: int) -> int:
        """Find a point load's ID from the node ID which it is located.

        Args:
            type (str): The type of object to which the load is applied. node, member. {"n" | "m"}.
            element_id (int): The node or member ID of the point load to find.

        Returns:
            int: The ID of the located point load.
        """

        found_id = None
        elements = []

        for k, v in vars(self).items():
            if v.type == type:
                elements.append(k)

        key = "node"
        if type == "m":
            key = "member"

        for k in elements:
            v = self[k]
            if (v[key] == element_id):
                found_id = k

        return found_id

    def verify(self, loadIndex: int, type: Literal["n", "m"], node: int, member: int):
        """Check if a node or member ID is provided depending on type = "n" | "m".

        Args:
            loadIndex (int): Index of the load to check.
            type (str): Node or member. {"n" | "m"}.
            node (int): Node ID if type="n".
            member (int): Node ID if type="m".
        """
        if (type == 'm' and (not member) and node):
            print(
                f'A member ID was not provided for a point load({loadIndex}) with type="m".')

        if (type == 'n' and (not node)):
            print(
                f'A node ID was not provided for a point load({loadIndex}) with type="n".')
