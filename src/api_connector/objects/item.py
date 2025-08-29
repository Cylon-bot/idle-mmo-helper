from typing import Optional

from pydantic import BaseModel

from api_connector.enum import ItemType, Quality
from api_connector.objects.battle import Pet
from api_connector.objects.mastery import Stats
from api_connector.objects.misc import Effects, Recipe, Requirements, TierModifiers, UpgradeRequirements, WhereToFind



class Item(BaseModel):
    hashed_id: str
    name: str
    image_url: str
    description: Optional[str] = None
    type: Optional[ItemType] = None
    quality: Optional[Quality] = None
    vendor_price: Optional[int] = None

    class Config:
        use_enum_values = False 

class ItemDetails(BaseModel):
    item: Item
    is_tradeable: bool
    max_tier: int
    requirements: Optional[Requirements] = None
    stats: Optional[Stats] = None
    effects: Optional[list[Effects]] = None
    tier_modifiers: Optional[TierModifiers] = None
    upgrade_requirements: Optional[UpgradeRequirements] = None
    health_restore: Optional[int] = None
    hunger_restore: Optional[int] = None
    recipe: Optional[Recipe] = None
    chest_drops: Optional[list] = None #TODO
    pet: Optional[Pet] = None
    where_to_find: Optional[WhereToFind] = None
