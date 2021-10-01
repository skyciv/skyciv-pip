from skyciv.classes.model.components.pressures.pressure import Pressure
from skyciv.utils.helpers import next_object_key
from skyciv.classes.model.components._base_class.model_collection_component import ModelCollectionComponent

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class Pressures(ModelCollectionComponent):
    """Creates an instance of the SkyCiv Pressures class.
    """

    def add(self,
            plate_id: int,
            axes: Literal["global", "local"] = 'global',
            x_mag: float = 0,
            y_mag: float = 0,
            z_mag: float = 0,
            load_group: str = None
            ) -> int:
        """Create a pressure with the next available ID.

        Args:
            plate_id (int): The plate to which the pressure is applied. Identified by the plate ID.
            axes (str, optional): The axes in which the distributed load will be applied. Defaults to 'global'. {"global" | "local"}.
            x_mag (float, optional): The magnitude of the pressure in the x-direction of the specified axes, in the units of the pressure property of the units object. Defaults to 0.
            y_mag (float, optional): The magnitude of the pressure in the y-direction of the specified axes, in the units of the pressure property of the units object. Defaults to 0.
            z_mag (float, optional): The magnitude of the pressure in the z-direction of the specified axes, in the units of the pressure property of the units object. Defaults to 0.
            load_group (str, optional): The group to which this load belongs. Defaults to None.

        Returns:
            int: The ID of the created pressure.
        """
        next_index = next_object_key(self)

        pressure = Pressure(plate_id,
                            axes,
                            x_mag,
                            y_mag,
                            z_mag,
                            load_group
                            )
        setattr(self, str(next_index), pressure)
        return next_index

    def id_from_plate_id(self, plate_id: int) -> int:
        """Find a pressure's ID from the plate ID which it is located.

        Args:
            plate_id (int): The plate ID of the pressure to find.

        Returns:
            int: The IF of the located pressure.
        """
        found_id = None

        for k, v in vars(self).items():
            if (v["plate_id"] == plate_id):
                found_id = k

        return found_id
