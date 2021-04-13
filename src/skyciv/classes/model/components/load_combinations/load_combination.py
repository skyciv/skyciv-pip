from skyciv.classes.model.components._base_class.model_collection_component import ModelCollectionComponent


class LoadCombination(ModelCollectionComponent):

    def __init__(self, name: str = None, combination_factors: dict = None) -> None:
        """Creates an instance of the SkyCiv LoadCombination class.

        Args:
            name (str): The name of the load combination.
            combination_factors (dict): Key value pairs for the factors to apply to the load groups.
        """
        self.set(name, combination_factors)

    def set(self, name: str, combination_factors: dict) -> None:
        """Set individual properties of the LoadCombination object.

        Args:
            name (str): The name of the load combination.
            combination_factors (dict): An object of key value pairs specifying the load group factor.

        Raises:
            Exception: If a combination factor key is "name" as this is reserved.

        Example::

            lc = LoadCombination()

            factors = {
                "SW": 1,
                "windCase": 1,
                "liveLoad": 1.5
            }

            lc.clear_all() # To remove any existing factors.
            lc.set("LC1", factors)
        """
        self.name = name

        if not combination_factors == None:
            for k, v in combination_factors.items():
                if k == "name":
                    raise Exception(
                        "A load combination can not have the name 'name' as this is a reserved keyword.")
                else:
                    setattr(self, str(k), v)
