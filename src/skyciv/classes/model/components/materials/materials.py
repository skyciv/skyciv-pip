from typing import Literal
from classes.model.components._base_class.model_collection_component import ModelCollectionComponent
from classes.model.components.materials.default_materials import default_materials
from classes.model.components.materials.material import Material
from utils.helpers import next_object_key


class Materials(ModelCollectionComponent):
    """Creates an instance of the SkyCiv Materials class.
    """

    def add_custom(
        self,
        name: str,
        density: float,
        elasticity_modulus: float,
        poissons_ratio: float,
        yield_strength: float,
        ultimate_strength: float,
        _class: Literal["steel", "aluminium",
                        "masonry", "concrete", "wood", "other"]
    ) -> int:
        """Create a custom material with the next available ID.

        Args:
            name (str): The name of the material.
            density (float): The density of the material.
            elasticity_modulus (float): The Modulus of Elasticity of the material.
            poissons_ratio (float): The Poisson's Ratio for the material.
            yield_strength (float): The Yield strength of the material.
            ultimate_strength (float): The Ultimate strength the material.
            _class (str): The type of material. {"steel" | "aluminium" | "masonry" | "concrete" | "wood" | "other"}.

        Returns:
            int: The ID of the created material.
        """

        next_index = next_object_key(self)

        material = Material(
            name,
            density,
            elasticity_modulus,
            poissons_ratio,
            yield_strength,
            ultimate_strength,
            _class
        )
        setattr(self, str(next_index), material)
        return next_index

    def add(self, material: Literal["Structural Steel",
                                    "Aluminium",
                                    "Carbon Fibre Reinforced Plastic",
                                    "Concrete",
                                    "Concrete High Strength",
                                    "Oakwood",
                                    "Glass"]) -> int:
        """Add a default material to the model.

        Args:
            material (str): The material name. {"Structural Steel" | "Aluminium" | "Carbon Fibre Reinforced Plastic" | "Concrete" | "Concrete High Strength" | "Oakwood" | "Glass"}.

        Returns:
            int: The ID of the created material.
        """
        name = default_materials[material]["name"]
        density = default_materials[material]["density"]
        elasticity_modulus = default_materials[material]["elasticity_modulus"]
        poissons_ratio = default_materials[material]["poissons_ratio"]
        yield_strength = default_materials[material]["yield_strength"]
        ultimate_strength = default_materials[material]["ultimate_strength"]
        _class = default_materials[material]["class"]

        index = self.add_custom(
            name,
            density,
            elasticity_modulus,
            poissons_ratio,
            yield_strength,
            ultimate_strength,
            _class
        )

        return index
