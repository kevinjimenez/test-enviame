USER_CREATION_VALIDATABLE_FIELDS = {

    "name": {
        "required": True,
        "type": "string",
    },

    "email": {
        "required": True,
        "type": "string",
    },

    "shipping_addres": {
        "required": True,
        "type": "string",
    },

    "role": {
        "required": True,
        "type": "string",
    },


}

USER_UPDATE_VALIDATABLE_FIELDS = {

    "name": {
        "required": False,
        "type": "string",
    },

    "email": {
        "required": False,
        "type": "string",
    },

    "shipping_addres": {
        "required": False,
        "type": "string",
    },

    "role": {
        "required": False,
        "type": "string",
    },

}