from dataclasses import dataclass
from typing import Any


@dataclass
class WithoutExplicitTypes:
    name: Any
    value: Any = 42


@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0


if __name__ == '__main__':
    print(WithoutExplicitTypes('Victor', 16))

    # While you need to add type hints in some form when using data classes,
    # these types are not enforced at runtime
    print(Position(3.14, 'pi day', 2018))
