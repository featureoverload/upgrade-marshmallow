from marshmallow import Schema
from marshmallow import fields


class Foo(Schema):
    name = fields.String(title='name', description='foo name')
    tag = fields.String(default='foo', missing='foo')
