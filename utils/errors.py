class Error(object):
    def __init__(self, msg: str = "") -> None:
        super().__init__()
        self._msg = msg

    def __str__(self) -> str:
        return self._msg

    def __repr__(self) -> str:
        return self._msg

    def __eq__(self, o: object) -> bool:
        return self._msg == o.__repr__

    def __nonzero__(self) -> bool:
        return self._msg != ""
