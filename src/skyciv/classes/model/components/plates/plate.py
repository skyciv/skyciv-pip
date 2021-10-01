from typing import List
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class Plate:
    def __init__(
        self,
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
    ) -> None:
        """Creates an instance of the SkyCiv Plate class.

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
        """
        self.nodes = nodes
        self.thickness = thickness
        self.material_id = material_id
        self.rotZ = rotZ
        self.type = type
        self.offset = offset
        self.diaphragm = diaphragm
        self.membrane_thickness = membrane_thickness
        self.shear_thickness = shear_thickness
        self.bending_thickness = bending_thickness
        self.state = state
        self.holes = holes
        self.is_meshed = is_meshed
