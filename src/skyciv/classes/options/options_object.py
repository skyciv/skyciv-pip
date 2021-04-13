from skyciv.utils.helpers import clone


class OptionsObject:

    def __init__(self, validate_input: bool = True, response_data_only: bool = False) -> None:
        """Creates an instance of the SkyCiv OptionsObject class.

        Args:
            validate_input (bool, optional): Verify the model input with SkyCiv's built in model validator. Defaults to True.
            response_data_only (bool, optional): Only respond with data from the last function specified in the functions array. Defaults to False.
        """
        self.validate_input = validate_input
        self.response_data_only = response_data_only

    def get(self):
        return clone(self.__dict__)
