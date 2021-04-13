from skyciv.classes.model.components._base_class.model_collection_component import ModelCollectionComponent
from skyciv.classes.model.components.load_combinations.load_combination import LoadCombination
from skyciv.utils.helpers import next_object_key


class LoadCombinations(ModelCollectionComponent):
    """Creates an instance of the SkyCiv LoadCombinations class.
    """

    def add(self, name: str, combination_factors: dict) -> int:
        """Adds a new load combination.

        Args:
            name (str): The name of the load combination.
            combination_factors (dict): Key value pairs for the factors to apply to the load groups.

        Returns:
            int: The ID of the created load combination.

        Example::

            lcs = LoadCombinations()

            factors = {
                "SW": 1,
                "windCase": 1,
                "liveLoad": 1.5
            }

            lcs.add("LC1", factors)
        """
        next_index = next_object_key(self)

        lc = LoadCombination(name, combination_factors)
        setattr(self, str(next_index), lc)

        return next_index
