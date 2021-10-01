try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class PointLoad:
    def __init__(
        self,
        type: Literal["n", "m"] = None,
        node: int = None,
        member: int = None,
        position: float = None,
        x_mag: float = 0,
        y_mag: float = 0,
        z_mag: float = 0,
        load_group: str = "LG1"
    ) -> None:
        """Creates an instance of the SkyCiv PointLoad class.

        Args:
            type (str): The type of object to which the load is applied. node, member. {"n" | "m"}
            node (int, optional): The node ID which the point load is located. If type is "m", provide value None. Defaults to None.
            member (int, optional): The member ID which the point load is located. If type is "n", provide value None. Defaults to None.
            position (float, optional): The percentage from node_A to node_B of the member which the point load is located. E.g. 10 for 10 % .  If type is "n", provide value None. Defaults to None.
            x_mag (float, optional): The magnitude of the point load force along the x-axis. Defaults to 0.
            y_mag (float, optional): The magnitude of the point load force along the y-axis. Defaults to 0.
            z_mag (float, optional): The magnitude of the point load force along the z-axis. Defaults to 0.
            load_group (str, optional): The load group to which the point load will be grouped. Defaults to "LG1".
        """

        self.type = type

        if node != None:
            self.node = node

        if member != None:
            self.member = member

        self.position = position
        self.x_mag = x_mag
        self.y_mag = y_mag
        self.z_mag = z_mag
        self.load_group = load_group
