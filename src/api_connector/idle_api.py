from typing import Optional
import requests

from api_connector.enum import HistoryType
from api_connector.misc_objects import Item, ItemDetails, ItemMarketHistory, Pet
from misc import JSON


class IdleMmoApiConnector():
    def __init__(self, api_key: str):
        self.base_url = "https://api.idle-mmo.com/v1"
        self.headers = {"Authorization": f"Bearer {api_key}",
                        "Accept": "application/json",
                        "User-Agent": "idle-mmo-helper/1.0.0"}
    
    def get_authentication_check(self) -> JSON:
        authentication_request = requests.get(url=f"{self.base_url}/auth/check", headers=self.headers)
        if authentication_request.status_code == 200:
            return authentication_request.json()
        else:
            raise Exception(authentication_request.json())
        
    def get_character_pets(self, hashed_character_id: str) -> list[Pet]:
        requested_pets_response = requests.get(url=f"{self.base_url}/character/{hashed_character_id}/pets", headers=self.headers)
        if requested_pets_response.status_code == 200:
            return [Pet(json_payload=pet_payload) for pet_payload in requested_pets_response.json()["pets"]]
        else:
            raise Exception(requested_pets_response.json())
    
    def get_items_by_search(self, item_query: Optional[str] = None, item_type: Optional[str] = None) -> list[Item]:
        requested_item_response = requests.get(url=f"{self.base_url}/item/search", headers=self.headers, params={"query": item_query, "type": item_type})
        if requested_item_response.status_code == 200:
            return [Item(**item_payload) for item_payload in requested_item_response.json()["items"]]
        else:
            raise Exception(requested_item_response.json())
        
    def get_item_details(self, hashed_item_id: str) -> ItemDetails:
        requested_item_response = requests.get(url=f"{self.base_url}/item/{hashed_item_id}/inspect", headers=self.headers)
        if requested_item_response.status_code == 200:
            requested_item_json = requested_item_response.json()["item"]
            item = Item(**requested_item_json)
            return ItemDetails(item=item, **requested_item_json)
        else:
            raise Exception(requested_item_response.json())
        
    def get_item_market_history(self, hashed_item_id: str, history_type: HistoryType, item_tier: int = 0) -> ItemMarketHistory:
        requested_item_response = requests.get(url=f"{self.base_url}/item/{hashed_item_id}/market-history", headers=self.headers, params={"tier": item_tier, "type": history_type.value})
        if requested_item_response.status_code == 200:
            return ItemMarketHistory(**requested_item_response.json())
        else:
            raise Exception(requested_item_response.json())