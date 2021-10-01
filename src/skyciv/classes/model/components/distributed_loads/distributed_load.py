try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class DistributedLoad:

    def __init__(
        self,
        member: int = None,
        x_mag_A: int = 0,
        y_mag_A: int = 0,
        z_mag_A: int = 0,
        x_mag_B: int = 0,
        y_mag_B: int = 0,
        z_mag_B: int = 0,
        position_A: int = 0,
        position_B: int = 0,
        load_group: str = None,
        axes: Literal["global", "local"] = 'global'
    ) -> None:
        """Creates an instance of the SkyCiv DistributedLoad class.

        Args:
            member (int): Member to which the distributed load will be applied. Identified by the member ID.
            x_mag_A (int, optional): The magnitude of the load in the x-direction at the starting position A. Defaults to 0.
            y_mag_A (int, optional): The magnitude of the load in the y-direction at the starting position A. Defaults to 0.
            z_mag_A (int, optional): The magnitude of the load in the z-direction at the starting position A. Defaults to 0.
            x_mag_B (int, optional): The magnitude of the load in the x-direction at the finish position B. Defaults to 0.
            y_mag_B (int, optional): The magnitude of the load in the y-direction at the finish position B. Defaults to 0.
            z_mag_B (int, optional): The magnitude of the load in the z-direction at the finish position B. Defaults to 0.
            position_A (int, optional): Position along member where the distributed load starts. Expressed as a percentage. Defaults to 0.
            position_B (int, optional): Position along member where the distributed load ends. Expressed as a percentage. Defaults to 0.
            load_group (str, optional): The load group to which the load belongs. Defaults to None.
            axes (str, optional): The axes in which the distributed load will be applied. Defaults to 'global'. {"global" | "local"}.
        """
        self.member = member
        self.x_mag_A = x_mag_A
        self.y_mag_A = y_mag_A
        self.z_mag_A = z_mag_A
        self.x_mag_B = x_mag_B
        self.y_mag_B = y_mag_B
        self.z_mag_B = z_mag_B
        self.position_A = position_A
        self.position_B = position_B
        self.load_group = load_group
        self.axes = axes
