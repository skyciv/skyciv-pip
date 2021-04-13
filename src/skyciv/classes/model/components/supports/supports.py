from skyciv.classes.model.components.supports.support import Support
from skyciv.utils.helpers import keyvals, next_object_key
from skyciv.classes.model.components._base_class.model_collection_component import ModelCollectionComponent


class Supports(ModelCollectionComponent):
    """Creates an instance of the SkyCiv Supports class.
    """

    def add(self,
            node: int,
            restraint_code: str = 'FFFFFF',
            tx: float = 0,
            ty: float = 0,
            tz: float = 0,
            rx: float = 0,
            ry: float = 0,
            rz: float = 0
            ) -> int:
        """Create a support with the next available ID.

        Args:
            node (int): The ID of the node at which the support is located.
            restraint_code (str, optional): A 6 character restraint code. See docs for restraint code https://skyciv.com/api/v3/docs/s3d-model#restraint-code. Defaults to 'FFFFFF'. Defaults to 'FFFFFF'.
            tx (float, optional): Spring stiffness for translation in the x-axis. Applies only if the restraint code character for translation in x = S. Defaults to 0.
            ty (float, optional): Spring stiffness for translation in the y-axis. Applies only if the restraint code character for translation in y = S. Defaults to 0.
            tz (float, optional): Spring stiffness for translation in the z-axis. Applies only if the restraint code character for translation in z = S. Defaults to 0.
            rx (float, optional): Spring stiffness for rotation about the x-axis. Applies only if the restraint code character for rotation about x = S. Defaults to 0.
            ry (float, optional): Spring stiffness for rotation about the y-axis. Applies only if the restraint code character for rotation about y = S. Defaults to 0.
            rz (float, optional): Spring stiffness for rotation about the z-axis. Applies only if the restraint code character for rotation about z = S. Defaults to 0.

        Returns:
            int: The ID of the created support.
        """

        next_index = next_object_key(self)

        support = Support(node, restraint_code, tx, ty, tz, rx, ry, rz)
        setattr(self, str(next_index), support)
        return next_index

    def id_from_node_id(self, node_id: int) -> int:
        """Find a support's ID from the node ID which it is located.

        Args:
            node_id (int): The node ID of the support to find.

        Returns:
            int: The ID of the located support.
        """
        id = None
        for k, v in keyvals(self):
            if (v.node == node_id):
                id = k

        return id
