class Settlement:
    def __init__(self,
                 node: int = None,
                 tx: float = 0,
                 ty: float = 0,
                 tz: float = 0,
                 rx: float = 0,
                 ry: float = 0,
                 rz: float = 0
                 ) -> None:
        """Creates an instance of the SkyCiv Settlement class.

        Args:
            node (int): The ID of the node at which the settlement is applied.
            tx (float, optional): Settlement displacement in the global x-axis. Defaults to None.
            ty (float, optional): Settlement displacement in the global y-axis. Defaults to None.
            tz (float, optional): Settlement displacement in the global z-axis. Defaults to None.
            rx (float, optional): Settlement rotation about the global x-axis. Defaults to None.
            ry (float, optional): Settlement rotation about the global y-axis. Defaults to None.
            rz (float, optional): Settlement rotation about the global z-axis. Defaults to None.
        """
        self.node = node
        self.tx = tx
        self.ty = ty
        self.tz = tz
        self.rx = rx
        self.ry = ry
        self.rz = rz
