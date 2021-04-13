from skyciv.classes.model.components._base_class.model_collection_component import ModelCollectionComponent
from skyciv.classes.model.components.distributed_loads.distributed_load import DistributedLoad
from skyciv.utils.helpers import next_object_key


class DistributedLoads(ModelCollectionComponent):
    """Creates an instance of the SkyCiv DistributedLoads class.
    """

    def add(
        self,
        member: int,
        x_mag_A: float = 0,
        y_mag_A: float = 0,
        z_mag_A: float = 0,
        x_mag_B: float = 0,
        y_mag_B: float = 0,
        z_mag_B: float = 0,
        position_A: float = 0,
        position_B: float = 0,
        load_group: str = None,
        axes: str = 'global'
    ) -> int:
        """Create a distributed load with the next available ID.

        Args:
            member (int): Member to which the distributed load will be applied. Identified by the member ID.
            x_mag_A (float, optional): The magnitude of the load in the x-direction at the starting position A. Defaults to 0.
            y_mag_A (float, optional): The magnitude of the load in the y-direction at the starting position A. Defaults to 0.
            z_mag_A (float, optional): The magnitude of the load in the z-direction at the starting position A. Defaults to 0.
            x_mag_B (float, optional): The magnitude of the load in the x-direction at the finish position B. Defaults to 0.
            y_mag_B (float, optional): The magnitude of the load in the y-direction at the finish position B. Defaults to 0.
            z_mag_B (float, optional): The magnitude of the load in the z-direction at the finish position B. Defaults to 0.
            position_A (float, optional): Position along member where the distributed load starts. Expressed as a percentage. Defaults to 0.
            position_B (float, optional): Position along member where the distributed load ends. Expressed as a percentage. Defaults to 0.
            load_group (str, optional): The load group to which the load belongs. Defaults to None.
            axes (str, optional): The axes in which the distributed load will be applied. Defaults to 'global'.

        Returns:
            int: The ID of the created load.
        """

        next_index = next_object_key(self)

        dl = DistributedLoad(
            member,
            x_mag_A,
            y_mag_A,
            z_mag_A,
            x_mag_B,
            y_mag_B,
            z_mag_B,
            position_A,
            position_B,
            load_group,
            axes
        )
        setattr(self, str(next_index), dl)

        return next_index

    def id_from_member_id(self, element_id: int) -> int:
        """Find a distributed load's ID from the member ID which it is located.

        Args:
            element_id (int): The member ID of the distributed load to find.

        Returns:
            int: The distributed load ID which is located at the provided member ID.
        """
        found_id = None

        for k, v in vars(self).items():

            if (v.member == element_id):
                found_id = k

        return found_id
