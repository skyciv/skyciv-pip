from skyciv.classes.model.components.area_loads.area_load import AreaLoad
from skyciv.classes.model.components.distributed_loads.distributed_load import DistributedLoad
from skyciv.classes.model.components.load_combinations.load_combination import LoadCombination
from skyciv.classes.model.components.materials.material import Material
from skyciv.classes.model.components.members.member import Member
from skyciv.classes.model.components.meshed_plates.meshed_plate import MeshedPlate
from skyciv.classes.model.components.moments.moment import Moment
from skyciv.classes.model.components.nodes.node import Node
from skyciv.classes.model.components.plates.plate import Plate
from skyciv.classes.model.components.point_loads.point_load import PointLoad
from skyciv.classes.model.components.pressures.pressure import Pressure
from skyciv.classes.model.components.sections.section import Section
from skyciv.classes.model.components.self_weights.self_weight import SelfWeight
from skyciv.classes.model.components.settlements.settlement import Settlement
from skyciv.classes.model.components.supports.support import Support
from skyciv.classes.model.model import Model
from skyciv.utils.helpers import keys, keyvals

key_class_map = {
    "nodes": Node,
    "members": Member,
    "plates": Plate,
    "meshed_plates": MeshedPlate,
    "sections": Section,
    "materials": Material,
    "supports": Support,
    "settlements": Settlement,
    "point_loads": PointLoad,
    "moments": Moment,
    "distributed_loads": DistributedLoad,
    "pressures": Pressure,
    "area_loads": AreaLoad,
    "self_weight": SelfWeight,
    "load_combinations": LoadCombination,
}


def set_attribs(_from, to):
    for collection, collection_values in keyvals(_from):
        if (type(collection_values) is dict or hasattr(collection_values, "__dict__")):
            # Check if single item should be created
            if collection in keys(key_class_map):
                # print(collection)
                for id in keys(collection_values):
                    # print(id)
                    item = key_class_map[collection]()
                    # print(item)
                    setattr(to[collection], id, item)
            # Dig deeper
            if collection_values != None:
                if collection == "sections":
                    # Special treatment for sections
                    for id, sec_data in keyvals(collection_values):
                        if type(sec_data) == list:
                            setattr(to[collection][id],
                                    "load_section", sec_data)
                        elif sec_data is None:
                            setattr(to[collection], id, None)
                        else:
                            setattr(to[collection][id], "load_section",
                                    sec_data["aux"]["polygons"][0]["library_selections"])

                        setattr(to[collection][id], "material_id",
                                sec_data["material_id"])
                else:
                    set_attribs(_from[collection], to[collection])

        else:
            # Set the value
            print(collection_values)
            setattr(to, collection, collection_values)


def model_adapter(jsonModel, model):
    set_attribs(jsonModel, model)
