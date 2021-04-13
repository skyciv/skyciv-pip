from skyciv.classes.model.components.settlements.settlement import Settlement
from skyciv.utils.helpers import keyvals, next_object_key
from skyciv.classes.model.components._base_class.model_collection_component import ModelCollectionComponent


class Settlements(ModelCollectionComponent):
    """Creates an instance of the SkyCiv Settlements class.
    """

    def add(self,
            node: int,
            tx: float = 0,
            ty: float = 0,
            tz: float = 0,
            rx: float = 0,
            ry: float = 0,
            rz: float = 0
            ) -> int:
        """Create a settlement with the next available ID.

        Args:
            node (int): The ID of the node at which the settlement is applied.
            tx (float, optional): Settlement displacement in the global x-axis. Defaults to None.
            ty (float, optional): Settlement displacement in the global y-axis. Defaults to None.
            tz (float, optional): Settlement displacement in the global z-axis. Defaults to None.
            rx (float, optional): Settlement rotation about the global x-axis. Defaults to None.
            ry (float, optional): Settlement rotation about the global y-axis. Defaults to None.
            rz (float, optional): Settlement rotation about the global z-axis. Defaults to None.

        Returns:
            int: The ID of the created settlement.
        """
        next_index = next_object_key(self)

        settlement = Settlement(node, tx, ty, tz, rx, ry, rz)
        setattr(self, str(next_index), settlement)
        return next_index

    def id_from_node_id(self, node_id: int) -> int:
        """Find a settlement's ID from the node ID which it is located.

        Args:
            node_id (int): The node ID of the settlement to find.

        Returns:
            int: The ID of the located settlement.
        """
        id = None

        for k, v in keyvals(self):
            if (v.node == node_id):
                id = k

        return id
