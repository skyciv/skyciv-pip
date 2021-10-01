from typing import List


class Section:

    def clear_self(self) -> None:
        """Delete all properties of the section.
        """
        for key in self.__dict__.keys():
            del self[key]

    def load_section_from_library(self, path: List[str], material_id: int) -> None:
        """Set the section from the SkyCiv section library.

        Args:
            path (list[str]): Provided as an array of 4 strings(see example below). It is the path of the section in the section library, obtained by inspection from within SkyCiv Section Builder or by attaining the library tree via S3D.SB.getLibraryTree.
            material_id (int): The ID of the material that is assigned to the section.

        Example::

            path = ["American", "AISC", "W shapes", "W14x22"]
        """
        self.clear_self()
        self.load_section = path
        self.material_id = material_id

    def load_custom_from_library(self, name: str, material_id: int) -> None:
        """Set the section to a custom shape created in SkyCiv section builder.

        Args:
            name (str): The name of a custom shape defined in SkyCiv Section Builder.
            material_id (int): The ID of the material that is assigned to the section.
        """
        self.clear_self()
        self.load_custom = name
        self.material_id = material_id
