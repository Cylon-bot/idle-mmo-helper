from typing import Optional

from pydantic import BaseModel


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