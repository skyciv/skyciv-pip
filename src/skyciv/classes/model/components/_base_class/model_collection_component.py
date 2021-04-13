from skyciv.utils.helpers import clone, keyvals


class ModelCollectionComponent:
    """The base class for model collection components.
    """

    def get(self, id: int = None) -> dict:
        """Get the data for a single element or all elements.

        Args:
            id (int, optional): The ID of the element to retrieve. Defaults to None.

        Returns:
            dict: All elements unless an element ID is provided.
        """
        data = {}

        if id is not None:
            if self.hasattr(id):
                setattr(data, id, clone(self[id]))
        else:

            # Trigger get on each single class
            for k, v in keyvals(self):
                data[k] = v.__dict__

        return data

    def exists(self, id: int) -> bool:
        """Check if an element exists.

        Args:
            id (int): The ID of the element to check for.

        Returns:
            bool: Whether the element exists.
        """
        if self.hasattr(id):
            return True
        else:
            return False

    def length(self) -> int:
        """Get the amount of elements in the collection.

        Returns:
            int: The amount of elements in the collection.
        """
        element_ids = self.__dict__.keys()
        return len(element_ids)

    def clear(self, id: int) -> None:
        """Remove an element.

        Args:
            id (int): The element ID to delete.
        """
        if self.hasattr(id):
            del self[id]

    def clear_all(self) -> None:
        """Remove all elements.
        """
        for key in self.__dict__.keys():
            del self[key]

    def __getitem__(self, item):
        return getattr(self, item)
