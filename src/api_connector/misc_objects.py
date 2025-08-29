from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from api_connector.enum import HistoryType, ItemType, Quality

class Requirements(BaseModel):
    level: int
    strenght: int
    
class Stats(BaseModel):
    strength: Optional[int] = None
    defence: Optional[int] = None
    speed: Optional[int] = None
    dexterity: Optional[int] = None
    critical_chance: Optional[int] = None
    critical_damage	: Optional[int] = None
    movement_speed: Optional[int] = None
    attack_power: Optional[int] = None
    protection: Optional[int] = None
    agility: Optional[int] = None
    accuracy: Optional[int] = None
    damage: Optional[int] = None

class Skills(BaseModel):
    woodcutting: Optional[int] = None
    mining: Optional[int] = None
    fishing: Optional[int] = None
    alchemy: Optional[int] = None
    smelting: Optional[int] = None
    cooking	: Optional[int] = None
    forge: Optional[int] = None
    meditation: Optional[int] = None
    hunting_mastery: Optional[int] = None
    guild_mastery: Optional[int] = None
    combat: Optional[int] = None
    dungeoneering: Optional[int] = None
    bartering: Optional[int] = None
    pet_mastery: Optional[int] = None
    shadow_mastery: Optional[int] = None
    yule_mastery: Optional[int] = None
    springtide_mastery: Optional[int] = None
    
class Effects(BaseModel):
    attribute: str
    target: str
    value: int
    value_type: str
    
    
class TierModifiers(BaseModel):
    tier_2: float = Field(alias="2")
    tier_3: float = Field(alias="3")
    tier_4: float = Field(alias="4")
    tier_5: float = Field(alias="5")
    
class UpgradeRequirements(BaseModel):
    item_id: str
    quantity: str
    
class Material(BaseModel):
    hashed_item_id: str
    item_name: str
    quantity: int

class Result(BaseModel):
    hashed_item_id: str
    item_name: str
    
class Experience(BaseModel):
    stats: Stats
    skills: Skills
    
class Recipe(BaseModel):
    skill: str
    level_required: int
    max_uses: int
    experience: Experience
    materials: list[Material]
    result: Result
    
class Pet(BaseModel): #TODO
    pass

class Ennemie(BaseModel):
    id: int
    name: str
    level: int

class Ennemie(BaseModel):
    id: int
    name: str
    level: int

class Dungeon(BaseModel):
    id: int
    name: str

class WorldBosses(BaseModel):
    id: int
    name: str
    
class WhereToFind(BaseModel):
    enemies: Optional[list[Ennemie]] = None
    dungeons: Optional[list[Dungeon]] = None
    world_bosses: Optional[list[WorldBosses]] = None
    
    

    

    
    
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

class HistoryData(BaseModel):
    date: datetime
    average_price: int
    total_sold: int
    
class LatestSold(BaseModel):
    item: Item
    tier: int
    quantity: int
    price_per_item: int
    total_price: int
    sold_at: datetime

class ItemMarketHistory(BaseModel):
    history_data: list[HistoryData]
    latest_sold: list[LatestSold]
    type: HistoryType
    