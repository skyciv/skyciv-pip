from skyciv.classes.model.components.sections.section import Section
from skyciv.utils.helpers import next_object_key
from skyciv.classes.model.components._base_class.model_collection_component import ModelCollectionComponent
from typing import List


class Sections(ModelCollectionComponent):
    """Creates an instance of the SkyCiv Sections class.
    """

    def add_library_section(self, path: List[str], material_id: int) -> int:
        """Add a section from the SkyCiv section library.

        Args:
            path (list[str]): Provided as an array of 4 strings (see example below). It is the path of the section in the section library, obtained by inspection from within SkyCiv Section Builder or by attaining the library tree via S3D.SB.getLibraryTree.
            material_id (int): The ID of the material that is assigned to the section.

        Returns:
            int: The ID of the new section.

        Example::

            path = ["American", "AISC", "W shapes", "W14x22"]
        """
        next_index = next_object_key(self)
        new_section = Section()
        new_section.load_section_from_library(path, material_id)
        setattr(self, str(next_index), new_section)
        return next_index

    def add_custom_section(self, name: str, material_id: int) -> int:
        """Add a custom section created in SkyCiv section builder.

        Args:
            name (str): The name of a custom shape defined in SkyCiv Section Builder.
            material_id (int): The ID of the material that is assigned to the section.

        Returns:
            int: The ID of the new section.
        """
        next_index = next_object_key(self)
        new_section = Section()
        new_section.load_custom_from_library(name, material_id)
        setattr(self, str(next_index), new_section)
        return next_index

    def ids_from_path(self, path: List[str]) -> List[int]:
        """Get all sections that match a SkyCiv section library path.

        Args:
            path (list[str]): Provided as an array of 4 strings(see example below). It is the path of the section in the section library, obtained by inspection from within SkyCiv Section Builder or by attaining the library tree via S3D.SB.getLibraryTree.

        Returns:
            [type]: A list of IDs that match the input path.

        Example::

            path = ["American", "AISC", "W shapes", "W14x22"]
        """
        ids = []

        for k, v in vars(self).items():
            if (v.path == path):
                ids.append(k)

        if (len(ids) == 0):
            ids = None

        return ids
