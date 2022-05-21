from src.utils.utils import format_date

class User():

    def __init__(self, id, name, email, shipping_addres, role, created_at = None, updated_at = None, deleted_at = None):

        self.id = id
        self.name = name
        self.email = email
        self.shipping_addres = shipping_addres
        self.role = role
        
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at

    def to_dict(self):

        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "shipping_addres": self.shipping_addres,
            "role": self.role,
            
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at,
        }

    def serialize(self):

        data = self.to_dict()
        
        data.pop("deleted_at")
        
        data["created_at"] = format_date(data["created_at"])
        data["updated_at"] = format_date(data["updated_at"])

        return data

    @classmethod
    def from_dict(cls, dict):

        id = dict.get("id")
        name = dict.get("name")
        email = dict.get("email")
        shipping_addres = dict.get("shipping_addres")
        role = dict.get("role")

        created_at = dict.get("created_at")
        updated_at = dict.get("updated_at")
        deleted_at = dict.get("deleted_at")

        return User(id, name, email, shipping_addres, role, created_at, updated_at, deleted_at)