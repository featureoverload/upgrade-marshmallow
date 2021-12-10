from marshmallow import Schema
from marshmallow import fields as ma_fields


class FooSchema(Schema):
    name = ma_fields.String(metadata={'title': 'foo name', 'description':
        'foo name'})
