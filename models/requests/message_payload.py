from marshmallow import Schema, fields, EXCLUDE
from marshmallow.validate import Length


class MessagePayload(Schema):
    class Meta:
        unknown = EXCLUDE

    username = fields.String(required=True)
    password = fields.String(required=True)
    message = fields.String(required=True)
    numbers = fields.List(required=True, cls_or_instance=fields.String, validate=[Length(min=1)])
