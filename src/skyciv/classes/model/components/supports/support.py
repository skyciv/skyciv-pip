class Support:
    def __init__(self,
                 node: int=None,
                 restraint_code: str = 'FFFFFF',
                 tx: float = 0,
                 ty: float = 0,
                 tz: float = 0,
                 rx: float = 0,
                 ry: float = 0,
                 rz: float = 0
                 ) -> None:
        """Creates an instance of the SkyCiv Support class.

        Args:
            node (int): The ID of the node at which the support is located.
            restraint_code (str, optional): A 6 character restraint code. See docs for restraint code https://skyciv.com/api/v3/docs/s3d-model#restraint-code. Defaults to 'FFFFFF'.
            tx (float, optional): Spring stiffness for translation in the x-axis. Applies only if the restraint code character for translation in x = S. Defaults to 0.
            ty (float, optional): Spring stiffness for translation in the y-axis. Applies only if the restraint code character for translation in y = S. Defaults to 0.
            tz (float, optional): Spring stiffness for translation in the z-axis. Applies only if the restraint code character for translation in z = S. Defaults to 0.
            rx (float, optional): Spring stiffness for rotation about the x-axis. Applies only if the restraint code character for rotation about x = S. Defaults to 0.
            ry (float, optional): Spring stiffness for rotation about the y-axis. Applies only if the restraint code character for rotation about y = S. Defaults to 0.
            rz (float, optional): Spring stiffness for rotation about the z-axis. Applies only if the restraint code character for rotation about z = S. Defaults to 0.
        """
        self.node = node

        if restraint_code:
            self.restraint_code = restraint_code
        else:
            self.restraint_code = "FFFFFF"

        self.tx = tx
        self.ty = ty
        self.tz = tz
        self.rx = rx
        self.ry = ry
        self.rz = rz
