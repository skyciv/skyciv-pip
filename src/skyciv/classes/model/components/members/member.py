try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class Member:
    def __init__(
        self,
        node_A: int = None,
        node_B: int = None,
        section_id: int = None,
        fixity_A: str = 'FFFFFF',
        fixity_B: str = 'FFFFFF',
        type: Literal["normal", "normal_continuous",
                      "cable", "rigid"] = 'normal',
        cable_length: float = None,
        rotation_angle: float = 0,
        offset_Ax: float = 0,
        offset_Ay: float = 0,
        offset_Az: float = 0,
        offset_Bx: float = 0,
        offset_By: float = 0,
        offset_Bz: float = 0
    ) -> None:
        """Creates an instance of the SkyCiv Member class.

        Args:
            node_A (int): The ID of the start node.
            node_B (int): The ID of the end node.
            section_id (int): The ID of the section that should be applied to the member.
            fixity_A (str, optional): See docs for restraint code https://skyciv.com/api/v3/docs/s3d-model#restraint-code. Defaults to 'FFFFFF'.
            fixity_B (str, optional): See docs for restraint code https://skyciv.com/api/v3/docs/s3d-model#restraint-code. Defaults to 'FFFFFF'.
            type (str, optional): Defaults to 'normal'. {"normal" | "normal_continuous" | "cable" | "rigid"}.
            cable_length (float, optional): Required only when type = cable. Defaults to None.
            rotation_angle (float, optional): Rotation of the member about its own axis, in degrees.
            offset_Ax (float, optional): The local x distance that the member is offset from its centroid at node A.
            offset_Ay (float, optional): The local y distance that the member is offset from its centroid at node A.
            offset_Az (float, optional): The local z distance that the member is offset from its centroid at node A.
            offset_Bx (float, optional): The local x distance that the member is offset from its centroid at node B.
            offset_By (float, optional): The local y distance that the member is offset from its centroid at node B.
            offset_Bz (float, optional): The local z distance that the member is offset from its centroid at node B.
        """
        self.node_A = node_A
        self.node_B = node_B
        self.section_id = section_id
        self.fixity_A = fixity_A
        self.fixity_B = fixity_B
        self.type = type
        self.cable_length = cable_length
        self.rotation_angle = rotation_angle
        self.offset_Ax = offset_Ax
        self.offset_Ay = offset_Ay
        self.offset_Az = offset_Az
        self.offset_Bx = offset_Bx
        self.offset_By = offset_By
        self.offset_Bz = offset_Bz
