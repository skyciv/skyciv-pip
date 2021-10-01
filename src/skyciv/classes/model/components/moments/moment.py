try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

class Moment:

    def __init__(
        self,
        type: Literal["n", "m"] = None,
        node: int = None,
        member: int = None,
        position: float = None,
        x_mag: float = 0,
        y_mag: float = 0,
        z_mag: float = 0,
        load_group: str = None
    ) -> None:
        """Creates an instance of the SkyCiv Moment class

        Args:
            type (str): The type of object to which the load is applied. node, member. {"n" | "m"}.
            node (int, optional): The node ID which the moment is located. If type is "m", provide value None. Defaults to None.
            member (int, optional): The member ID which the moment is located. If type is "n", provide value None. Defaults to None.
            position (float, optional): The percentage from node_A to node_B of the member which the moment is located. E.g. 10 for 10 %. If type is "n", provide value None. Defaults to None.
            x_mag (float, optional): The magnitude of the moment about the x-axis. Positive = counter-clockwise, negative = clockwise. Defaults to 0.
            y_mag (float, optional): The magnitude of the moment about the y-axis. Positive = counter-clockwise, negative = clockwise. Defaults to 0.
            z_mag (float, optional): The magnitude of the moment about the z-axis. Positive = counter-clockwise, negative = clockwise. Defaults to 0.
            load_group (str, optional): The load group to which the moment will be grouped. Defaults to None.

        Example::

            node_load = Moment('n', 1, None, None, 0, -5.3, 0, "LG1")
            member_load = Moment('m', None, 3, 32.4, 0, -5.3, 0, "LG1")
        """
        self.type = type
        self.node = node
        self.member = member
        self.position = position
        self.x_mag = x_mag
        self.y_mag = y_mag
        self.z_mag = z_mag
        self.load_group = load_group
