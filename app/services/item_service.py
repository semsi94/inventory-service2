from sqlalchemy.orm import Session
from app.repositories.item_repository import ItemRepository
from app.schemas.item import ItemCreate, ItemUpdate
from app.models.item import Item

class ItemService:
    def __init__(self, db: Session):
        self.item_repo = ItemRepository(db)

    def get_item(self, item_id: int):
        return self.item_repo.get_item(item_id)

    def get_items(self, skip: int = 0, limit: int = 10):
        return self.item_repo.get_items(skip, limit)

    def create_item(self, item: ItemCreate):
        return self.item_repo.create_item(item)

    def update_item(self, item_id: int, item: ItemUpdate):
        return self.item_repo.update_item(item_id, item)

    def delete_item(self, item_id: int):
        return self.item_repo.delete_item(item_id)
