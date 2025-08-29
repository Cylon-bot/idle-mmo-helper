from pydantic import BaseModel


class Pet(BaseModel): #TODO
    pass

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