from src.roles.entities.role import Role
from src.utils import utils

# Casos de uso para el manejo de libros.

# Recibe en el constructor el repositorio a utilizar. Da igual si recibe el repositorio
# de SQL o de Firestore, el caso de uso debe funcionar independientemente de su implementación.

class ManageRolesUsecase:

    def __init__(self, roles_repository):
        self.roles_repository = roles_repository

    def get_roles(self):

        # Retorna una lista de entidades role desde el repositorio.

        return self.roles_repository.get_roles()

    def get_role(self, role_id):

        # Retorna una instancia de role según la ID recibida.

        return self.roles_repository.get_role(role_id)

    def create_role(self, data):

        # Crea una instancia role desde la data recibida, que ya debe venir validada desde afuera,
        # y guarda dicha instancia en el repositorio para finalmente retornarla.
            
        current_time = utils.get_current_datetime()
        
        data["created_at"] = current_time
        data["updated_at"] = current_time

        role = Role.from_dict(data)
        role = self.roles_repository.create_role(role)

        return role

    def update_role(self, role_id, data):

        # Actualiza los datos recibidos y los guarda en el repositorio según la ID recibida.
        # La data no necesariamente debe contener todos los campos de la entidad, sólo
        # los campos que se van a actualizar. Esta data debe venir validada desde afuera.

        role = self.get_role(role_id)

        if role:

            data["updated_at"] = utils.get_current_datetime()
            role = self.roles_repository.update_role(role_id, data)

            return role

        else:
            raise ValueError(f"role of ID {role_id} doesn't exist.")

    def delete_role(self, role_id):

        # Realiza un soft-delete del libro con la ID especificada, si es que existe.
        # A nivel de repositorio realiza una actualización al campo "deleted_at".

        role = self.get_role(role_id)

        if role:

            data = {
                "deleted_at": utils.get_current_datetime()
            }
            
            role = self.roles_repository.update_role(role_id, data)

        else:
            raise ValueError(f"role of ID {role_id} doesn't exist or is already deleted.")