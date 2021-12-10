from marshmallow import Schema
from marshmallow import fields


class FooSchema(Schema):
    # the foo name
    name = fields.String(title='foo')
