from skyciv.classes.model.components.settings.units import Units
from skyciv.utils.helpers import clone

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class Settings:
    def __init__(self,
                 unit_system: Literal["metric", "imperial"],
                 vertical_axis: Literal["Y", "Z"] = 'Y'
                 ) -> None:
        """Create a settings object using the default values.

        Args:
            unit_system (str): {'metric' | 'imperial'}
            vertical_axis (str, optional): The global vertical axis. Defaults to 'Y'.
        """
        self.units = Units(unit_system)
        self.precision = 'fixed'
        self.precision_values = 3
        self.evaluation_points = 9
        self.vertical_axis = vertical_axis
        self.solver_timeout = 600
        self.accurate_buckling_shape = False
        self.buckling_johnson = False
        self.non_linear_tolerance = '1'
        self.non_linear_theory = 'small'
        self.auto_stabilize_model = False
        self.member_offsets_axis = 'global'

    def set(self, settings_object: dict) -> None:
        """Set individual properties of the settings object.

        Args:
            settings_object (dict): An object of key value pairs.

        Example::

            settings = SettingsObject()
            settings.set({
                "vertical_axis": "Z",
                "auto_stabilize_model": True
            })
        """
        for k, v in vars(settings_object).items():
            if self.hasattr(k):
                self[k] = v

    def get(self) -> None:
        """Get the settings object as a Python dictionary.
        """
        settings = clone(vars(self))
        settings["units"] = settings["units"].get()
        return settings

    def __getitem__(self, item):
        return getattr(self, item)
