import abc
from typing import Optional

class Pin (abc.ABC):

    @abc.abstractmethod
    def __init__ (self):
        pass

    @property
    @abc.abstractmethod
    def value (self) -> int:
        pass


class Input (Pin):

    _connection: 'Output'
    _default: int

    def __init__ (self, default: Optional[int]):
        self._default = default if default is not None else 0
        pass

    @property
    def connection (self) -> 'Output':
        return self._connection

    @connection.setter
    def connection (self, other: 'Output'):
        assert isinstance(other, Output)
        self._connection = other

    @property
    def value (self) -> int:
        return (
            self._connection.value
            if hasattr(self, '_connection')
            else 0
        )

    @value.setter
    def value (self, _):
        raise Exception("value cannot be set externally")


class Output (Pin):

    _connections: list['Input']
    parent: 'Chip'

    def __init__ (self, parent: 'Chip'):
        self.connections = []
        self.parent = parent

    @property
    def value (self) -> int:
        # Output should implement how it determines its value
        # This is a placeholder - subclasses should override this
        return 0


class Chip (abc.ABC):

    _inputs: list[Pin]

    @abc.abstractmethod
    def __init__ (self):
        pass
