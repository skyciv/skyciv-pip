from typing import Literal


class Plate:
    def __init__(
        self,
        nodes: list[int],
        thickness: float,
        material_id: int,
        rotZ: float = 0,
        type: str = 'mindlin',
        offset: float = 0,
        state: Literal["stress", "strain"] = 'stress',
        is_meshed: bool = False
    ) -> None:
        """Creates an instance of the SkyCiv Plate class.

        Args:
            nodes (list[int]): An array of node IDs that define the plate. At least 3 IDs are required.
            thickness (float): Plate thickness.
            material_id (int): The ID of the material to use for the plate.
            rotZ (float, optional): Rotation about the Z axis. Defaults to 0.
            type (str, optional): Mindlin plates take into account shear deformations based on the Mindlin-Reissner Theory. Defaults to 'mindlin'.
            offset (float, optional): Offset of the plate along its local z-axis. Defaults to 0.
            state (str, optional): Denotes whether the plate is in a state of plane stress or plane strain. Defaults to 'stress'. {"stress" | "strain"}.
            is_meshed (bool, optional): Indicates whether the plate is already meshed. Defaults to False.
        """
        self.nodes = nodes
        self.thickness = thickness
        self.material_id = material_id
        self.rotZ = rotZ
        self.type = type
        self.offset = offset
        self.state = state
        self.is_meshed = is_meshed
