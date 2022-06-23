from dataclasses import dataclass


@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0


if __name__ == '__main__':
    pos = Position('Oslo', 10.8, 59.9)
    print(pos)
    print(pos.lat)
    print(f'{pos.name} is at {pos.lat}°N, {pos.lon}°E')

    # Testting default values
    print(Position('Null Island'))
    print(Position('Greenwich', lat=51.8))
    print(Position('Vancouver', -123.1, 49.3))
