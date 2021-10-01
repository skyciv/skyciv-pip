from skyciv.classes.functions.api_function import ApiFunction
from skyciv.classes.model.components.load_combinations.load_combinations import LoadCombinations
from skyciv.utils.helpers import clone, has_get_method, keyvals
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

class ApiFunctions:

    def __init__(self):
        """Creates an instance of the SkyCiv ApiFunctions class.
        """
        self.function_list = []

    def get(self):
        """Get the functions array.
        """
        list = clone(self.function_list)

        # Run get method on functions
        for i in range(len(list)):
            list[i] = list[i].get()

            # Run get method on any function args if they have the method available
            for k, v in list[i]["arguments"].items():
                if has_get_method(v):
                    list[i]["arguments"][k] = v.get()

        return list

    def add(self, function_name: Literal["S3D.session.start", "S3D.model.set", "S3D.model.get", "S3D.model.repair", "S3D.model.solve", "S3D.model.takeScreenshot", "S3D.model.mesh", "S3D.results.set", "S3D.results.get", "S3D.results.fetchMemberResult", "S3D.results.getAnalysisReport", "S3D.model.takeScreenshot", "S3D.design.member.getInput", "S3D.design.member.check", "S3D.design.member.optimize", "standalone.member.check", "S3D.design.rc.getInput", "S3D.design.rc.check", "S3D.SB.loadLibraryShape", "S3D.SB.getLibraryTree", "S3D.SB.buildCustomShape", "S3D.SB.solve", "S3D.SB.runGSD", "S3D.file.save", "S3D.file.open", "S3D.file.share", "S3D.file.getFileDirectory"], args: dict = {}) -> None:
        """Add a SkyCiv function to the ApiObject's functions list. See the docs for available functions and respective arguments. https://skyciv.com/api/v3/docs/the-request-object#functions.
        Args:
            function_name (str): The SkyCiv function name. {"S3D.session.start" | "S3D.model.set" | "S3D.model.get" | "S3D.model.repair" | "S3D.model.solve" | "S3D.model.takeScreenshot" | "S3D.model.mesh" | "S3D.results.set" | "S3D.results.get" | "S3D.results.fetchMemberResult" | "S3D.results.getAnalysisReport" | "S3D.model.takeScreenshot" | "S3D.design.member.getInput" | "S3D.design.member.check" | "S3D.design.member.optimize" | "standalone.member.check" | "S3D.design.rc.getInput" | "S3D.design.rc.check" | "S3D.SB.loadLibraryShape" | "S3D.SB.getLibraryTree" | "S3D.SB.buildCustomShape" | "S3D.SB.solve" | "S3D.SB.runGSD" | "S3D.file.save" | "S3D.file.open" | "S3D.file.share" | "S3D.file.getFileDirectory"}
            args (dict, optional): See the docs for the available arguments. Defaults to {}.
        """
        fn = ApiFunction(function_name, args)

        # Where there is an s3d_model, overwrite load_combinations with its get method it doesnt have the list prop.
        for arg_key, arg_value in args.items():
            if (arg_key == 's3d_model'):
                for k, v in keyvals(arg_value):
                    if (isinstance(v, LoadCombinations)):
                        # args["s3d_model"]["load_combinations"] = v.get()
                        args["s3d_model"].set({
                            "load_combinations": v.get(),
                        })

        self.function_list.append(fn)

    def remove(self, function_name: Literal["S3D.session.start", "S3D.model.set", "S3D.model.get", "S3D.model.repair", "S3D.model.solve", "S3D.model.takeScreenshot", "S3D.model.mesh", "S3D.results.set", "S3D.results.get", "S3D.results.fetchMemberResult", "S3D.results.getAnalysisReport", "S3D.model.takeScreenshot", "S3D.design.member.getInput", "S3D.design.member.check", "S3D.design.member.optimize", "standalone.member.check", "S3D.design.rc.getInput", "S3D.design.rc.check", "S3D.SB.loadLibraryShape", "S3D.SB.getLibraryTree", "S3D.SB.buildCustomShape", "S3D.SB.solve", "S3D.SB.runGSD", "S3D.file.save", "S3D.file.open", "S3D.file.share", "S3D.file.getFileDirectory"]) -> None:
        """Remove all occurences of a SkyCiv function from the ApiObject's functions list. See the docs for available functions and respective arguments. https://skyciv.com/api/v3/docs/the-request-object#functions

        Args:
            function_name (str): The SkyCiv function name. {"S3D.session.start" | "S3D.model.set" | "S3D.model.get" | "S3D.model.repair" | "S3D.model.solve" | "S3D.model.takeScreenshot" | "S3D.model.mesh" | "S3D.results.set" | "S3D.results.get" | "S3D.results.fetchMemberResult" | "S3D.results.getAnalysisReport" | "S3D.model.takeScreenshot" | "S3D.design.member.getInput" | "S3D.design.member.check" | "S3D.design.member.optimize" | "standalone.member.check" | "S3D.design.rc.getInput" | "S3D.design.rc.check" | "S3D.SB.loadLibraryShape" | "S3D.SB.getLibraryTree" | "S3D.SB.buildCustomShape" | "S3D.SB.solve" | "S3D.SB.runGSD" | "S3D.file.save" | "S3D.file.open" | "S3D.file.share" | "S3D.file.getFileDirectory"}.
        """
        new_list = []
        for fn in self.function_list:
            if fn["function"] != function_name:
                new_list.append(fn)

        self.function_list = new_list

    def remove_all(self) -> None:
        """Remove all SkyCiv functions from the ApiObject's functions list. See the docs for available functions and respective arguments. https://skyciv.com/api/v3/docs/the-request-object#functions
        """
        self.function_list = []
