from skyciv.utils.helpers import clone


class AuthObject:
    def __init__(self, username: str = None, key: str = None, session_id: str = None):
        """Creates an instance of the SkyCiv AuthObject class.

        Args:
            username (str, optional): Your SkyCiv username. Defaults to None.
            key (str, optional): Your SkyCiv API key. Defaults to None.
            session_id (str, optional): The session_id. This package will automatically add this to the APIObject if you use the APIObject's .request() method. Defaults to None.
        """
        self.username = username
        self.key = key
        self.session_id = session_id

    def get(self):
        return clone(self.__dict__)
