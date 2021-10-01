from skyciv.classes.model.components.members.member import Member
from skyciv.utils.helpers import next_object_key
from skyciv.classes.model.components._base_class.model_collection_component import ModelCollectionComponent
from typing import List
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class Members(ModelCollectionComponent):
    """Creates an instance of the SkyCiv Members class.
    """

    def add(
        self,
        node_A: int,
        node_B: int,
        section_id: int,
        fixity_A: str = 'FFFFFF',
        fixity_B: str = 'FFFFFF',
        type: Literal["normal", "normal_continuous",
                      "cable", "rigid"] = 'normal',
        cable_length: float = None
    ) -> int:
        """Create a member with the next available ID.

        Args:
            node_A (int): The ID of the node at the beginning of the member.
            node_B (int): The ID of the node at the end of the member.
            section_id (int): The ID of the section to apply to the member.
            fixity_A (str, optional): See docs for restraint code. https://skyciv.com/api/v3/docs/s3d-model#restraint-code. Defaults to 'FFFFFF'.
            fixity_B (str, optional): See docs for restraint code. https://skyciv.com/api/v3/docs/s3d-model#restraint-code. Defaults to 'FFFFFF'.
            type (str, optional): The type of member. Defaults to 'normal'. {"normal" | "normal_continuous" | "cable" | "rigid"}.
            cable_length (float, optional): Required only when type = cable. Defaults to None.

        Returns:
            int: Required only when type = cable.
        """
        next_index = next_object_key(self)
        element_ids = self.get_member_ids_from_nodes_ids(node_A, node_B)

        if (element_ids != None):
            print(
                'There is more than one member with the same end nodes. Ensure they have different offsets.')

        member = Member(
            node_A,
            node_B,
            section_id,
            fixity_A,
            fixity_B,
            type,
            cable_length
        )
        setattr(self, str(next_index), member)
        return next_index

    def get_member_ids_from_nodes_ids(self, node_A: int, node_B: int) -> List[int]:
        """Get the IDs of all members by its end nodes.

        Args:
            node_A (int): The ID of Node A.
            node_B (int): The ID of Node B.

        Returns:
            list[int]: An array of member IDs or None if none exist.
        """
        ids = []

        for k, v in vars(self).items():
            if (v.node_A == node_A and v.node_B == node_B):
                ids.append(k)

        if len(ids) == 0:
            ids = None

        return ids
