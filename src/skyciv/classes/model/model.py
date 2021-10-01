from skyciv.classes.model.components.area_loads.area_loads import AreaLoads
from skyciv.classes.model.components.distributed_loads.distributed_loads import DistributedLoads
from skyciv.classes.model.components.load_combinations.load_combinations import LoadCombinations
from skyciv.classes.model.components.materials.materials import Materials
from skyciv.classes.model.components.members.members import Members
from skyciv.classes.model.components.meshed_plates.meshed_plates import MeshedPlates
from skyciv.classes.model.components.moments.moments import Moments
from skyciv.classes.model.components.nodes.nodes import Nodes
from skyciv.classes.model.components.plates.plates import Plates
from skyciv.classes.model.components.point_loads.point_loads import PointLoads
from skyciv.classes.model.components.pressures.pressures import Pressures
from skyciv.classes.model.components.sections.sections import Sections
from skyciv.classes.model.components.self_weights.self_weights import SelfWeights
from skyciv.classes.model.components.settings.settings import Settings
from skyciv.classes.model.components.settlements.settlements import Settlements
from skyciv.classes.model.components.supports.supports import Supports
from skyciv.utils.helpers import clone, has_get_method, keyvals

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class Model:

    def __init__(self, unit_system: Literal["metric", "imperial"], vertical_axis: Literal["Y", "Z"] = 'Y'):
        """Create an s3d_model object.

        Args:
            unit_system (str): {'metric' | 'imperial'}
            vertical_axis (str, optional): {"Y" | "Z"}. Defaults to 'Y'.

        Example: 
            Default for: metric | imperial::
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
        self.settings = Settings(unit_system, vertical_axis)
        self.nodes = Nodes()
        self.members = Members()
        self.plates = Plates()
        self.meshed_plates = MeshedPlates()
        self.sections = Sections()
        self.materials = Materials()
        self.supports = Supports()
        self.settlements = Settlements()
        self.point_loads = PointLoads()
        self.moments = Moments()
        self.distributed_loads = DistributedLoads()
        self.pressures = Pressures()
        self.area_loads = AreaLoads()
        self.member_prestress_loads = {}
        self.self_weight = SelfWeights()
        self.load_combinations = LoadCombinations()
        self.load_cases = {}
        self.nodal_masses = {}
        self.nodal_masses_conversion_map = {}
        self.spectral_loads = {}
        self.groups = []

    def get(self) -> dict:
        """Get the model in the format required by the SkyCiv API.

        Returns:
            dict: A SkyCiv formatted S3D Model as a python dictionary.
        """
        s3d_model = clone(self.__dict__)

        for k, v in s3d_model.items():
            if (has_get_method(v)):
                s3d_model[k] = v.get()

        return s3d_model

    def set(self, model_object: dict) -> None:
        """Set individual properties of the model object.

        Args:
            model_object (dict): An object of key value pairs.

        Example::

            model = new Model()
            model.set({
                nodes: SkyCivNodesObject,
                members: "SkyCivMembersObject"
            })
        """
        for k, v in model_object.items():
            if hasattr(self, k):
                setattr(self, str(k), v)

    def __getitem__(self, item):
        return getattr(self, item)
