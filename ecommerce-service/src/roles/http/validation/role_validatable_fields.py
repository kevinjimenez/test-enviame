ROLE_CREATION_VALIDATABLE_FIELDS = {

    "name": {
        "required": True,
        "type": "string",
    },

    "description": {
        "required": True,
        "type": "string",
    },

}

ROLE_UPDATE_VALIDATABLE_FIELDS = {

    "name": {
        "required": False,
        "type": "string",
    },

    "description": {
        "required": False,
        "type": "string",
    },    

}