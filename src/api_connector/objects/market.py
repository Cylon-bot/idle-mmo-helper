from datetime import datetime

from pydantic import BaseModel

from api_connector.enum import HistoryType
from api_connector.objects.item import Item


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
    