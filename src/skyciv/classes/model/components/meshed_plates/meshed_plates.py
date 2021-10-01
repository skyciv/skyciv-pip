from skyciv.classes.model.components.meshed_plates.meshed_plate import MeshedPlate
from skyciv.utils.helpers import next_object_key
from skyciv.classes.model.components._base_class.model_collection_component import ModelCollectionComponent
from typing import List

class MeshedPlates(ModelCollectionComponent):
    """Creates an instance of the SkyCiv MeshedPlates class.
    """

    def add(self, parent_plate: int, node_A: int, node_B: int, node_C: int, node_D: int = None, rotZ: float = 0) -> int:
        """Create a meshed plate with the next available ID.

        Args:
            parent_plate (int): The ID of the plate which this meshed plate originated from. Must refer to a plate in the plates object.
            node_A (int): The first node of the meshed plate.
            node_B (int): The second node of the meshed plate.
            node_C (int): The third node of the meshed plate.
            node_D (int, optional): The fourth node of the meshed plate. Set this to None if the meshed plate is triangular. Defaults to None.
            rotZ (float, optional): Rotation of this plate about the plate's local z-axis, in degrees. Defaults to 0.

        Returns:
            int: The ID of the new meshed plate element.
        """
        next_index = next_object_key(self)
        element_ids = self.get_meshed_plate_ids_from_nodes_ids(
            node_A, node_B, node_C, node_D)

        if (element_ids != None):
            print('There is more than one meshed plate with the same nodes.')

        mp = MeshedPlate(parent_plate, node_A, node_B, node_C, node_D, rotZ)
        setattr(self, str(next_index), mp)
        return next_index

    def get_meshed_plate_ids_from_nodes_ids(self, node_A: int, node_B: int, node_C: int, node_D: int = None) -> List[int]:
        """Get the IDs of all meshed plates by corner nodes.

        Args:
            node_A (int): The ID of Node A.
            node_B (int): The ID of Node B.
            node_C (int): The ID of Node C.
            node_D (int, optional): The ID of Node D. Defaults to None.

        Returns:
            list[int]: An array of meshed plate IDs or None if none exist.
        """
        ids = []

        for k, v in vars(self).items():
            if (
                v.node_A == node_A and
                v.node_B == node_B and
                v.node_C == node_C and
                v.node_D == node_D
            ):
                ids.append(k)

        if len(ids) == 0:
            ids = None

        return ids
