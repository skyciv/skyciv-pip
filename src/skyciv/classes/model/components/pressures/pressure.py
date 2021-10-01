try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class Pressure:
    def __init__(self,
                 plate_id: int = None,
                 axes: Literal["global", "local"] = 'global',
                 x_mag: float = 0,
                 y_mag: float = 0,
                 z_mag: float = 0,
                 load_group: str = None
                 ) -> None:
        """Creates an instance of the SkyCiv Pressure class.

        Args:
            plate_id (int): The plate to which the pressure is applied. Identified by the plate ID.
            axes (str, optional): The axes in which the distributed load will be applied. Defaults to 'global'. {"global" | "local"}.
            x_mag (float, optional): The magnitude of the pressure in the x-direction of the specified axes, in the units of the pressure property of the units object. Defaults to 0.
            y_mag (float, optional): The magnitude of the pressure in the y-direction of the specified axes, in the units of the pressure property of the units object. Defaults to 0.
            z_mag (float, optional): The magnitude of the pressure in the z-direction of the specified axes, in the units of the pressure property of the units object. Defaults to 0.
            load_group (str, optional): The group to which this load belongs. Defaults to None.
        """
        self.plate_id = plate_id
        self.axes = axes
        self.x_mag = x_mag
        self.y_mag = y_mag
        self.z_mag = z_mag
        self.load_group = load_group
