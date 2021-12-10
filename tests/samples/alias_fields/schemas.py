from marshmallow import Schema
from marshmallow import fields as ma_fields


class FooSchema(Schema):
    name = ma_fields.String(title='foo name', description='foo name')
    # TODO: nested
    # fields = ma_fields.List(ma_fields.String(title='field'))
