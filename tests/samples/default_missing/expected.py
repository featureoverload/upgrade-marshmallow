from marshmallow import Schema
from marshmallow import fields


class Foo(Schema):
    name = fields.String(metadata={'title': 'name', 'description': 'foo name'})
    tag = fields.String(dump_default='foo', load_default='foo')
