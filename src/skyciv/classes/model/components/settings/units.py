from skyciv.utils.helpers import clone
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class Units:
    def __init__(self, unit_system: Literal["metric", "imperial"], units_object: dict = None) -> None:
        """Create a units object using the default value for Metric or Imperial.

        Args:
            unit_system (str): {'metric' | 'imperial'}
            units_object (dict, optional): A dictionary of key, value pairs to set individual unit properties. Defaults to None.

        Example:
            Default values for metric | imperial::

            {
                "length": "m" | 'ft',
                "section_length": "mm" | 'in',
                "material_strength": "mpa" | 'ksi',
                "density": "kg/m3" | 'lb/ft3',
                "force": "kn" | 'kip',
                "moment": "kn-m" | 'kip-ft',
                "pressure": "kpa" | 'ksf',
                "mass": "kg" | 'kip',
                "translation": "mm" | 'in',
                "stress": "mpa" | 'ksi'
            }
        """
        self.length = None
        self.section_length = None
        self.material_strength = None
        self.density = None
        self.force = None
        self.moment = None
        self.pressure = None
        self.mass = None
        self.translation = None
        self.stress = None

        self.set_unit_system(unit_system)

        if (units_object):
            self.set(units_object)

    def set_unit_system(self, unit_system: Literal["metric", "imperial"]):
        """Set the units object using the default values for Metric or Imperial.

        Args:
            unit_system (str): {'metric' | 'imperial'}

        Example:
            Default values for metric | imperial::

            {
                "length": "m" | 'ft',
                "section_length": "mm" | 'in',
                "material_strength": "mpa" | 'ksi',
                "density": "kg/m3" | 'lb/ft3',
                "force": "kn" | 'kip',
                "moment": "kn-m" | 'kip-ft',
                "pressure": "kpa" | 'ksf',
                "mass": "kg" | 'kip',
                "translation": "mm" | 'in',
                "stress": "mpa" | 'ksi'
            }
        """
        if unit_system == 'metric':
            self.set_default_metric()
        else:
            self.set_default_imperial()

    def set_default_metric(self):
        """Set the unit system to the default metric values.

        Example::

            {
                "length": "m",
                "section_length": "mm",
                "material_strength": "mpa",
                "density": "kg/m3",
                "force": "kn",
                "moment": "kn-m",
                "pressure": "kpa",
                "mass": "kg",
                "translation": "mm",
                "stress": "mpa"
            }
        """
        self.length = 'm'
        self.section_length = 'mm'
        self.material_strength = 'mpa'
        self.density = 'kg/m3'
        self.force = 'kn'
        self.moment = 'kn-m'
        self.pressure = 'kpa'
        self.mass = 'kg'
        self.translation = 'mm'
        self.stress = 'mpa'

    def set_default_imperial(self):
        """Set the unit system to the default imperial values.

        Example::

            {
                length: 'ft',
                section_length: 'in',
                material_strength: 'ksi',
                density: 'lb/ft3',
                force: 'kip',
                moment: 'kip-ft',
                pressure: 'ksf',
                mass: 'kip',
                translation: 'in',
                stress: 'ksi',
            }
        """
        self.length = 'ft'
        self.section_length = 'in'
        self.material_strength = 'ksi'
        self.density = 'lb/ft3'
        self.force = 'kip'
        self.moment = 'kip-ft'
        self.pressure = 'ksf'
        self.mass = 'kip'
        self.translation = 'in'
        self.stress = 'ksi'

    def set(self, units_object: dict):
        """Set individual properties of the units object. Imperial and Metric MUST NOT be mixed.

        Args:
            units_object (dict): An object of key value pairs.

        Example::

            units_obj = Units("metric")
            units_obj.set({
                "length": "m",
                "pressure": "mpa"
            })
        """
        for k, v in vars(units_object).items():
            if (self.hasattr(k)):
                self[k] = v

    def get(self) -> None:
        """Get the units object as a Python dictionary.
        """
        return clone(vars(self))

    def get_unit_system(self) -> str:
        """Determines the unit system based on the length units.

        Returns:
            str: The unit system.
        """
        if (self.length in ['m', 'mm']):
            return 'metric'
        else:
            return 'imperial'

    def __getitem__(self, item):
        return getattr(self, item)
