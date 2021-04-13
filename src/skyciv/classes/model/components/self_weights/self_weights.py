from skyciv.classes.model.components.self_weights.self_weight import SelfWeight
from skyciv.utils.helpers import next_object_key
from skyciv.classes.model.components._base_class.model_collection_component import ModelCollectionComponent


class SelfWeights(ModelCollectionComponent):
    """Creates an instance of the SkyCiv SelfWeights class.
    """

    def add(self, enabled: bool = True, x: int = 0, y: int = 0, z: int = 0, LG: str = 'SW1') -> int:
        """Add an instance of self-weight.

        Args:
            enabled (bool, optional): Defaults to True.
            x (int, optional): Acceleration due to gravity in the x-axis, defined as a multiplier of the gravitational constant g. Defaults to 0.
            y (int, optional): Acceleration due to gravity in the y-axis, defined as a multiplier of the gravitational constant g. Defaults to 0.
            z (int, optional): Acceleration due to gravity in the z-axis, defined as a multiplier of the gravitational constant g. Defaults to 0.
            LG (str, optional): The load group that the self-weight belongs to. Defaults to existing value. Defaults to 'SW1'.

        Example:
            For a simple model where +Y on the global axis is vertical,
            the following will apply [1 ✕ gravity] for the model self-weight::

            sws = SelfWeights()
            sws.add(y=-1, LG="SW1")

        Returns:
            int: The ID of the newly created self-weight.
        """
        next_index = next_object_key(self)
        new_self_weight = SelfWeight(enabled, x, y, z, LG)
        setattr(self, str(next_index), new_self_weight)
        return next_index

    def disable(self, id: int = 1) -> None:
        """Disables an instance of self-weight.

        Args:
            id (int, optional): The ID of the self-weight to disable. Defaults to 1.
        """
        self[id].disable()
