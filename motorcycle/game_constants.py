from enum import Enum, IntEnum, auto

class CharaBodyIndex(Enum):
    Normal = auto()
    Succeeded = auto()
    Failed = auto()

class GameState(Enum):
    GameTitle = auto()
    GamePlay = auto()
    GameResult = auto()

class FaceIndex(IntEnum):
    Empty = -1
    Normal = 0
    Blink = auto()
    Astonish = auto()
    Smile = auto()
    Cry = auto()

    
