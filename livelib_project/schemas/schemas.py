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

save_book_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "content": {
      "type": "string"
    },
    "ub_id": {
      "type": "integer"
    },
    "new_book": {
      "type": "string"
    },
    "ab_action": {
      "type": "string"
    },
    "ub_rating": {
      "type": "string"
    },
    "read_again": {
      "type": "boolean"
    },
    "is_new": {
      "type": "boolean"
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
    "text": {
      "type": "string"
    },
    "bookmark_status": {
      "type": "string"
    }
  },
  "required": [
    "content",
    "ub_id",
    "new_book",
    "ab_action",
    "ub_rating",
    "read_again",
    "is_new",
    "count_books_wish",
    "count_books_read",
    "booksmenu_wish",
    "text",
    "bookmark_status"
  ]
}