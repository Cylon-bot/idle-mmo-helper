from typing import Optional

from pydantic import BaseModel, Field

from api_connector.objects.battle import Dungeon, Ennemie, WorldBosses
from api_connector.objects.mastery import Skills, Stats

class Material(BaseModel):
    hashed_item_id: str
    item_name: str
    quantity: int
    
class Requirements(BaseModel):
    level: int
    strenght: int
    
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
    
class WhereToFind(BaseModel):
    enemies: Optional[list[Ennemie]] = None
    dungeons: Optional[list[Dungeon]] = None
    world_bosses: Optional[list[WorldBosses]] = None
    

