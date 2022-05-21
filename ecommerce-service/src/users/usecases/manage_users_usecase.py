from src.users.entities.user import User
from src.utils import utils

class ManageUsersUsecase:

    def __init__(self, users_repository):
        self.users_repository = users_repository

    def get_users(self):

        return self.users_repository.get_users()

    def get_user(self, user_id):

        return self.users_repository.get_user(user_id)

    def create_user(self, data):

        current_time = utils.get_current_datetime()
        
        data["created_at"] = current_time
        data["updated_at"] = current_time
        
        user = User.from_dict(data)
        user = self.users_repository.create_user(user)

        return user

    def update_user(self, user_id, data):

        user = self.get_user(user_id)

        if user:

            data["updated_at"] = utils.get_current_datetime()
            user = self.users_repository.update_user(user_id, data)

            return user

        else:
            raise ValueError(f"user of ID {user_id} doesn't exist.")

    def delete_user(self, user_id):

        user = self.get_user(user_id)

        if user:

            data = {
                "deleted_at": utils.get_current_datetime()
            }
            
            user = self.users_repository.update_user(user_id, data)

        else:
            raise ValueError(f"user of ID {user_id} doesn't exist or is already deleted.")