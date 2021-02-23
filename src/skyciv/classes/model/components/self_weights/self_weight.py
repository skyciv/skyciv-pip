
class SelfWeight:
    def __init__(self,
                 enabled: bool = False,
                 x: float = 0,
                 y: float = 0,
                 z: float = 0,
                 LG: str = "SW1"
                 ) -> None:
        """Creates an instance of the SkyCiv SelfWeight class.

        Args:
            enabled (bool): If the this weight is applied to the model or not.
            x (float): Acceleration due to gravity in the x-axis, defined as a multiplier of the gravitational constant g.
            y (float): Acceleration due to gravity in the y-axis, defined as a multiplier of the gravitational constant g.
            z (float): Acceleration due to gravity in the z-axis, defined as a multiplier of the gravitational constant g.
            LG (str, optional): The load group that the self-weight belongs to. Defaults to LG1.
        """
        self.enabled = enabled
        self.x = x
        self.y = y
        self.z = z
        self.LG = LG

    def enable(self, x: float = 0, y: float = 0, z: float = 0, LG: str = "SW1") -> None:
        """Enables self-weight with provided gravity multipliers.

        Args:
            x (float, optional): Gravity multiplier in the x-direction. Defaults to 0.
            y (float, optional): Gravity multiplier in the y-direction. Defaults to 0.
            z (float, optional): Gravity multiplier in the z-direction. Defaults to 0.
            LG (str, optional): The load group that the self-weight belongs to. Defaults to LG1.

        Example:
            For a simple model where +Y on the global axis is vertical,
            the following will apply [1 ✕ gravity] for the model self-weight::

            sw = SelfWeight()
            sw.enable(0, -1, 0, "SW1")

        """
        self.enabled = True
        self.x = x
        self.y = y
        self.z = z
        self.LG = LG

    def disable(self) -> None:
        """Disables self-weight.
        """
        self.enabled = False
