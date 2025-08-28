import requests

from api_connector.idle_pet import Pet
from api_connector.item import Item


class IdleMmoApiConnector():
    def __init__(self, api_key: str):
        self.base_url = "https://api.idle-mmo.com/v1"
        self.headers = {"Authentication": api_key,
                        "Accept": "application/json",
                        "User-Agent": "idle-mmo-helper/1.0.0"}
    
    def get_character_pets(self, character_id: str) -> list[Pet]:
        requested_pets_response = requests.get(url=f"{self.base_url}/character/{character_id}/pets", headers=self.headers)
        if requested_pets_response.status_code == 200:
            return [Pet(json_payload=pet_payload) for pet_payload in requested_pets_response.json()["pets"]]
        else:
            raise Exception(requested_pets_response.reason)
    
    def get_item_market_history(self, item_id: str) -> Item:
        requested_item_response = requests.get(url=f"{self.base_url}/item/{item_id}/market-history", headers=self.headers)
        if requested_item_response.status_code == 200:
            return Item(json_payload=requested_item_response.json())
        else:
            raise Exception(requested_item_response.reason)