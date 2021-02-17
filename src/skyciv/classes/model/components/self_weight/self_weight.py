from utils.helpers import clone


class SelfWeight:
    def __init__(self,
                 enabled: bool = False,
                 x: float = 0,
                 y: float = 0,
                 z: float = 0
                 ) -> None:
        """Creates an instance of the SkyCiv SelfWeight class.

        Args:
            enabled (bool): If the this weight is applied to the model or not.
            x (float): Acceleration due to gravity in the x axis, defined as a multiplier of the gravitational constant g.
            y (float): Acceleration due to gravity in the y axis, defined as a multiplier of the gravitational constant g.
            z (float): Acceleration due to gravity in the z axis, defined as a multiplier of the gravitational constant g.
        """
        self.enabled = enabled
        self.x = x
        self.y = y
        self.z = z

    def get(self) -> dict:
        """Get the self weight object as a dictionary.

        Returns:
            dict: A SkyCiv formatted S3D SelfWeight as a python dictionary.
        """
        return clone(vars(self))

    def enable(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        """Enables selfweight with provided gravity multipliers.

        Args:
            x (float, optional): Gravity multiplier in the X direction. Defaults to 0.
            y (float, optional): Gravity multiplier in the Y direction. Defaults to 0.
            z (float, optional): Gravity multiplier in the Z direction. Defaults to 0.

        Example:
            For a simple model where +Y on the global axis is vertical,
            the following will apply [1 ✕ gravity] for the model selfweight::

            sw = SelfWeight()
            sw.enable(0, -1, 0)

        """
        self.enabled = True
        self.x = x
        self.y = y
        self.z = z

    def disable(self) -> None:
        """Disable self weight.
        """
        self.enabled = False
