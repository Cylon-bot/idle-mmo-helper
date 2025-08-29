import os

from dotenv import load_dotenv

from api_connector.enum import HistoryType
from api_connector.idle_api import IdleMmoApiConnector

load_dotenv()
def main():
    idle_connector = IdleMmoApiConnector(api_key=os.getenv("IDLE_API_KEY"))
    character_hashed_id = idle_connector.get_authentication_check()["character"]["hashed_id"]
    item = idle_connector.get_items_by_search(item_query="Elk Antler")[0]
    print(idle_connector.get_item_market_history(hashed_item_id=item.hashed_id, history_type=HistoryType.Orders))
    
    
main()