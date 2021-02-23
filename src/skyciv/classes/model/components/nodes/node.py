class Node:

    def __init__(self, x: float = None, y: float = None, z: float = None) -> None:
        """Creates an instance of the SkyCiv Node class.

        Args:
            x (float): The X coordinate of the node.
            y (float): The Y coordinate of the node.
            z (float): The Z coordinate of the node.
        """
        self.x = x
        self.y = y
        self.z = z
