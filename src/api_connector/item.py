
from dataclasses import dataclass

from misc import JSON


@dataclass
class Item:
    json_payload: JSON
    
    def __post_init__():
        pass
    
