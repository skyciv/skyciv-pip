from skyciv.classes.model.components.moments.moment import Moment
from skyciv.utils.helpers import next_object_key
from skyciv.classes.model.components._base_class.model_collection_component import ModelCollectionComponent
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

class Moments(ModelCollectionComponent):
    """Creates an instance of the SkyCiv Moments class.
    """

    def add(self,
            type: Literal["n", "m"],
            node: int = None,
            member: int = None,
            position: float = None,
            x_mag: float = 0,
            y_mag: float = 0,
            z_mag: float = 0,
            load_group: str = None
            ) -> int:
        """Create a moment with the next available ID.

        Args:
            type (str): The type of object to which the load is applied. node, member. {"n" | "m"}.
            node (int, optional): The node ID which the moment is located. If type is "m", provide value None. Defaults to None.
            member (int, optional): The member ID which the moment is located. If type is "n", provide value None. Defaults to None.
            position (float, optional): The percentage from node_A to node_B of the member which the moment is located. E.g. 10 for 10 %. If type is "n", provide value None. Defaults to None.
            x_mag (float, optional): The magnitude of the moment about the x-axis. Positive = counter-clockwise, negative = clockwise. Defaults to 0.
            y_mag (float, optional): The magnitude of the moment about the y-axis. Positive = counter-clockwise, negative = clockwise. Defaults to 0.
            z_mag (float, optional): The magnitude of the moment about the z-axis. Positive = counter-clockwise, negative = clockwise. Defaults to 0.
            load_group (str, optional): The load group to which the moment will be grouped. Defaults to None.

        Returns:
            int: The ID of the created moment.
        """

        next_index = next_object_key(self)

        moment = Moment(type, node, member, position,
                        x_mag, y_mag, z_mag, load_group)
        setattr(self, str(next_index), moment)
        return next_index

    def id_from_element_id(self, type: Literal["n", "m"], element_id: int) -> int:
        """Find a moment's ID from the node ID which it is located.

        Args:
            type (str): The type of object to which the load is applied. node, member. {"n" | "m"}.
            element_id (int): The node or member ID of the moment to find.

        Returns:
            int: The ID of the found moment.
        """
        found_id = None

        elements = []

        for k, v in vars(self).items():
            if v.type == type:
                elements.append(k)

        key = "node"
        if type == "m":
            key = 'member'

        for k in elements:
            v = self[k]
            if v[key] == element_id:
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
                f'A member ID was not provided for a moment({loadIndex}) with type="m".')

        if (type == 'n' and (not node)):
            print(
                f'A node ID was not provided for a moment({loadIndex}) with type="n".')
