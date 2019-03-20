from typing import List, Dict, Any


class InvalidUserOptions(Exception):
    pass


class UserOptions:
    """
    Configuration supplied by the end user.
    """
    def __init__(
        self,
        session_options: Dict[str, Any],
        contracts_options: List[Dict[str, Any]],
    ) -> None:
        self.session_options = session_options
        self.contracts_options = contracts_options

    def __eq__(self, other):
        if not isinstance(other, UserOptions):
            return False
        return (
            self.session_options == other.session_options
        ) and (
            self.contracts_options == other.contracts_options
        )
