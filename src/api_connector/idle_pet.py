
from dataclasses import dataclass

from misc import JSON


@dataclass
class Pet:
    json_payload: JSON
    
    def __post_init__():
        pass
