class MeshedPlate:
    def __init__(self,
                 parent_plate: int = None,
                 node_A: int = None,
                 node_B: int = None,
                 node_C: int = None,
                 node_D: int = None,
                 rotZ: float = 0
                 ) -> None:
        """Creates an instance of the SkyCiv MeshedPlate class.

        Args:
            parent_plate (int): The ID of the plate which this meshed plate originated from. Must refer to a plate in the plates object.
            node_A (int): The first node of the meshed plate.
            node_B (int): The second node of the meshed plate.
            node_C (int): The third node of the meshed plate.
            node_D (int, optional): The fourth node of the meshed plate. Set this to None if the meshed plate is triangular. Defaults to None.
            rotZ (float, optional): Rotation of this plate about the plate's local z-axis, in degrees. Defaults to 0.
        """
        self.parent_plate = parent_plate
        self.node_A = node_A
        self.node_B = node_B
        self.node_C = node_C
        self.node_D = node_D
        self.rotZ = rotZ
