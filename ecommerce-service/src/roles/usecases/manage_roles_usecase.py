from src.roles.entities.role import Role
from src.utils import utils

class ManageRolesUsecase:

    def __init__(self, roles_repository):
        self.roles_repository = roles_repository

    def get_roles(self):

        return self.roles_repository.get_roles()

    def get_role(self, role_id):

        return self.roles_repository.get_role(role_id)

    def create_role(self, data):
            
        current_time = utils.get_current_datetime()
        
        data["created_at"] = current_time
        data["updated_at"] = current_time

        role = Role.from_dict(data)
        role = self.roles_repository.create_role(role)

        return role

    def update_role(self, role_id, data):

        role = self.get_role(role_id)

        if role:

            data["updated_at"] = utils.get_current_datetime()
            role = self.roles_repository.update_role(role_id, data)

            return role

        else:
            raise ValueError(f"role of ID {role_id} doesn't exist.")

    def delete_role(self, role_id):

        role = self.get_role(role_id)

        if role:

            data = {
                "deleted_at": utils.get_current_datetime()
            }
            
            role = self.roles_repository.update_role(role_id, data)

        else:
            raise ValueError(f"role of ID {role_id} doesn't exist or is already deleted.")