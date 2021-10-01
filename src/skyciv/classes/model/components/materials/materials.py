from skyciv.classes.model.components._base_class.model_collection_component import ModelCollectionComponent
from skyciv.classes.model.components.materials.default_materials import default_materials
from skyciv.classes.model.components.materials.material import Material
from skyciv.utils.helpers import next_object_key

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


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
                                    "Glass"], unit_system: str = "metric") -> int:
        """Add a default material to the model.

        Args:
            material (str): The material name. {"Structural Steel" | "Aluminium" | "Carbon Fibre Reinforced Plastic" | "Concrete" | "Concrete High Strength" | "Oakwood" | "Glass"}.
            unit_system (str): {'metric' | 'imperial'}

        Returns:
            int: The ID of the created material.
        """

        materials = default_materials[unit_system][material]

        name = materials["name"]
        density = materials["density"]
        elasticity_modulus = materials["elasticity_modulus"]
        poissons_ratio = materials["poissons_ratio"]
        yield_strength = materials["yield_strength"]
        ultimate_strength = materials["ultimate_strength"]
        _class = materials["class"]

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
