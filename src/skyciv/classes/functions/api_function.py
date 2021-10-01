from skyciv.utils.helpers import clone
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class ApiFunction:

    def __init__(self, function_name: Literal["S3D.session.start", "S3D.model.set", "S3D.model.get", "S3D.model.repair", "S3D.model.solve", "S3D.model.takeScreenshot", "S3D.model.mesh", "S3D.results.set", "S3D.results.get", "S3D.results.fetchMemberResult", "S3D.results.getAnalysisReport", "S3D.model.takeScreenshot", "S3D.design.member.getInput", "S3D.design.member.check", "S3D.design.member.optimize", "standalone.member.check", "S3D.design.rc.getInput", "S3D.design.rc.check", "S3D.SB.loadLibraryShape", "S3D.SB.getLibraryTree", "S3D.SB.buildCustomShape", "S3D.SB.solve", "S3D.SB.runGSD", "S3D.file.save", "S3D.file.open", "S3D.file.share", "S3D.file.getFileDirectory"], args: dict = {}) -> None:
        """Creates an instance of the SkyCiv ApiFunction class. See the docs for available functions and respective arguments. https://skyciv.com/api/v3/docs/the-request-object#functions

        Args:
            function_name (str): The SkyCiv function name. {"S3D.session.start" | "S3D.model.set" | "S3D.model.get" | "S3D.model.repair" | "S3D.model.solve" | "S3D.model.takeScreenshot" | "S3D.model.mesh" | "S3D.results.set" | "S3D.results.get" | "S3D.results.fetchMemberResult" | "S3D.results.getAnalysisReport" | "S3D.model.takeScreenshot" | "S3D.design.member.getInput" | "S3D.design.member.check" | "S3D.design.member.optimize" | "standalone.member.check" | "S3D.design.rc.getInput" | "S3D.design.rc.check" | "S3D.SB.loadLibraryShape" | "S3D.SB.getLibraryTree" | "S3D.SB.buildCustomShape" | "S3D.SB.solve" | "S3D.SB.runGSD" | "S3D.file.save" | "S3D.file.open" | "S3D.file.share" | "S3D.file.getFileDirectory"}
            args (dict, optional): See the docs for the available arguments. Defaults to {}.
        """
        self.function = function_name
        self.arguments = args

    def get(self) -> dict:
        """Get the function object as a python dictionary.
        Returns:
            dict: The function as a python dictionary.
        """
        return clone(self.__dict__)
