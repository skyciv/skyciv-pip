from classes.model.components.plates.plate import Plate
from utils.helpers import next_object_key
from classes.model.components._base_class.model_collection_component import ModelCollectionComponent


class Plates(ModelCollectionComponent):
    """Creates an instance of the SkyCiv Plates class.
    """

    def add(self,
            nodes: list[int],
            thickness: float,
            material_id: int,
            rotZ: float = 0,
            type: str = 'mindlin',
            offset: float = 0,
            state: str = 'stress',
            is_meshed: bool = False
            ) -> int:
        """Create a plate with the next available ID.

        Args:
            nodes (list[int]): An array of node IDs that define the plate. At least 3 IDs are required.
            thickness (float): Plate thickness.
            material_id (int): The ID of the material to use for the plate.
            rotZ (float, optional): Rotation about the z-axis. Defaults to 0.
            type (str, optional): Mindlin plates take into account shear deformations based on the Mindlin-Reissner Theory. Defaults to 'mindlin'.
            offset (float, optional): Offset of the plate along its local z-axis. Defaults to 0.
            state (str, optional): Denotes whether the plate is in a state of plane stress or plane strain. Defaults to 'stress'.
            is_meshed (bool, optional): Indicates whether the plate is already meshed. Defaults to False.

        Returns:
            int: The ID of the created plate.
        """
        next_index = next_object_key(self)
        element_ids = self.get_plate_ids_from_node_ids(nodes)

        if (element_ids != None):
            print('There is more than one plate with the same nodes.')

        pl = Plate(nodes,
                   thickness,
                   material_id,
                   rotZ,
                   type,
                   offset,
                   state,
                   is_meshed
                   )
        setattr(self, str(next_index), pl)

        return next_index

    def get_plate_ids_from_node_ids(self, nodes: list[int]) -> list[int]:
        """Get the IDs of all plates that match the provided nodes array. Node order IS considered.

        Args:
            nodes (list[int]): An array of node IDs that define the plate. At least 3 IDs are required.

        Returns:
            list[int]: An array of member IDs or None if none exist.
        """
        ids = []

        for k, v in vars(self).items():
            if v.nodes == nodes:
                ids.append(k)

        if len(ids) == 0:
            ids = None

        return ids
