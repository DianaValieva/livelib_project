login_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "error_code": {
            "type": "integer"
        },
        "usermenu": {
            "type": "string"
        },
        "redirect": {
            "type": "string"
        },
        "object": {
            "type": "object",
            "properties": {
                "object_alias": {
                    "type": "string"
                },
                "object_id": {
                    "type": "string"
                },
                "action_object_alias": {
                    "type": "string"
                },
                "action_object_id": {
                    "type": "integer"
                },
                "action": {
                    "type": "string"
                },
                "url": {
                    "type": "string"
                },
                "event": {
                    "type": "string"
                },
                "user_id": {
                    "type": "integer"
                },
                "created_at": {
                    "type": "string"
                },
                "source": {
                    "type": "string"
                }
            },
            "required": [
                "object_alias",
                "object_id",
                "action_object_alias",
                "action_object_id",
                "action",
                "url",
                "event",
                "user_id",
                "created_at",
                "source"
            ]
        },
        "ab_action": {
            "type": "string"
        },
        "is_register": {
            "type": "boolean"
        }
    },
    "required": [
        "error_code",
        "usermenu",
        "redirect",
        "object",
        "ab_action",
        "is_register"
    ]
}

unsucessful_login_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "error_code": {
            "type": "integer"
        },
        "message": {
            "type": "string"
        }
    },
    "required": [
        "error_code",
        "message"
    ]
}

save_book_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "error_code": {
            "type": "integer"
        },
        "button": {
            "type": "string"
        },
        "content": {
            "type": "string"
        },
        "content_add": {
            "type": "string"
        },
        "text": {
            "type": "string"
        },
        "book_id": {
            "type": "integer"
        },
        "userbook_id": {
            "type": "integer"
        },
        "count_books_wish": {
            "type": "integer"
        },
        "count_books_read": {
            "type": "integer"
        },
        "booksmenu_wish": {
            "type": "string"
        },
        "bookmark_status": {
            "type": "string"
        },
        "book_read": {
            "type": "integer"
        },
        "date_field": {
            "type": "string"
        }
    },
    "required": [
        "error_code",
        "button",
        "content",
        "content_add",
        "text",
        "book_id",
        "userbook_id",
        "count_books_wish",
        "count_books_read",
        "booksmenu_wish",
        "bookmark_status",
        "book_read",
        "date_field"
    ]
}

vote_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "object_id": {
            "type": "integer"
        },
        "object_alias": {
            "type": "string"
        }
    },
    "required": [
        "object_id",
        "object_alias"
    ]
}
