try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class Material:
    def __init__(
        self,
        name: str = None,
        density: float = None,
        elasticity_modulus: float = None,
        poissons_ratio: float = None,
        yield_strength: float = None,
        ultimate_strength: float = None,
        _class: Literal["steel", "aluminium",
                        "masonry", "concrete", "wood", "other"] = None
    ) -> None:
        """Creates an instance of the SkyCiv Material class.

        Args:
            name (str): The name of the material.
            density (float): The density of the material.
            elasticity_modulus (float): The Modulus of Elasticity of the material.
            poissons_ratio (float): The Poisson's Ratio for the material.
            yield_strength (float): The Yield strength of the material.
            ultimate_strength (float): The Ultimate strength the material.
            _class (str): The type of material. {"steel" | "aluminium" | "masonry" | "concrete" | "wood" | "other"}.
        """
        self.name = name
        self.density = density
        self.elasticity_modulus = elasticity_modulus
        self.poissons_ratio = poissons_ratio
        self.yield_strength = yield_strength
        self.ultimate_strength = ultimate_strength
        self.__setattr__("class", _class)  # Force with __setattr.
