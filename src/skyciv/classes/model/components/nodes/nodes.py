from skyciv.classes.model.components.nodes.node import Node
from skyciv.utils.helpers import next_object_key
from skyciv.classes.model.components._base_class.model_collection_component import ModelCollectionComponent


class Nodes(ModelCollectionComponent):
    """Creates an instance of the SkyCiv Nodes class.
    """

    def add(self, x: int, y: int, z: int) -> int:
        """Create a node with the next available ID.

        Args:
            x (int): The X coordinate of the node.
            y (int): The Y coordinate of the node.
            z (int): The Z coordinate of the node.

        Returns:
            int: The ID of the created node.
        """
        next_index = next_object_key(self)
        nodeId = self.id_from_coords(x, y, z)

        if (nodeId != None):
            print('Prevented overwriting an existing node with the Nodes.add() method.')
            return nodeId
        else:
            node = Node(x, y, z)
            setattr(self, str(next_index), node)
            return next_index

    def id_from_coords(self, x: int, y: int, z: int) -> int:
        """Find a node's ID from its coordinates.

        Args:
            x (int): The x coordinate of the node whose ID to find.
            y (int): The y coordinate of the node whose ID to find.
            z (int): The z coordinate of the node whose ID to find.

        Returns:
            int: The ID of the found node.
        """
        id = None

        for k, v in vars(self).items():
            if (v.x == x and v.y == y and v.z == z):
                id = k

        return id
