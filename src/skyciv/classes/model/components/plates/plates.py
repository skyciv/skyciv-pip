from skyciv.classes.model.components.plates.plate import Plate
from skyciv.utils.helpers import next_object_key
from skyciv.classes.model.components._base_class.model_collection_component import ModelCollectionComponent
from typing import List
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class Plates(ModelCollectionComponent):
    """Creates an instance of the SkyCiv Plates class.
    """

    def add(self,
            nodes: List[int] = None,
            thickness: float = None,
            material_id: int = None,
            rotZ: float = 0,
            type: str = 'auto',
            offset: float = 0,
            diaphragm: Literal["no", "rigid"] = 'no',
            membrane_thickness: float = None,
            shear_thickness: float = None,
            bending_thickness: float = None,
            state: Literal["stress", "strain"] = 'stress',
            holes: List[int] = None,
            is_meshed: bool = False
            ) -> int:
        """Create a plate with the next available ID.

        Args:
            nodes (list[int], optional): An array of node IDs that define the plate. At least 3 IDs are required. Defaults to None.
            thickness (float, optional): Plate thickness. Defaults to None.
            material_id (int, optional): The ID of the material to use for the plate. Defaults to None.
            rotZ (float, optional): Rotation about the z-axis. Defaults to 0.
            type (str, optional): Auto will consider shear deformation when the plate thickness is sufficient. Defaults to 'auto'.
            offset (float, optional): Offset of the plate along its local z-axis. Defaults to 0.
            diaphragm (Literal[, optional): If the plate is a diaphragm.. Defaults to 'no'.
            membrane_thickness (float, optional): The membrane thickness to be used. Takes the value of thickness if None. Defaults to None.
            shear_thickness (float, optional): The shear thickness to be used. Takes the value of thickness if None. Defaults to None.
            bending_thickness (float, optional): The bending thickness to be used. Takes the value of thickness if None. Defaults to None.
            state (Literal[, optional): Denotes whether the plate is in a state of plane stress or plane strain. Defaults to 'stress'.
            holes (list[int], optional): An array of node IDs. Used to define holes in the plate.. Defaults to None.
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
                   diaphragm,
                   membrane_thickness,
                   shear_thickness,
                   bending_thickness,
                   state,
                   holes,
                   is_meshed,
                   )
        setattr(self, str(next_index), pl)

        return next_index

    def get_plate_ids_from_node_ids(self, nodes: List[int]) -> List[int]:
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
