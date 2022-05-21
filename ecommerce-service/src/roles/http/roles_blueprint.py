from flask import Blueprint, request

from enviame.inputvalidation import validate_schema_flask, SUCCESS_CODE, FAIL_CODE

from src.roles.http.validation import role_validatable_fields

# Endpoints para CRUD de libros.

# Sólo se encarga de recibir las llamadas HTTP y le entrega los datos
# relevantes a los casos de uso correspondientes. Esta capa no debe
# contener lógica de negocio, sólo lo necesario para recibir y entregar
# respuestas válidas al mundo exterior.

# Se realiza la validación de datos de entrada mediante el decorador 
# "@validate_schema_flask", el cual recibe como argumento un diccionario definido
# en el archivo "role_validatable_fields". No sólo valida que todos los campos
# requeridos vengan en el payload, sino que también que no vengan campos de más.

def create_roles_blueprint(manage_roles_usecase):

    blueprint = Blueprint("roles", __name__)

    @blueprint.route("/roles", methods = ["GET"])
    def get_roles():

        roles = manage_roles_usecase.get_roles()

        roles_dict = []
        for role in roles:
            roles_dict.append(role.serialize())

        data = roles_dict
        code = SUCCESS_CODE
        message = "roles obtained succesfully"
        http_code = 200

        response = {
            "code": code,
            "message": message,
            "data": data,
        }
        
        return response, http_code

    @blueprint.route("/roles/<string:role_id>", methods = ["GET"])
    def get_role(role_id):

        role = manage_roles_usecase.get_role(role_id)

        if role:
            data = role.serialize()
            code = SUCCESS_CODE
            message = "role obtained succesfully"
            http_code = 200

        else:
            data = None
            code = FAIL_CODE
            message = f"role of ID {role_id} does not exist."
            http_code = 404

        response = {
            "code": code,
            "message": message,
        }

        if data:
            response["data"] = data
        
        return response, http_code

    @blueprint.route("/roles", methods = ["POST"])
    @validate_schema_flask(role_validatable_fields.ROLE_CREATION_VALIDATABLE_FIELDS)
    def create_role():

        body = request.get_json()

        try:
            role = manage_roles_usecase.create_role(body)
            data = role.serialize()
            code = SUCCESS_CODE
            message = "role created succesfully"
            http_code = 201

        except ValueError as e:
            data = None
            code = FAIL_CODE
            message = str(e)
            http_code = 400

        response = {
            "code": code,
            "message": message,
        }

        if data:
            response["data"] = data

        return response, http_code

    @blueprint.route("/roles/<string:role_id>", methods = ["PUT"])
    @validate_schema_flask(role_validatable_fields.ROLE_UPDATE_VALIDATABLE_FIELDS)
    def update_role(role_id):

        body = request.get_json()

        try:
            role = manage_roles_usecase.update_role(role_id, body)
            data = role.serialize()
            message = "role updated succesfully"
            code = SUCCESS_CODE
            http_code = 200

        except ValueError as e:
            data = None
            code = FAIL_CODE
            message = str(e)
            http_code = 400

        response = {
            "code": code,
            "message": message,
        }

        if data:
            response["data"] = data

        return response, http_code

    @blueprint.route("/roles/<string:role_id>", methods = ["DELETE"])
    def delete_role(role_id):

        try:
            manage_roles_usecase.delete_role(role_id)
            code = SUCCESS_CODE
            message = f"role of ID {role_id} deleted succesfully."
            http_code = 200

        except ValueError as e:
            code = FAIL_CODE
            message = str(e)
            http_code = 400

        response = {
            "code": code,
            "message": message,
        }

        return response, http_code

    return blueprint
