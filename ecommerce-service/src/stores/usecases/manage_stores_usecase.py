from src.stores.entities.store import Store
from src.utils import utils

class ManageStoresUsecase:

    def __init__(self, stores_repository):
        self.stores_repository = stores_repository

    def get_stores(self):

        return self.stores_repository.get_stores()

    def get_store(self, store_id):

        return self.stores_repository.get_store(store_id)

    def create_store(self, data):
        current_time = utils.get_current_datetime()
        
        data["created_at"] = current_time
        data["updated_at"] = current_time
        
        store = Store.from_dict(data)
        store = self.stores_repository.create_store(store)

        return store

    def update_store(self, store_id, data):

        store = self.get_store(store_id)

        if store:

            data["updated_at"] = utils.get_current_datetime()
            store = self.stores_repository.update_store(store_id, data)

            return store

        else:
            raise ValueError(f"store of ID {store_id} doesn't exist.")

    def delete_store(self, store_id):

        store = self.get_store(store_id)

        if store:

            data = {
                "deleted_at": utils.get_current_datetime()
            }
            
            store = self.stores_repository.update_store(store_id, data)

        else:
            raise ValueError(f"store of ID {store_id} doesn't exist or is already deleted.")